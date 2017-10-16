#cycle through all AWS regions and grab ids of running instances and 
#compare against current list of chef server nodes. If a node no longer
#needs to be in the chef server list, remove it

## NOTE: monitor.pem is located in a databag
import boto3
import os
import re
import chef
import urllib3

def get_reservations(instance_states):
    reservations = []
    for region in boto3.client('ec2', 'us-east-1').describe_regions()['Regions']:
        reservations.extend(boto3.client('ec2', region['RegionName']).describe_instances(
            Filters=[{'Name': 'instance-state-name', 'Values': instance_states}]
        )['Reservations'])
    return reservations

def get_instances(reservations):
    return [instance for reservation in reservations for instance in reservation['Instances']]

def get_instance_ids(instances):
    return [instance['InstanceId'] for instance in instances]

def get_running_instance_ids():
    # Get Reservations of running instances
    reservations = get_reservations(['running'])

    # Get instance objects from reservations
    instances = get_instances(reservations)

    # Get instance ids from instances
    instance_ids = get_instance_ids(instances)

    return instance_ids

def get_chef_nodes(cert_path, user_name):
    with chef.ChefAPI('https://cbs-chef.hl.aws/organizations/cbs', cert_path, user_name, ssl_verify=False):
        return [str(node) for node in chef.Node.list()]

def get_instance_id_from_string(string):
    search = re.search(r'i-.{17}', string)
    if search:
        return search.group(0)

def delete_chef_nodes(cert_path, user_name, nodes):
    for node in nodes:
        if "packer" not in node:
            print(node)
            with chef.ChefAPI('https://cbs-chef.hl.aws/organizations/cbs', cert_path, user_name, ssl_verify=False):
                 n = chef.Node(node)
                 n.delete()

def main():
    ## Get the chef creds from environment variables
    cert_path = '/root/.chef/monitor.pem'
    user_name = 'monitor'

    ## Get InstanceIDs for all running ec2 instances
    running_instance_ids = get_running_instance_ids()

    ## Get InstanceIDs from chef node names
    chef_nodes = get_chef_nodes(cert_path, user_name)

    ## Isolates all nodes that are: a) in chef node list, b) not running
    non_running_chef_nodes = [i for i in chef_nodes if get_instance_id_from_string(i) not in running_instance_ids]

    ## Delete non-running nodes from chef server list
    delete_chef_nodes(cert_path, user_name, non_running_chef_nodes)

if __name__ == '__main__':
    main()
