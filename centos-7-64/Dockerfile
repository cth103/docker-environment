FROM centos:7

RUN yum -y install gcc-c++ boost-devel
RUN yum -y install git
RUN yum -y --enablerepo=extras install epel-release
RUN yum -y install yasm
RUN yum -y install bzip2
RUN yum -y install make

RUN mkdir /src

# libx264 requires a newer nasm than is provided by the repos
ADD http://www.nasm.us/pub/nasm/releasebuilds/2.13/nasm-2.13.tar.xz /src/
RUN cd /src && tar xJf nasm-2.13.tar.xz && cd nasm-2.13 && ./configure && make -j4 && make install

# libx264 is not packaged by Centos as far as I can see
ADD http://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20170705-2245.tar.bz2 /src/
RUN cd /src && tar xjf x264-snapshot-20170705-2245.tar.bz2 && cd x264-snapshot-20170705-2245 && \
    ./configure --enable-static --disable-shared && make -j4 && make install

RUN yum -y install libxml++-devel
RUN yum -y install cmake