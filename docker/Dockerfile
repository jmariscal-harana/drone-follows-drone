FROM python

RUN apt-get update &&\
    apt-get -y install sudo ffmpeg libsm6 libxext6 x11-apps

RUN pip install pytest opencv-python opencv-contrib-python

RUN adduser ubuntu --disabled-password
RUN sudo usermod -aG sudo ubuntu
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER ubuntu
WORKDIR /home/ubuntu/
COPY . drone-follows-drone/

WORKDIR /home/ubuntu/drone-follows-drone/

ENV PYTHONPATH="${PYTHONPATH}:/home/ubuntu/drone-follows-drone/"