FROM python:latest
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    cmake \
    git \
    sudo \
    wget \
    vim \
    nkf
RUN pip install --upgrade pip
COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN ln -sf /bin/bash /bin/sh
WORKDIR /work
CMD ["/bin/bash"] 