FROM ubuntu:18.04

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update
RUN apt-get install -y vim python3-pip
RUN apt-get install -y python3-tk
RUN apt-get install -y python-opengl xvfb ffmpeg nvidia-340 mesa-utils
RUN pip3 install matplotlib gym pyvirtualdisplay

WORKDIR /root/
COPY *.py /root/

ENTRYPOINT python3 test_gym.py


