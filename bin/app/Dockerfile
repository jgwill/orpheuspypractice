FROM jgwill/orpheus:base


ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y xvfb \
  x11-xkb-utils xfonts-100dpi  \
  xfonts-75dpi \
  xfonts-scalable \
  xfonts-cyrillic \
  x11-apps 

RUN apt install -y xterm

# Add user jgi
RUN useradd -ms /bin/bash jgi
RUN echo "jgi ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers


WORKDIR /install
COPY dist/* .
RUN pip install --no-cache-dir *.whl

WORKDIR /scripts
COPY scripts/* .
RUN chmod +x *.sh
WORKDIR /samples
COPY samples/*.abc .

USER jgi
WORKDIR /work


# Set up the virtual display
ENV DISPLAY=:99
RUN sudo Xvfb :99 -screen 0 1024x768x16 &

WORKDIR /app
# Run the application with xvfb
CMD ["xvfb-run", "-a", "/scripts/run.sh"]


