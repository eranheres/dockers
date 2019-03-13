FROM ubuntu:16.04

RUN apt-get update && \
    # General
    apt-get install -y python3-pip cmake zlib1g-dev python3-tk python-opencv && \
    # Boost libraries 
    apt-get install -y libboost-all-dev && \
    # Scipy requirements
    apt-get install -y libblas-dev liblapack-dev libatlas-base-dev gfortran && \ 
    # PyGame
    apt-get install -y libsdl-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev \
                    libsmpeg-dev libportmidi-dev libavformat-dev libswscale-dev && \
    # Dashboard
    apt-get install -y dpkg-dev build-essential python3.5-dev libjpeg-dev  libtiff-dev libsdl1.2-dev libnotify-dev \
                    freeglut3 freeglut3-dev libsm-dev libgtk2.0-dev libgtk-3-dev libwebkitgtk-dev libgtk-3-dev libwebkitgtk-3.0-dev \
                    libgstreamer-plugins-base1.0-dev  && \
    # Gym
    apt-get install -y libav-tools libsdl2-dev swig cmake  && \
    # others
    apt-get install -y vim git 

RUN pip3 install virtualenv
RUN virtualenv -p python3 coach_env
ENV PATH="/coach_env/bin:${PATH}"
ENV VIRTUAL_ENV=/coach_env
RUN pip3 install rl_coach
