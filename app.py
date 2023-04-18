#!/usr/bin/env python3
import os
import aws_cdk as cdk
from attini_cdk import AttiniRuntimeVariables

from hello_world.hello_world_stack import HelloWorldStack

if AttiniRuntimeVariables.ENVIRONMENT not in os.environ:
    stack_prefix = "dev"
else:
    stack_prefix = os.environ[AttiniRuntimeVariables.ENVIRONMENT]

app = cdk.App()

hello_world_stack = HelloWorldStack(app, "hello-world-stack",
                                    stack_name=f"{stack_prefix}-hello-world-stack",
                                    env=cdk.Environment(
                                        account=os.getenv("CDK_DEFAULT_ACCOUNT"),
                                        region=os.environ["CDK_DEFAULT_REGION"]
                                    ))

app.synth()
