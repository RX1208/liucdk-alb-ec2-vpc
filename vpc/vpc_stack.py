from aws_cdk import (core,aws_ec2 as ec2)


class VpcStack(core.Stack):
    
    def __init__(self,scope: core.Construct,id:str,**kwargs) -> None:
        super().__init__(scope,id,**kwargs)
         
         
        #创建VPC   
        self.vpc = ec2.Vpc(self,"vpc",
            
            #两个可用区
            max_azs = 2,
            #1个nat网关
            nat_gateways = 1,
            #创建公网子网和私网子网
            subnet_configuration = [ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PUBLIC,
                name = "public"
                ),ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PRIVATE,
                name = "private"
                )
                ])
                
        
        #创建alb安全组        
        self.sgalb = ec2.SecurityGroup(self,"sg_alb",
            #选择vpc
            vpc =self.vpc ,
            #自定义安全组名称
            security_group_name = "sg_elb",
            #默认开放所有出站流量
            allow_all_outbound = True
            )
        #添加80入站端口
        self.sgalb.connections.allow_from_any_ipv4(ec2.Port.tcp(80))

        #创建ec2安全组 
        self.sgdemo = ec2.SecurityGroup(self,"sg_demo",
            vpc = self.vpc ,
            security_group_name = "sg_demo",
            allow_all_outbound = True
            )
        #安全组接收alb的80端口流量
        self.sgdemo.connections.allow_from(self.sgalb,ec2.Port.tcp(80))
        
        
        #输出vpc id
        core.CfnOutput(self,"Output_vpc",
            value=self.vpc.vpc_id)
        
        #输出安全组alb id    
        core.CfnOutput(self,"Output_sgalb",
            value=self.sgalb.security_group_id)
        #输出安全组 demo id
        core.CfnOutput(self,"Output_sgdemo",
            value=self.sgdemo.security_group_id)
