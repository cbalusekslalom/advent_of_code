#!/bin/bash

export THIS_DIR=$(pwd)
year1=0
confirm="n"

funtion_setup() {
  echo "What year would you like to setup?"
  read year1
}

if (( ${#year1} != 4 )) ; then
    echo Year value must be a 4 digit year -- 2022. >&2
fi
echo "You would like to create ${year1}?"
read confirm

### Should put limit on number of year inputs to 1
### Should confirm year
### Check if year exists, prompt to overwrite
### Build out aoc structure

