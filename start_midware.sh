#!/bin/bash

# Detect system architecture
arch=$(uname -m)

# Map common architecture names to your expected values
case "$arch" in
  x86_64)    arch="amd64" ;;
  aarch64)   arch="arm64" ;;
  arm64)     arch="arm64" ;;
  *)         arch="unknown" ;;
esac

# Check if architecture-specific env file exists
env_file=".env.${arch}"
if [ ! -f "$env_file" ]; then
  echo "Error: Environment file $env_file not found"
  exit 1
fi

# Determine which compose command to use
COMPOSE_CMD="podman-compose"  # Default to podman-compose

# Check if docker-compose exists and is executable
if command -v docker-compose &> /dev/null; then
    COMPOSE_CMD="docker-compose"
    echo "Using docker-compose"
else
    echo "docker-compose not found, using podman-compose"
fi
# Run podman-compose with the architecture-specific env file
echo "Stoping containers with $env_file..."
$COMPOSE_CMD --env-file "$env_file" down
echo "Starting containers with $env_file..."
$COMPOSE_CMD --env-file "$env_file" up -d midware
echo "Start finished"