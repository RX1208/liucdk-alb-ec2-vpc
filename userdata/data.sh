

#!/bin/bash -xe
sleep 20
wget https://yc-helloworld.s3.ap-northeast-1.amazonaws.com/server_demo -O /root/server_demo
wget https://yc-helloworld.s3.ap-northeast-1.amazonaws.com/conf.toml -O /root/conf.toml
chmod a+x /root/server_demo
cd /root
/root/server_demo
