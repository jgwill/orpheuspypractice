FROM jgwill/ubuntu:py3.10
#ubuntu:22.04

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /install
COPY dist/* .
RUN pip install --no-cache-dir *.whl

WORKDIR /scripts
COPY scripts/* .
RUN chmod +x *.sh

WORKDIR /samples
COPY samples/*.abc .
RUN chmod 777 *
RUN chmod 777 .

# Add user jgi
RUN useradd -ms /bin/bash jgi
RUN echo "jgi ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

USER jgi

WORKDIR /work


