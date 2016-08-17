#!/bin/bash

var=$(grep -o "Process" t1.log | wc -l)

echo $var

if (($var > 0));
then
echo "All  Process"

else

echo "No Processing"

fi

if [-a tmp2.txt];
then
echo "File"
fi

if [ -f tmp2.txt ]
  then
    echo "/var/log/messages exists."
fi
