#!/bin/sh

echo "Waiting for PostgreSQL..."
while ! nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 0.1
done
echo "PostgreSQL started"

if [ "$REDIS_HOST" ]; then
  echo "Waiting for Redis..."
  while ! nc -z "$REDIS_HOST" "$REDIS_PORT"; do
    sleep 0.1
  done
  echo "Redis started"
fi

exec "$@"
