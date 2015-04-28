#!/bin/bash
for i in {1..100}
do
      echo "/usr/bin/time -f '%e' python ising.py $i" >> scriptTiming.sh
done
