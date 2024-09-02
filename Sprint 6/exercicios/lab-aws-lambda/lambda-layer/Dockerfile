FROM amazonlinux:2023
RUN yum update -y
RUN yum install -y \
    python3.11 \
    python3.11-pip \
    zip
RUN yum -y clean all
RUN python3.11 -m pip install --upgrade pip