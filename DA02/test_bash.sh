#!/bin/bash
# Counting total number of arguments
echo "Total number of arguments: $#"

# Reading argument values individually
echo "First argument value : $1"
echo "Second argument value : $2"
echo "Third argument value : $3"

# Reading argument values using loop
for argval in {0..29} #"$@"
do
       echo running $argval of 30
       echo -n "$argval "
done

# Adding argument values
sum=$(($1+$2+$3))

# print the result
echo -e "\nResult of sum = $sum"