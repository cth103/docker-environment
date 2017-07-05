FROM fedora:24

RUN dnf -y install gcc-c++ libxml++-devel boost-devel yasm cmake openssl-devel xmlsec1-openssl-devel libsndfile-devel libtool-ltdl-devel gtk2-devel \
	GraphicsMagick-c++-devel libcurl-devel libsamplerate-devel libzip-devel pangomm-devel nettle-devel wxGTK3-devel compat-wxGTK3-gtk2-devel \
	libssh-devel rpm-build

ADD id_rsa /root/.ssh/id_rsa
ADD ssh_config /root/.ssh/config
