#!/bin/sh

# args 1 = year, 2 = day (2 digits), 3 = name
DIR="$1/$2_$3"
mkdir $DIR

cp template/aocYYYYDD.py $DIR/aoc$1$2.py
cp template/test_aocYYYYDD.py $DIR/test_aoc$1$2.py

sed -i -e"s/<YYYY>/${1}/g" -e"s/<DD>/${2}/g" -e"s/<Name>/${3}/g" $DIR/aoc$1$2.py
sed -i -e"s/<YYYY>/${1}/g" -e"s/<DD>/${2}/g" -e"s/<Name>/${3}/g" $DIR/test_aoc$1$2.py
