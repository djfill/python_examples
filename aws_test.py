import boto3
s3 = boto3.resource('s3')
ec2 = boto3.resource('ec2')

def list_buckets():
    # List bucket names
    print "List of buckets:"
    for bucket in s3.buckets.all():
        print(bucket.name)

def create_rhel_instance():
    # Create a Red Hat instance
    ec2.create_instances(ImageId='ami-7172b611', MinCount=1, MaxCount=1, KeyName='privateaws', SecurityGroupIds=['sg-7784460e'], InstanceType='t2.micro')

def list_ec2_instances():
    # List EC2 instances
    print "List of EC2 instances:"
    instance_iterator = ec2.instances.all()
    for instance in instance_iterator:
        print(instance.public_dns_name)

# MAIN
list_ec2_instances()
create_rhel_instance()
list_ec2_instances()
