
import os

from aws_cdk import core as cdk


from aws_cdk import core
from vpc.vpc_stack import VpcStack
from hello.hello_stack import HelloStack


app = core.App()
vpc1=VpcStack(app,"vpc")
HelloStack(app, "HelloStack",
    vpc = vpc1.vpc,
    sg_alb = vpc1.sgalb,
    sg_demo = vpc1.sgdemo
    )

app.synth()
