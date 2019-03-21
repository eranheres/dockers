# This is an example docker file on how to install and setup my neovim
# configuration
FROM ubuntu:14.04

# setting up all dependencies
RUN apt-get update && \
    apt-get install -y curl git software-properties-common python-software-properties && \
    add-apt-repository ppa:neovim-ppa/unstable && \
    apt-get update && \
    apt-get install -y neovim python-dev python-pip python3-dev python3-setuptools && \
    easy_install3 pip && \
    pip3 install neovim

RUN bash -c "ln -sf /usr/bin/python3 /usr/local/bin/python3"
RUN bash -c "ln -sf /usr/bin/python /usr/local/bin/python"
ENV LANG=C.UTF-8

# setting my personal env setups
RUN git clone https://github.com/eranheres/vimconfig.git && \
    cd vimconfig && \
    /bin/bash -c "./neovim_setup.sh"

RUN git config --global user.email "eran.heres@gmail.com"
RUN git config --global user.name "Eran Heres"

