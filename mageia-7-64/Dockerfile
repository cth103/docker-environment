FROM mageia:7

RUN dnf -y install gcc-c++ libxml++2.6-devel boost-devel yasm cmake openssl-devel lib64xmlsec1-devel libsndfile-devel gtk2-devel \
lib64graphicsmagick-devel libcurl-devel libsamplerate-devel libzip-devel lib64pangomm1.4-devel nettle-devel lib64wxgtku3.0-devel \
lib64ssh-devel rpm-build git lib64pulseaudio-devel alsa-lib-devel gettext lib64icu-devel curl polkit-devel lib64cairomm1.0-devel \
xerces-c-devel

# libx264 requires a newer nasm than is provided by the repos
ADD http://www.nasm.us/pub/nasm/releasebuilds/2.13/nasm-2.13.tar.xz /src/
ADD https://src.fedoraproject.org/rpms/nasm/raw/0cc3eb244bd971df81a7f02bc12c5ec259e1a5d6/f/0001-Remove-invalid-pure_func-qualifiers.patch /src/
RUN cd /src && tar xJf nasm-2.13.tar.xz && cd nasm-2.13 && ./configure && patch -p1 < ../0001-Remove-invalid-pure_func-qualifiers.patch && make -j4 && make install

# x264 is not packaged as far as I can see
ADD http://ftp.videolan.org/pub/videolan/x264/snapshots/x264-snapshot-20170705-2245.tar.bz2 /src/
RUN cd /src && tar xjf x264-snapshot-20170705-2245.tar.bz2 && cd x264-snapshot-20170705-2245 && \
./configure --enable-static --disable-shared && make -j4 && make install

RUN useradd -ms /bin/bash -u 1000 carl
RUN useradd -ms /bin/bash -u 124 jenkins
