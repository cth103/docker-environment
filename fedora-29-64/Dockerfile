FROM fedora:29

RUN dnf -y install gcc-c++ libxml++-devel boost-devel cmake openssl-devel xmlsec1-openssl-devel libsndfile-devel libtool-ltdl-devel gtk2-devel \
GraphicsMagick-c++-devel libcurl-devel libsamplerate-devel libzip-devel pangomm-devel nettle-devel wxGTK3-devel compat-wxGTK3-gtk2-devel \
libssh-devel rpm-build git pulseaudio-libs-devel alsa-lib-devel gettext make polkit-devel xerces-c-devel

ADD http://www.nasm.us/pub/nasm/releasebuilds/2.13/nasm-2.13.tar.xz /src/
ADD https://src.fedoraproject.org/rpms/nasm/raw/0cc3eb244bd971df81a7f02bc12c5ec259e1a5d6/f/0001-Remove-invalid-pure_func-qualifiers.patch /src/
RUN cd /src && tar xJf nasm-2.13.tar.xz && cd nasm-2.13 && ./configure && patch -p1 < ../0001-Remove-invalid-pure_func-qualifiers.patch && make -j4 && make install
ADD http://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20170705-2245.tar.bz2 /src/
RUN cd /src && tar xjf x264-snapshot-20170705-2245.tar.bz2 && cd x264-snapshot-20170705-2245 && \
./configure --enable-static --disable-shared && make -j4 && make install
RUN useradd -ms /bin/bash -u 1000 carl
RUN useradd -ms /bin/bash -u 124 jenkins
