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

# Set up the virtual display
ENV DISPLAY=:99
RUN sudo Xvfb :99 -screen 0 1024x768x16 

WORKDIR /work

# Run the application with xvfb
CMD ["xvfb-run", "-a", "
