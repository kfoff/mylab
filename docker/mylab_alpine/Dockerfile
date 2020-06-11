FROM alpine

RUN apk upgrade \
    && apk add --no-cache mc \
    make \
    build-base \
    gcc \
    linux-headers \
    python3 \
    python3-dev \
    py3-pip \
    py3-virtualenv \
    git \
    postgresql-client \
    postgresql-dev \
    libffi-dev \
    jpeg-dev zlib-dev \
    && pip3 install --no-cache-dir --upgrade pip \
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
