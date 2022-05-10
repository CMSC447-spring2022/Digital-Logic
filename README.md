# DigitalLogic
We created a Python Django based web app that supports a password protected launch into backend Docker workspace 
configured to run a modified version of Logisim.

### Login Page
To run the account based features, a `secret` file needs to be one directory above Digital-Logic.
If `secret` is not there, then users won't be able to sign up of do other account maintenance.

To debug, remove the `secret` file or use `Email(debug=True)`. Emails will not be sent in debug mode.

### Launcher
The launcher client communicates with a backend server running Kasm hosted on AWS.  
Kasm is a Docker container launcher.  When a user logs in they can get a fresh 
Logisim workspace.

### Selenium Tests
To run Selenium tests as a developer, run the app locally, then run the Selenium
integration tests.

### Kasm Customization
```dockerfile
FROM kasmweb/core-ubuntu-bionic:1.10.0
USER root

ENV HOME /home/kasm-default-profile
ENV STARTUPDIR /dockerstartup
ENV INST_SCRIPTS $STARTUPDIR/install
WORKDIR $HOME

######### Customize Container Here ###########

# Install Google Chrome
COPY ./src/ubuntu/install/chrome $INST_SCRIPTS/chrome/
RUN bash $INST_SCRIPTS/chrome/install_chrome.sh  && rm -rf $INST_SCRIPTS/chrome/

# Install VLC
RUN apt-get update && apt-get install -y vlc

# Install Shotcut
COPY ./src/ubuntu/install/shotcut/Shotcut.desktop $HOME/Desktop/
WORKDIR /tmp
RUN wget https://github.com/mltframework/shotcut/releases/download/v21.10.31/shotcut-linux-x86_64-211031.txz && \
    tar -xf shotcut-linux-x86_64-211031.txz -C /opt

ENV DESKTOP /home/kasm-user/Desktop/
WORKDIR $DESKTOP

RUN wget https://iweb.dl.sourceforge.net/project/circuit/2.7.x/2.7.1/logisim-generic-2.7.1.jar

WORKDIR $DESKTOP

USER root
RUN su
RUN apt update
RUN apt install default-jre -y
RUN echo '#!/bin/bash \njava -jar ~/Desktop/logisim-generic-2.7.1.jar' > setup
RUN chmod +x setup

######### End Customizations ###########

RUN chown 1000:0 $HOME
RUN $STARTUPDIR/set_user_permission.sh $HOME

ENV HOME /home/kasm-user
WORKDIR $HOME
RUN mkdir -p $HOME && chown -R 1000:0 $HOME

USER 1000

```