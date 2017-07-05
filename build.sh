#!/bin/bash

for d in ubuntu-14.04; do
    pushd $d
    docker build -t $d .
    popd
done


