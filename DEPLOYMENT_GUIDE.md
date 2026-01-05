# Global Deployment Guide for Message Encryption

## Overview

This guide provides comprehensive instructions to deploy the Message Encryption application globally across multiple platforms and services.

## Table of Contents

1. [PyPI Distribution](#pypi-distribution)
2. [Docker Container Deployment](#docker-container-deployment)
3. [Cloud Platform Deployments](#cloud-platform-deployments)
4. [Installation Methods](#installation-methods)

---

## PyPI Distribution

### Publishing to PyPI

1. **Create PyPI Account**
   - Register at [pypi.org](https://pypi.org/account/register/)
   - Generate API token from account settings

2. **Configure GitHub Secrets**
   - Go to Repository Settings > Secrets and variables > Actions
   - Add secret: `PYPI_API_TOKEN` with your PyPI API token

3. **Create Release**
   - Tag your commit: `git tag v1.0.0`
   - Push tag: `git push origin v1.0.0`
   - GitHub Actions will automatically publish to PyPI

4. **Install from PyPI**
   ```bash
   pip install message-encryption
   ```

---

## Docker Container Deployment

### Build Docker Image

```bash
# Clone repository
git clone https://github.com/latituded3420/message-encryption.git
cd message-encryption

# Build image
docker build -t message-encryption:latest .

# Run container
docker run -it message-encryption:latest
```

### Push to Docker Hub

```bash
# Tag image
docker tag message-encryption:latest yourusername/message-encryption:latest

# Login to Docker Hub
docker login

# Push image
docker push yourusername/message-encryption:latest
```

---

## Cloud Platform Deployments

### Render.com Deployment

1. **Create Render Account**
   - Visit [render.com](https://render.com)
   - Connect GitHub account

2. **Deploy Web Service**
   - Click "New +" > Web Service
   - Select this repository
   - Set build command: `pip install -e .`
   - Set start command: `message-encryption`
   - Deploy

### Heroku Deployment (Legacy)

```bash
# Install Heroku CLI
# Create app
heroku create your-app-name

# Add Procfile (create in root):
# Procfile content: web: message-encryption

# Deploy
git push heroku main
```

### AWS Deployment

#### Option 1: EC2 Instance

```bash
# SSH into EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Update system
sudo yum update -y

# Install Python
sudo yum install python3 python3-pip -y

# Clone and install
git clone https://github.com/latituded3420/message-encryption.git
cd message-encryption
pip install -e .

# Run as service
message-encryption
```

#### Option 2: Docker on ECS

1. Build and push Docker image to AWS ECR
2. Create ECS task definition
3. Deploy service

---

## Installation Methods

### Method 1: pip (Recommended)

```bash
pip install message-encryption
message-encryption
```

### Method 2: Docker

```bash
docker pull latituded3420/message-encryption:latest
docker run -it latituded3420/message-encryption:latest
```

### Method 3: Local Development

```bash
# Clone repository
git clone https://github.com/latituded3420/message-encryption.git
cd message-encryption

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run
message-encryption
```

### Method 4: GitHub Codespace

1. Click "Code" > "Codespaces" > "Create codespace on main"
2. Run: `pip install -e .`
3. Run: `message-encryption`

---

## CI/CD Pipeline

Our GitHub Actions workflow automatically:

1. **Publishes to PyPI** when you create a git tag (v*)
2. **Builds Docker image** for every push
3. **Runs tests** to ensure quality

---

## Environment Variables

No environment variables are required for basic deployment.

---

## Troubleshooting

### Docker Build Issues
- Ensure Docker is installed: `docker --version`
- Check Dockerfile syntax
- Verify all dependencies in requirements.txt

### PyPI Publication Issues
- Verify API token in GitHub Secrets
- Check setup.py configuration
- Ensure version is unique and doesn't already exist

---

## Security Considerations

1. Never commit secrets or API keys
2. Use GitHub Secrets for sensitive data
3. Keep dependencies updated
4. Review security advisories regularly

---

## Support

For issues and questions:
- GitHub Issues: https://github.com/latituded3420/message-encryption/issues
- Contact: latituded3420@gmail.com
