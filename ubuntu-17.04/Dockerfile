FROM ubuntu:17.04

RUN apt-get update
RUN apt-get -y install git openssh-server g++ pkg-config libgtk2.0-dev libxml++2.6-dev \
    libboost-filesystem-dev libboost-test-dev libboost-locale-dev libboost-regex-dev libboost-date-time-dev libboost-thread-dev \
    libssl-dev libxmlsec1-dev cmake libx264-dev yasm libsndfile-dev libmagick++-dev libpulse-dev \
    libwxgtk3.0-dev libasound2-dev wx3.0-i18n libsamplerate-dev wget curl libpangomm-1.4-dev libssh-dev \
    libcurl4-openssl-dev libzip-dev nettle-dev

ADD id_rsa /root/.ssh/id_rsa
ADD ssh_config /root/.ssh/config
