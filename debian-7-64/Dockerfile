FROM debian:7

RUN apt-get update
RUN apt-get -y install git openssh-server g++ pkg-config libgtk2.0-dev libxml++2.6-dev \
libboost-filesystem-dev libboost-test-dev libboost-locale-dev libboost-regex-dev libboost-date-time-dev libboost-thread-dev \
libssl-dev libxmlsec1-dev cmake libx264-dev libsndfile-dev libmagick++-dev libpulse-dev \
libasound2-dev libsamplerate-dev wget curl libpangomm-1.4-dev \
libcurl4-openssl-dev libzip-dev nettle-dev libssh-dev devscripts liblzma-dev

# No wxwidgets 3 in the distro
RUN mkdir /src
ADD https://github.com/wxWidgets/wxWidgets/releases/download/v3.0.3/wxWidgets-3.0.3.tar.bz2 /src/
RUN cd /src && tar xjf wxWidgets-3.0.3.tar.bz2 && cd /src/wxWidgets-3.0.3 && \
./configure --enable-static --disable-shared --enable-prefseditor && make -j4 && make install

# Need a more up-to-date yasm
ADD http://www.tortall.net/projects/yasm/releases/yasm-1.3.0.tar.gz /src/
RUN cd /src && tar xzf yasm-1.3.0.tar.gz && cd yasm-1.3.0 && \
./configure && make -j8 && make install

RUN useradd -ms /bin/bash -u 1000 carl
RUN useradd -ms /bin/bash -u 127 jenkins
