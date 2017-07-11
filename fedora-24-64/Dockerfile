FROM fedora:24

RUN dnf -y install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm

RUN dnf -y install gcc-c++ libxml++-devel boost-devel yasm cmake openssl-devel xmlsec1-openssl-devel libsndfile-devel libtool-ltdl-devel gtk2-devel \
	GraphicsMagick-c++-devel libcurl-devel libsamplerate-devel libzip-devel pangomm-devel nettle-devel wxGTK3-devel compat-wxGTK3-gtk2-devel \
	libssh-devel rpm-build git x264-devel pulseaudio-libs-devel alsa-lib-devel gettext make

ADD http://git.carlh.net/gitweb/?p=cdist.git;a=blob_plain;f=cdist;hb=refs/heads/docker2 /usr/bin/cdist
RUN chmod u+x /usr/bin/cdist
ADD config /root/.config/cdist
