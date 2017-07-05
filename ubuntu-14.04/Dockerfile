FROM ubuntu:14.04

RUN apt-get update
RUN apt-get -y install git openssh-server g++ pkg-config libgtk2.0-dev libxml++2.6-dev libboost-filesystem-dev libboost-test-dev \
    libssl-dev libxmlsec1-dev cmake libboost-date-time-dev libx264-dev yasm libsndfile-dev libmagick++-dev

ADD id_rsa /root/.ssh/id_rsa
ADD ssh_config /root/.ssh/config
