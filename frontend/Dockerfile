# syntax=docker/dockerfile:1
ARG VOLTO_VERSION
FROM plone/frontend-builder:${VOLTO_VERSION} as builder

COPY --chown=node packages/volto-happy-site /app/packages/volto-happy-site
COPY --chown=node volto.config.js /app/
COPY --chown=node package.json /app/package.json.temp
COPY --chown=node mrs.developer.json /app/

RUN --mount=type=cache,id=pnpm,target=/app/.pnpm-store,uid=1000 <<EOT
     python3 -c "import json; data = json.load(open('package.json.temp')); deps = data['dependencies']; data['dependencies'].update(deps); json.dump(data, open('package.json', 'w'), indent=2)"
     rm package.json.temp
     pnpm dlx mrs-developer missdev --no-config --fetch-https
     pnpm install && pnpm build:deps
     pnpm build
     pnpm install --prod
EOT

FROM plone/frontend-prod-config:${VOLTO_VERSION}

LABEL maintainer="Brian Davis <info@happybaseball.com>" \
      org.label-schema.name="plone-happy-site-frontend" \
      org.label-schema.description="Plone Happy Site frontend image." \
      org.label-schema.vendor="Brian Davis"

COPY --from=builder /app/ /app/
