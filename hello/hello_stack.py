from aws_cdk import core as cdk
from aws_cdk import core
from aws_cdk import (aws_ec2 as ec2,
    aws_autoscaling as autoscaling,
    aws_elasticloadbalancingv2 as elb
    )

#定义实例类型
ec2_type = "t2.micro"
#定义密钥
key_name = "hello"

#导入用户数据文件
with open("./userdata/data.sh") as f:
    user_data = f.read()


class HelloStack(cdk.Stack):

    def __init__(self, scope: cdk.Construct, id: str,vpc,sg_alb,sg_demo, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # The code that defines your stack goes here
        
        #选择AMI镜像    
        ami_linux = ec2.MachineImage.latest_amazon_linux(
            
            #选择第2代亚马逊linux
            generation = ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            #选择linux版本有 minimal 和 standard 两种
            edition = ec2.AmazonLinuxEdition.STANDARD,
            #选择虚拟化类型 有 HVM 和 PV ，可不配置默认HVM
            virtualization = ec2.AmazonLinuxVirt.HVM,
            #选择存储类型 EBS 和 GENERAL_PURPOSE
            storage = ec2.AmazonLinuxStorage.EBS
            )
        
        
        #创建alb
        alb = elb.ApplicationLoadBalancer(self,"helloALB",
            vpc =vpc,
            security_group=sg_alb,
            internet_facing=True,
            load_balancer_name="helloALB"
            )
        
   
        #添加新的alb监听端口80
        listener = alb.add_listener("my80",
            port=80,
            open=True
        )
           
        #创建 AutoScaling组
        self.asg = autoscaling.AutoScalingGroup(self,"myautoscaling",
            vpc = vpc,
            #实例启动在私网子网
            vpc_subnets = ec2.SubnetSelection(subnet_type=ec2.SubnetType.PRIVATE),
            #实例类型
            instance_type=ec2.InstanceType(instance_type_identifier=ec2_type),
            #实例镜像
            machine_image = ami_linux,
            #实例密钥
            key_name =key_name,
            security_group=sg_demo,
            #实例用户数据
            user_data=ec2.UserData.custom(user_data),
            #需求2实例
            desired_capacity=2,
            #最小与最大弹性伸缩
            min_capacity=1,
            max_capacity=4
            )
     
        
        #创建alb目标组
        listener.add_targets("addTargetGroup",
            protocol = elb.ApplicationProtocol.HTTP,
            port=7777,
            
            #目标组为AutoScaling组
            targets=[self.asg]
            )
        
        #输出alb的dns地址
        core.CfnOutput(self,"Output",
            value=alb.load_balancer_dns_name
        )
