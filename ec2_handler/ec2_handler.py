"""Module for to ec2 EC2 deployments 
"""
import argparse
import boto.ec2


class EC2Handler(object):

    def __init__(self):

        pass


    def get_ec2_instances(self, region, kwargs):

        if(kwargs):
            ec2_conn = boto.ec2.connect_to_region(region,
                aws_access_key_id=kwargs['aws_access_key_id'],
                aws_secret_access_key=kwargs['aws_secret_access_key'])
        else:
            ec2_conn = boto.ec2.connect_to_region(region)

        reservations = ec2_conn.get_all_reservations()
        for reservation in reservations:
            print region+':',reservation.instances

        for vol in ec2_conn.get_all_volumes():
            print region+':',vol.id


def main():
    
    ec2 = EC2Handler()
    regions = ['us-east-1','us-west-1','us-west-2','eu-west-1','sa-east-1',
               'ap-southeast-1','ap-southeast-2','ap-northeast-1']
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--access-key', help='Access Key');
    parser.add_argument('-s', '--secret-key', help='Secret Key');
    args = parser.parse_args()
    aws_access_key_id = args.access_key
    aws_secret_access_key = args.secret_key

    kwargs = { 
        'aws_access_key_id': args.access_key,
        'aws_secret_access_key': args.secret_key
        }
    for region in regions: ec2.get_ec2_instances(region, kwargs)


if  __name__ =='__main__':

    main()

