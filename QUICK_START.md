# Quick Start Guide

## 🚀 Getting Started in 2 Minutes

### Option 1: Install from PyPI (Easiest)

```bash
# Install the package
pip install message-encryption

# Run the application
message-encryption
```

### Option 2: Docker (No Installation Required)

```bash
# Pull and run Docker container
docker run -it latituded3420/message-encryption:latest
```

### Option 3: Clone and Run Locally

```bash
# Clone the repository
git clone https://github.com/latituded3420/message-encryption.git
cd message-encryption

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install in development mode
pip install -e .

# Run the application
message-encryption
```

---

## 📝 Using the Application

Once running, you'll see the main menu:

```
========================================
SECRET CODE GENERATOR
========================================
1. Encode a message
2. Decode a message
3. Exit
----------------------------------------
Enter your choice (1-3):
```

### Encode a Message

1. Choose option `1`
2. Enter your message: `Hello World`
3. Enter shift number (0-25): `3`
4. Result: `Khoor Zruog`

### Decode a Message

1. Choose option `2`
2. Enter the coded message: `Khoor Zruog`
3. Enter shift number (0-25): `3`
4. Result: `Hello World`

---

## 🌍 Deploy Globally

For comprehensive deployment instructions across multiple platforms, see [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)

**Quick deployment options:**

- **PyPI**: `pip install message-encryption`
- **Docker Hub**: `docker pull latituded3420/message-encryption`
- **Cloud**: Render.com, Heroku, AWS (see DEPLOYMENT_GUIDE.md)

---

## 🛠️ Development

To contribute or modify the code:

```bash
# Clone repository
git clone https://github.com/latituded3420/message-encryption.git

# Install dependencies
pip install -e .

# Make your changes to message_encryption.py

# Test your changes
message-encryption
```

---

## 📦 Package Information

- **Version**: 1.0.0
- **Author**: Salim Shaikh
- **License**: MIT
- **Python**: 3.7+

---

## 🆘 Troubleshooting

### Command not found
```bash
# Make sure pip install was successful
pip install message-encryption --upgrade
```

### Docker permission denied
```bash
# Add user to docker group
sudo usermod -aG docker $USER
```

### Import errors
```bash
# Reinstall package
pip uninstall message-encryption -y
pip install message-encryption
```

---

## 📚 Learn More

- [Full Deployment Guide](DEPLOYMENT_GUIDE.md)
- [GitHub Repository](https://github.com/latituded3420/message-encryption)
- [PyPI Package](https://pypi.org/project/message-encryption/)

---

## 💡 Next Steps

1. Try encoding and decoding messages
2. Deploy to your preferred platform
3. Integrate into your projects
4. Share your feedback

Happy encrypting! 🔐
