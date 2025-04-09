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

echo "Set arch to $arch"

# specify podman image
if [ "$arch" = "arm64" ]; then
  export CROSSBAR_IMAGE=crossbario/crossbar-aarch64
else
  export CROSSBAR_IMAGE=crossbario/crossbar
fi

# Determine which compose command to use
COMPOSE_CMD="podman-compose"  # Default to podman-compose

# Check if docker-compose exists and is executable
if command -v docker-compose &> /dev/null; then
    COMPOSE_CMD="docker-compose"
fi
echo "Using $COMPOSE_CMD"
# Run podman-compose with the architecture-specific env file
echo "Stopping containers"
$COMPOSE_CMD down midware
echo "Starting containers"
$COMPOSE_CMD up -d midware
echo "Start finished"