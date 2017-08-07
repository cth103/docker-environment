FROM centos:6

RUN yum -y --enablerepo=extras install epel-release
RUN yum -y install gcc-c++ git yasm bzip2 make libxml++-devel cmake openssl-devel xz libtool-ltdl-devel \
    xmlsec1-devel ImageMagick-devel ImageMagick-c++-devel libtool python-argparse xmlsec1-openssl-devel pcre-devel xz-devel pulseaudio-libs-devel \
    alsa-lib-devel gtk2-devel libcurl-devel libicu-devel libsamplerate-devel libzip-devel pangomm-devel nettle-devel \
    gettext libssh-devel libsndfile-devel rpm-build

RUN mkdir /src

# libx264 requires a newer nasm than is provided by the repos
ADD http://www.nasm.us/pub/nasm/releasebuilds/2.13/nasm-2.13.tar.xz /src/
RUN cd /src && tar xJf nasm-2.13.tar.xz && cd nasm-2.13 && ./configure && make -j4 && make install

# libx264 is not packaged by Centos as far as I can see
ADD http://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20170705-2245.tar.bz2 /src/
RUN cd /src && tar xjf x264-snapshot-20170705-2245.tar.bz2 && cd x264-snapshot-20170705-2245 && \
    ./configure --enable-static --disable-shared && make -j4 && make install

# boost is too old
ADD https://dl.bintray.com/boostorg/release/1.63.0/source/boost_1_63_0.tar.bz2 /src/
RUN cd /src && tar xjf boost_1_63_0.tar.bz2 && cd boost_1_63_0 && ./bootstrap.sh && ./b2 link=static --without-python install

# We need wxWidgets3 linked against GTK2
ADD https://github.com/wxWidgets/wxWidgets/releases/download/v3.0.3/wxWidgets-3.0.3.tar.bz2 /src/
RUN cd /src && tar xjf wxWidgets-3.0.3.tar.bz2 && cd /src/wxWidgets-3.0.3 && \
    ./configure --enable-static --disable-shared --enable-prefseditor && make -j8 && make install

# curl is too old
ADD https://curl.haxx.se/download/curl-7.54.1.tar.bz2 /src/
RUN cd /src && tar xjf curl-7.54.1.tar.bz2 && cd /src/curl-7.54.1 && ./configure --enable-static --disable-shared && make -j8 && make install
