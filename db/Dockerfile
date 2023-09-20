FROM postgres:15-alpine
RUN mkdir -p /docker-entrypoint-initdb.d
COPY db/init-db.sh /docker-entrypoint-initdb.d/init-db.sh