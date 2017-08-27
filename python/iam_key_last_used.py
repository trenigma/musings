""" Goal here is three-fold:
a) get usernames
b) get keys
c) get last used time
"""

import boto3

# Create IAM client
iam = boto3.client('iam')
resource = boto3.resource('iam')

for user in resource.users.all():
	for key in user.access_keys.all():
		#do stuff with the key
            response = iam.get_access_key_last_used(AccessKeyId=key.access_key_id)
            #print(response)
            result = 'no last used date'
            if 'LastUsedDate' in response['AccessKeyLastUsed']:
                result = response['AccessKeyLastUsed']['LastUsedDate']
            print(response['UserName'] + ' - ' + key.access_key_id + ' - ' + str(result))
