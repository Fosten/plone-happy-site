# syntax=docker/dockerfile:1
FROM node:18-slim as base
FROM base as builder

RUN <<EOT
    apt-get update
    buildDeps="python3 build-essential git ca-certificates"
    apt-get install -y --no-install-recommends $buildDeps
    rm -rf /var/lib/apt/lists/*
EOT

COPY --chown=node . /build/

RUN corepack enable
USER node
WORKDIR /build

RUN <<EOT
    mkdir -p src/addons
    make install
EOT

RUN yarn build

FROM base

LABEL maintainer="Brian Davis <info@happybaseball.com>" \
      org.label-schema.name="plone-happy-site-frontend" \
      org.label-schema.description="Plone Happy Site frontend image." \
      org.label-schema.vendor="Brian Davis"

RUN <<EOT
    apt-get update
    buildDeps="busybox"
    apt-get install -y --no-install-recommends $buildDeps
    busybox --install -s
    rm -rf /var/lib/apt/lists/*
EOT


USER node
COPY --from=builder /build/ /app/

WORKDIR /app
EXPOSE 3000
CMD ["yarn", "start:prod"]
