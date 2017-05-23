#!/bin/bash

##pulls 'LastTimeUsed' for AWS IAM users' access keys
while IFS='' read -r line || [[ -n "$line" ]]; do
    echo -n "$line "
    aws iam get-access-key-last-used --access-key $line --output text | cut -f 2 >> keylast.csv
    #printf '\n'
done < "keys_hlprod.txt"

printf '\n'
echo "these are all the LastTimeUsed for each user key =)"
printf '\n'
