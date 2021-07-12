

先把项目git到本地：

* `git clone https://github.com/RX1208/liucdk-alb-ec2-vpc.git`

在 MacOS 和 Linux上创建:

```
$ python3 -m venv .venv
```

在  MacOS 和 Linux上 激活 virtualenv：

```
$ source .venv/bin/activate
```

在 windows上 激活 virtualenv：

```
% .venv\Scripts\activate.bat
```

下载需要的aws_cdk包.

```
$ pip install -r requirements.txt
```

生成堆栈文件.

```
$ cdk synth
```


## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk deploy vpcStack`       部署vpc堆栈
 * `cdk deploy ec2Stack`  部署alb-ec2堆栈
 * `cdk deploy --all`     部署所有堆栈
 * `cdk diff`        compare deployed stack with current state
 * `cdk destroy`    删除堆栈


## 更新cdk,pip

```
$ sudo npm install -g aws-cdk
$ /home/ec2-user/environment/liucdk-alb-ec2-vpc/.venv/bin/python3 -m pip install --upgrade pip
```
Enjoy!
