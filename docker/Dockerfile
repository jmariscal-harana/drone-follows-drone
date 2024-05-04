FROM python

RUN apt-get update && \
    apt-get -y install sudo && \
    && apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install opencv-python

RUN adduser ubuntu --disabled-password
RUN sudo usermod -aG sudo ubuntu
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER ubuntu
WORKDIR /home/ubuntu/
COPY . drone-follows-drone/

WORKDIR /home/ubuntu/drone-follows-drone/

ENV PYTHONPATH="${PYTHONPATH}:/home/ubuntu/drone-follows-drone/"