#!/bin/bash

for d in debian-7-64 debin-8-64 debian-9-64 \
         ubuntu-14.04-32 ubuntu-14.04-64 \
         ubuntu-16.04-32 ubuntu-16.04-64 \
         ubuntu-16.10-32 ubuntu-16.10-64 \
         ubuntu-17.04-32 ubuntu-17.04-64; do
    pushd $d
    docker build -t $d .
    popd
done


