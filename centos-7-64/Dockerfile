FROM centos:7

RUN yum -y --enablerepo=extras install epel-release
RUN yum -y install gcc-c++ boost-devel git yasm bzip2 make libxml++-devel cmake openssl-devel

RUN mkdir /src

# libx264 requires a newer nasm than is provided by the repos
ADD http://www.nasm.us/pub/nasm/releasebuilds/2.13/nasm-2.13.tar.xz /src/
RUN cd /src && tar xJf nasm-2.13.tar.xz && cd nasm-2.13 && ./configure && make -j4 && make install

# libx264 is not packaged by Centos as far as I can see
ADD http://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20170705-2245.tar.bz2 /src/
RUN cd /src && tar xjf x264-snapshot-20170705-2245.tar.bz2 && cd x264-snapshot-20170705-2245 && \
    ./configure --enable-static --disable-shared && make -j4 && make install

ADD http://git.carlh.net/gitweb/?p=cdist.git;a=blob_plain;f=cdist;hb=refs/heads/docker2 /usr/bin/cdist
RUN chmod u+x /usr/bin/cdist
ADD config /root/.config/cdist

RUN yum -y install xmlsec1-devel ImageMagick-devel libtool
