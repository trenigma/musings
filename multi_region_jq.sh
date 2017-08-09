for region in `aws ec2 describe-regions --output text | cut -f3`
do
     echo -e "\nListing Instances in region:'$region'..."
     aws ec2 describe-instances --region $region | jq '.Reservations[] | ( .Instances[] | {state: .State.Name, name: (.Tags[]|select(.Key=="Name").Value), id: .InstanceId, type: .InstanceType, key: .KeyName})'
done