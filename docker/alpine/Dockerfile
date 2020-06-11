FROM alpine

RUN apk upgrade \
    && apk add --no-cache mc \
    make \
    python3 \
    python3-dev \
    py3-pip \
    py3-virtualenv \
    git \
    postgresql-client \
    # libpq-dev \
    # build-essential python3-setuptools python3-wheel python3-cffi \
    # libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info \
    # libpangocairo-1.0-0 \
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
