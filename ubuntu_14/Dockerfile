FROM ubuntu:14.04

RUN apt-get update && apt-get install -y curl git vim wget \ 
    python-setuptools python-dev build-essential && \
    easy_install pip 
RUN pip install sagemaker awscli
# setting my personal env setups
RUN git clone https://github.com/eranheres/vimconfig.git && \
    cd vimconfig && \
	/bin/bash -c 'echo "source $(pwd)/vimrc-config" >> ~/.vimrc' && \
    /bin/bash -c "source setup.sh" && \
    git clone https://github.com/eranheres/bash_config.git && \ 
    cd bash_config 
