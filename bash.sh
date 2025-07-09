#!/bin/bash

set -e  # Exit on any error

echo "🔄 Updating system packages..."
sudo apt-get update

echo "🧼 Removing any old Docker versions..."
sudo apt-get remove -y docker docker-engine docker.io containerd runc || true

echo "📦 Installing dependencies..."
sudo apt-get install -y ca-certificates curl gnupg lsb-release

echo "🔐 Adding Docker's official GPG key..."
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/debian/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg

echo "📂 Adding Docker repository..."
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/debian $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

echo "🔄 Updating package list after adding Docker repo..."
sudo apt-get update

echo "🐳 Installing Docker and Docker Compose V2..."
sudo apt-get install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin git

echo "👤 Adding current user to Docker group..."
sudo usermod -aG docker "$USER"

echo "🔁 Restarting Docker service..."
sudo systemctl restart docker

# Step 6: Clone or update the repo
REPO_DIR="assignment_retail"
REPO_URL="git@github.com:TanmayAT/assignment_retail.git"

if [ ! -d "$REPO_DIR" ]; then
  echo "📥 Cloning the repository via SSH..."
  git clone "$REPO_URL"
fi

echo "📦 Entering repo and updating..."
cd "$REPO_DIR"
git checkout main
git fetch origin main
git pull origin main

# Step 7: Build and run containers
echo "🚀 Building and running Docker containers..."
docker compose up -d --build

echo "✅ Done! You may need to run 'newgrp docker' or restart your terminal for group changes to take effect."