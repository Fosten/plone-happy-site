# syntax=docker/dockerfile:1
ARG PLONE_VERSION=6.0.0.2
FROM plone/plone-backend:${PLONE_VERSION}

LABEL maintainer="Brian Davis <info@happybaseball.com>" \
      org.label-schema.name="plone-happy-site-backend" \
      org.label-schema.description="Plone Happy Site backend image." \
      org.label-schema.vendor="Brian Davis"

# Add local code
COPY . .

# Install local requirements and fix permissions
RUN <<EOT
    ./bin/pip install mxdev
    mv requirements-docker.txt requirements.txt
    ./bin/mxdev -c mx.ini
    ./bin/pip install -r requirements-mxdev.txt
    chown -R plone: /app
EOT
