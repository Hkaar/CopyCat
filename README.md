# CopyCat
_version 0.011_ | **Made by Hkaar**

A simple cli utility to backup your files

## Features
- Fully backup any folders you want to a source directory
- Control/Filter on what you backup based on size & name
- Support for auto archive files with 7z

## How to use
### Setup

Clone the repository to your machine :

```
git clone https://github.com/Hkaar/CopyCat.git
```

Install the required packages :

```
pip install -r requirements.txt
```

You can configure the tool like this :

```
python main.py config <key> <value>
```

Or just edit the <mark>config.json</mark> file

And then your all set for using copycat

### User Guide

How to copy files :

```
python main.py copy [options] <source> <destination>
```

How to configure CopyCat :

```
python main.py config <key> <value>
```
