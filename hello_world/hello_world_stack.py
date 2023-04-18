from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    CfnOutput,
    aws_sqs as sqs,
    aws_sns as sns,
    aws_sns_subscriptions as subs,
)


class HelloWorldStack(Stack):
    sns_topic_name = "SnsTopicName"

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        queue = sqs.Queue(
            self, "HelloWorldQueue",
            visibility_timeout=Duration.seconds(300),
        )

        topic = sns.Topic(
            self, "HelloWorldTopic"
        )

        topic.add_subscription(subs.SqsSubscription(queue))

        CfnOutput(self, "SnsTopicName",
                  value=topic.topic_name
                  )
