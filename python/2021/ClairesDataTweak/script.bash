!#/bin/hash

for line in $(awk -F: '{print $1}' Claires2.csv)
do
	echo $line
done
