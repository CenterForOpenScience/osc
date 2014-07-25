#!/bin/sh
set -e   # if there's an error, stop running
set -x   # print each command as it runs

old="src=images\/"
new="src=\"images\/"

for file in $(git grep $old | cut -d':'  -f 1 | uniq)
do
  echo "replacing '$old' with '$new' in '$file'"
  sed -i -e "s/$old/$new/g" $file
done
