#!/bin/bash
for i in {1..100}
do
      /usr/bin/time -f '%e' python isingTotalEnergyDifference.py $i
done
