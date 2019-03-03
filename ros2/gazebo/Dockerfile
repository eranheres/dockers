#
# Ubuntu Node.js Dockerfile
#
# https://github.com/dockerfile/ubuntu/blob/master/Dockerfile
# https://docs.docker.com/examples/nodejs_web_app/
#

# Pull base image.
FROM ubuntu

# Install Node.js
RUN apt-get update && apt-get install --yes curl
RUN curl --silent --location https://deb.nodesource.com/setup_4.x | sudo bash -
RUN apt-get install --yes nodejs
RUN apt-get install --yes build-essential

# Bundle app source
# Trouble with COPY http://stackoverflow.com/a/30405787/2926832
COPY . /src

# Install app dependencies
RUN cd /src; npm install

# Binds to port 8080
EXPOSE  8080

#  Defines your runtime(define default command)
# These commands unlike RUN (they are carried out in the construction of the container) are run when the container
CMD ["node", "/src/index.js"]


#FROM gazebo
# install ros tutorials packages
#RUN apt-get update && apt-get install -y mercurial curl
#RUN curl -sL https://deb.nodesource.com/setup_10.x | bash -
#RUN apt-get install -y nodejs
#RUN curl -sL https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add-
#RUN apt-get update && apt-get install -y yarn
#RUN cd ~ \
#    && hg clone https://bitbucket.org/osrf/gzweb \
#    && cd ~/gzweb \
#    && hg up gzweb_1.4.0
#RUN . /usr/share/gazebo/setup.sh
#RUN npm run deploy --- -m
#WORKDIR /root
