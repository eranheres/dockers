FROM consol/ubuntu-xfce-vnc
ENV REFRESHED_AT 2018-03-18
LABEL maintainer "eran.heres@gmail.com"

# Switch to root user to install additional software
USER 0

#USER 1000

# Basic command line tools
RUN apt-get update && apt-get install -y wget git nano curl lsb-release software-properties-common \
       python-dev python-pip python3-dev python3-pip 
RUN add-apt-repository ppa:neovim-ppa/stable
RUN apt-get update && apt-get install -y neovim 

# Installing ROS
RUN sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
RUN apt-key adv --keyserver hkp://ha.pool.sks-keyservers.net:80 --recv-key 421C365BD9FF1F717815A3895523BAEEB01FA116
RUN apt-get update && apt-get install -y ros-kinetic-desktop-full
RUN rosdep init 

## switch back to default user
USER 1000
RUN rosdep update

# Update Gazebo 7
USER 0
RUN sh -c 'echo "deb http://packages.osrfoundation.org/gazebo/ubuntu-stable `lsb_release -cs` main" > /etc/apt/sources.list.d/gazebo-stable.list'
RUN wget http://packages.osrfoundation.org/gazebo.key -O - | apt-key add -
RUN apt-get update && apt-get install -y gazebo7 libignition-math2-dev

# setting my personal env setups
RUN git clone https://github.com/eranheres/vimconfig.git && \
    cd vimconfig 
#WORKDIR /root
