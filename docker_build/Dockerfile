# Galaxy - deepTools
#
# VERSION       0.2

FROM bgruening/galaxy-stable

LABEL maintainer="Björn A. Grüning, bjoern.gruening@gmail.com"

ENV GALAXY_CONFIG_BRAND UBUGalaxy

WORKDIR /galaxy-central

RUN add-tool-shed --url 'http://testtoolshed.g2.bx.psu.edu/' --name 'Test Tool Shed'

# Install Visualisation
RUN install-biojs msa

# Job config
ADD job_conf.xml $GALAXY_ROOT/config/job_conf.xml
RUN pip install pbs

# Style
ADD ./img/escudoubu.png $GALAXY_CONFIG_DIR/web/welcome_image.png
ADD welcome.html $GALAXY_CONFIG_DIR/web/welcome.html
ENV GALAXY_CONFIG_WELCOME_URL=$GALAXY_CONFIG_DIR/web/welcome.html

# Adding the tool definitions to the container
ADD my_tool_list.yml $GALAXY_ROOT/my_tool_list.yml

# Install deepTools
RUN install-tools $GALAXY_ROOT/my_tool_list.yml

# Install workflow
ADD workflows/* $GALAXY_HOME/workflows/
RUN startup_lite && \
    galaxy-wait && \
    workflow-install --workflow_path $GALAXY_HOME/workflows/ -g http://localhost:8080 -u $GALAXY_DEFAULT_ADMIN_USER -p $GALAXY_DEFAULT_ADMIN_PASSWORD

# Mark folders as imported from the host.
VOLUME ["/export/", "/data/", "/var/lib/docker"]

# Expose port 80 (webserver), 21 (FTP server), 8800 (Proxy)
EXPOSE :80
EXPOSE :21
EXPOSE :8800

# Autostart script that is invoked during container start
CMD ["/usr/bin/startup"]

