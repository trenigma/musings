#!/usr/bin/env python3
import boto3

iam = boto3.client('iam')
#key = []
with open('keys_hlprod.txt') as f:
    for line in iter(f):
        print(line.strip('\n\r'))
        response = iam.get_access_key_last_used(AccessKeyId=line.strip('\n\r'))
        print(response['AccessKeyLastUsed'])