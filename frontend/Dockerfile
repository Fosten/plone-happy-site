# syntax=docker/dockerfile:1
ARG VOLTO_VERSION
FROM plone/frontend-builder:${VOLTO_VERSION} as builder

COPY --chown=node patches /app/patches
COPY --chown=node packages/volto-happy-site /app/packages/volto-happy-site
COPY --chown=node volto.config.js /app/
COPY --chown=node package.json /app/package.json
COPY --chown=node mrs.developer.json /app/
COPY --chown=node pnpm-workspace.yaml /app/

RUN --mount=type=cache,id=pnpm,target=/app/.pnpm-store,uid=1000 <<EOT
     pnpm dlx mrs-developer missdev --no-config --fetch-https
     pnpm install && pnpm build:deps
     pnpm build
     CI=1 pnpm install --prod
EOT

FROM plone/frontend-prod-config:${VOLTO_VERSION}

LABEL maintainer="Brian Davis <info@happybaseball.com>" \
      org.label-schema.name="plone-happy-site-frontend" \
      org.label-schema.description="Plone Happy Site frontend image." \
      org.label-schema.vendor="Brian Davis"

COPY --from=builder /app/ /app/
