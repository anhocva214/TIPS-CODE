FROM ubuntu:latest

EXPOSE 5500


#update ubuntu
RUN apt-get -y update

# install ssh
RUN apt-get -y install ssh

#install the build-essential package
RUN apt-get install build-essential -y

#install curl
RUN apt-get install curl -y

# install git
RUN apt-get install git -y

# install nodejs
RUN curl -sL https://deb.nodesource.com/setup_12.x | bash
RUN apt-get install nodejs -y
RUN npm install -g yarn

# Git clone repositories private
# WORKDIR /home
# COPY github_key .
# RUN eval $(ssh-agent) && \
#     ssh-add github_key && \
#     ssh-keyscan -H github.com >> /etc/ssh/ssh_known_hosts && \
#     git clone git@github.com:<username>/<repo-name>.git


# Use source in this folder
WORKDIR /home/app
COPY ./ ./ 


#====================================RUN===============================================
RUN yarn install
RUN yarn build
CMD ["yarn", "start"]
