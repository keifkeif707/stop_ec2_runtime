import boto3

def stop_ec2_instances():
    ec2 = boto3.client('ec2')
    
    # Get all running instances
    response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
    
    running_instances = [instance['InstanceId'] for reservation in response['Reservations'] for instance in reservation['Instances']]
    
    if running_instances:
        # Stop running instances
        ec2.stop_instances(InstanceIds=running_instances)
        print(f'Stopping instances: {running_instances}')
    else:
        print('No running instances found')

if __name__ == "__main__":
    stop_ec2_instances()
