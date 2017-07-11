FROM ioft/i386-ubuntu:14.04

RUN apt-get update
RUN apt-get -y install git openssh-server g++ pkg-config libgtk2.0-dev libxml++2.6-dev \
    libboost-filesystem-dev libboost-test-dev libboost-locale-dev libboost-regex-dev libboost-date-time-dev libboost-thread-dev \
    libssl-dev libxmlsec1-dev cmake libx264-dev yasm libsndfile-dev libmagick++-dev libpulse-dev \
    libasound2-dev libsamplerate-dev wget curl libpangomm-1.4-dev libssh-dev \
    libcurl4-openssl-dev libzip-dev nettle-dev devscripts

# The distro wxWidgets does not include wx/preferences.h
RUN mkdir /src
ADD https://github.com/wxWidgets/wxWidgets/releases/download/v3.0.3/wxWidgets-3.0.3.tar.bz2 /src/
RUN cd /src && tar xjf wxWidgets-3.0.3.tar.bz2 && cd /src/wxWidgets-3.0.3 && \
    ./configure --enable-static --disable-shared --enable-prefseditor && make -j4 && make install

ADD http://git.carlh.net/gitweb/?p=cdist.git;a=blob_plain;f=cdist;hb=refs/heads/docker2 /usr/bin/cdist
RUN chmod u+x /usr/bin/cdist
ADD config /root/.config/cdist
