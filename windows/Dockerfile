FROM ubuntu:16.04

RUN apt-get update
RUN apt-get -y install \
autoconf automake autopoint bash bison bzip2 flex gettext \
git g++ gperf intltool libffi-dev libgdk-pixbuf2.0-dev \
libtool-bin libltdl-dev libssl-dev libxml-parser-perl make \
openssl p7zip-full patch perl pkg-config python ruby scons \
sed unzip wget xz-utils openssh-server cmake nsis yasm curl lzip
RUN cd /opt && git clone git://git.carlh.net/git/mxe.git && cd mxe && git checkout carl-1 && make -j8

RUN useradd -ms /bin/bash -u 1000 carl
RUN useradd -ms /bin/bash -u 124 jenkins
