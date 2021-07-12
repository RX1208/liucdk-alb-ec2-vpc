
import os

from aws_cdk import core
from vpc.vpc_stack import VpcStack
from hello.hello_stack import albec2Stack


app = core.App()
vpc1=VpcStack(app,"vpc")
albec2Stack(app, "HelloStack",
    vpc = vpc1.vpc,
    sg_alb = vpc1.sgalb,
    sg_demo = vpc1.sgdemo
    )

app.synth()
