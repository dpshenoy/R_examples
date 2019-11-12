#! /bin/bash

# compiles the files into a single text file with
# the 7 header lines stripped.

# delete previous one
rm -f allyears.txt

for file in 19*.txt 2000s.txt
do
    sed -n 8,3660p $file >> allyears.txt
done

