from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="message-encryption",
    version="1.0.0",
    author="Salim Shaikh",
    author_email="latituded3420@gmail.com",
    description="A Python application implementing Caesar cipher encryption for secure message encoding and decoding",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/latituded3420/message-encryption",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "message-encryption=message_encryption:main_menu",
        ],
    },
)
