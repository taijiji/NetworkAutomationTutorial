FROM centos:7 AS sample_ansible

MAINTAINER Taiji Tsuchiya <ttsuchiya@ctc-america.com>

VOLUME ["/sample_ansible", "./sample_ansible"]

RUN yum -y install yum-utils
RUN yum -y install https://centos7.iuscommunity.org/ius-release.rpm


# Install Python3,6 environment
RUN yum -y install python36u
RUN python3.6 -V
RUN yum -y install python36u-pip
RUN pip3.6 -V
RUN yum -y install python36u-devel.x86_64

WORKDIR /
RUN pip3.6 install -r requirements.txt