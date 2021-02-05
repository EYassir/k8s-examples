aws ec2 create-volume \
--size 80 --region eu-west-1 \
--availability-zone eu-west-1a \
--volume-type gp2 \
--tag-specifications 'ResourceType=volume,Tags=[{Key=Name,Value=hello}]'