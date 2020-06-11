# FROM ubuntu:18.04
FROM ubuntu:20.04

# EXPOSE 5432

# RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Asia/Krasnoyarsk /etc/localtime

RUN apt update && apt install -y mc \
    net-tools \
    python3 \
    python3-dev \
    python3-pip \
    python3-venv \
    git \
    wget \
    postgresql \
    postgresql-client \
    libpq-dev \
    build-essential python3-setuptools python3-wheel python3-cffi \
    # libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    && pip3 install virtualenv

RUN mkdir /home/git/ \
    /home/www/ \
    /home/www/project/ \
    /home/disc/ \
    /root/.ssh/

WORKDIR /home/git/

RUN git clone https://github.com/discoroveryx/mylab \
    && ln -s /home/git/mylab/mylab-docker /bin \
    && mylab-docker

WORKDIR /home/www/project/
