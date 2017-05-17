#!/bin/bash

while IFS='' read -r line || [[ -n "$line" ]]; do
    echo -n "$line "
    aws iam list-groups-for-user --user-name $line --output text | cut -f 5 | (tr '\n' ' ' )
    printf '\n'
done < "usersforloop.txt"

printf '\n'
echo "these are all the groups for each user =)"
printf '\n'
#done