from aws_cdk import (core,aws_ec2 as ec2)


class VpcStack(core.Stack):
    
    def __init__(self,scope: core.Construct,id:str,**kwargs) -> None:
        super().__init__(scope,id,**kwargs)
            
        self.vpc = ec2.Vpc(self,"vpc",
            max_azs = 2,
            nat_gateways = 1,
            subnet_configuration = [ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PUBLIC,
                name = "public"
                ),ec2.SubnetConfiguration(
                subnet_type = ec2.SubnetType.PRIVATE,
                name = "private"
                )
                ])
                
                
        self.sgalb = ec2.SecurityGroup(self,"sg_alb",
            vpc =self.vpc ,
            security_group_name = "sg_elb",
            allow_all_outbound = True
            )
        self.sgalb.connections.allow_from_any_ipv4(ec2.Port.tcp(80))

         
        self.sgdemo = ec2.SecurityGroup(self,"sg_demo",
            vpc = self.vpc ,
            security_group_name = "sg_demo",
            allow_all_outbound = True
            )
        
        self.sgdemo.connections.allow_from(self.sgalb,ec2.Port.tcp(7777))
        
        core.CfnOutput(self,"Output_vpc",
            value=self.vpc.vpc_id)
        
            
        core.CfnOutput(self,"Output_sgalb",
            value=self.sgalb.security_group_id)
        
        core.CfnOutput(self,"Output_sgdemo",
            value=self.sgdemo.security_group_id)
