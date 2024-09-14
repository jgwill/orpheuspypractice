FROM jgwill/ubuntu:py3.10

ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y xvfb \
  x11-xkb-utils xfonts-100dpi  \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  x11-apps 

RUN apt install -y xterm

RUN apt update && apt install abcmidi musescore3 -y

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
WORKDIR /scripts
COPY scripts/* .
RUN chmod +x *.sh
WORKDIR /samples
COPY samples/*.abc .

WORKDIR /work