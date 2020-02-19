FROM debian

EXPOSE 5432

RUN rm /etc/localtime
RUN ln -s /usr/share/zoneinfo/Asia/Krasnoyarsk /etc/localtime

RUN apt update
RUN apt install -y mc
RUN apt install -y net-tools
RUN apt install -y python3
RUN apt install -y python3-dev
RUN apt install -y python3-pip
RUN apt install -y python3-venv
RUN apt install -y git git-lfs
RUN apt install -y wget
RUN apt install -y postgresql
RUN apt install -y libpq-dev
RUN apt install -y build-essential python3-setuptools python3-wheel python3-cffi
# RUN apt install -y libcairo2 libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0 libffi-dev shared-mime-info

RUN pip3 install virtualenv

RUN mkdir /home/git/
RUN mkdir /home/www/
RUN mkdir /home/disc
RUN mkdir /root/.ssh/

WORKDIR /home/git/

RUN git clone https://github.com/roveryx/mylab
RUN ln -s /home/git/mylab/mylab-docker /bin
RUN mylab-docker
