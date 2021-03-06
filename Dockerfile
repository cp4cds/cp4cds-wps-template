# vim:set ft=dockerfile:
FROM debian:latest
MAINTAINER https://github.com/cp4cds/myapp

LABEL Description="MyApp: a WPS template for CP4CDS" Vendor="CP4CDS" Version="1.0"

# Configure hostname and ports for services
ENV HTTP_PORT 5000
ENV HTTPS_PORT 5001
ENV OUTPUT_PORT 8000
ENV HOSTNAME localhost

# Set current home
ENV HOME /root

# Copy application sources
COPY . /opt/birdhouse/src/myapp

# cd into application
WORKDIR /opt/birdhouse/src/myapp

# Provide custom.cfg with settings for docker image
RUN printf "[buildout]\nextends=profiles/docker.cfg" > custom.cfg

# Install system dependencies
RUN bash bootstrap.sh -i

# Set conda enviroment
ENV ANACONDA_HOME /opt/conda
ENV CONDA_ENVS_DIR /opt/conda/envs

# Run install and fix permissions
RUN make clean install && chmod 755 /opt/birdhouse/etc && chmod 755 /opt/birdhouse/var/run

# Volume for data, cache, logfiles, ...
#VOLUME /opt/birdhouse/var/lib
#VOLUME /opt/birdhouse/var/log
# Volume for configs
#VOLUME /opt/birdhouse/etc

# Ports used in birdhouse
EXPOSE $HTTP_PORT $OUTPUT_PORT

# Start supervisor in foreground
ENV DAEMON_OPTS --nodaemon

# Start service ...
CMD ["make", "update-config", "start"]
