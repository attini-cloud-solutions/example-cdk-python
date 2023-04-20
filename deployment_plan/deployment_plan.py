from attini_cdk import (
    AttiniRunner,
    RunnerConfiguration,
    AttiniDeploymentPlanStack,
    AttiniCdk,
    AttiniRunnerJob,
    DeploymentPlan,
)
from constructs import Construct
import aws_cdk as cdk
import app as hello_world_app


class DeploymentPlanStack(AttiniDeploymentPlanStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        hello_world_stack = hello_world_app.hello_world_stack

        runner = AttiniRunner(self, "runner",
                              runner_configuration=RunnerConfiguration(
                                  job_timeout=3600
                              ))

        deploy_cdk_app = AttiniCdk(self, "deploy_cdk_app",
                                   runner=runner.runner_name,
                                   path="./"
                                   )

        run_script = AttiniRunnerJob(self, 'run_script',
                                     runner=runner.runner_name,
                                     environment={
                                         "SNS_TOPIC": deploy_cdk_app.get_output(
                                             hello_world_stack.artifact_id,
                                             hello_world_stack.sns_topic_name
                                         )
                                     },
                                     commands=[
                                         'echo "My SNS topic is: $SNS_TOPIC"'
                                     ])

        DeploymentPlan(self, "deployment_plan",
                       definition=deploy_cdk_app.next(run_script)
                       )


deployment_plan_app = cdk.App()

DeploymentPlanStack(deployment_plan_app, "DeploymentPlanAppStack")

deployment_plan_app.synth()
