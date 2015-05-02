"""Module for to ec2 EC2 deployments
"""
import argparse
import boto.ec2

REGIONS = [
    'us-east-1', 'us-west-1', 'us-west-2', 'eu-west-1', 'sa-east-1',
    'ap-southeast-1', 'ap-southeast-2', 'ap-northeast-1'
]

class EC2Handler(object):

    def __init__(self):

        pass

    def instance_newest(self, region, filters, kwargs):
        
        instance_newest = ''
        launch_time_prev = '2000-01-01'

        if(kwargs):
            ec2_conn = boto.ec2.connect_to_region(
                region,
                aws_access_key_id=kwargs['aws_access_key_id'],
                aws_secret_access_key=kwargs['aws_secret_access_key']
            )
        else:
            ec2_conn = boto.ec2.connect_to_region(region)

        reservations = ec2_conn.get_all_instances(filters=filters)
        for reservation in reservations:
            for instance in reservation.instances:
                #current_instance = '{}: {} - {}'.format(
                #    region, 
                #    instance.id,
                #    instance.tags['Name'],
                #    instance.launch_time
                #) 
                #print current_instance
                if instance.launch_time > launch_time_prev:
                    instance_newest = instance 
                launch_time_prev = instance.launch_time
        
        return instance_newest

    def instance_report(self, region, instance):
        return '{}: {} - {} - {}'.format(
            region, 
            instance.id,
            instance.tags['Name'],
            instance.public_dns_name,
            instance.launch_time
        ) 


def main():

    regions = REGIONS
    ec2 = EC2Handler()
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--access-key', help='Access Key')
    parser.add_argument('-s', '--secret-key', help='Secret Key')
    parser.add_argument('-r', '--region')
    parser.add_argument('-p', '--product-name', 
        help='Product Name (i.e. loop_client)')
    args = parser.parse_args()
    aws_access_key_id = args.access_key
    aws_secret_access_key = args.secret_key
    product_name = args.product_name
    if args.region:
        regions = []
        regions.append(args.region)
 
    kwargs = {
        'aws_access_key_id': aws_access_key_id,
        'aws_secret_access_key': aws_secret_access_key
    }
    filters = {
        'tag:Type': product_name
    }

    for region in regions:
        instance = ec2.instance_newest(region, filters, kwargs)
        print(ec2.instance_report(region, instance))

if __name__ == '__main__':

    main()
