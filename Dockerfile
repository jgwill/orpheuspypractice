FROM jgwill/ubuntu:py3.10
#ubuntu:22.04

WORKDIR /install
COPY dist/* .
RUN pip install --no-cache-dir *.whl

WORKDIR /scripts
COPY scripts/* .

# Add user jgi
RUN useradd -ms /bin/bash jgi
RUN echo "jgi ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER jgi

WORKDIR /work


