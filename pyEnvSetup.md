# Environment Setup

You will need to prepare your local environment to run Python. Recall from the prerequisite work that are targeting Python 3 (because Python 2 will soon be deprecated).

## Windows Machines
Download the [Python installer](https://www.python.org/ftp/python/3.7.2/python-3.7.2-webinstall.exe). Choose to 'Add Python to your path' when running the installer. *PIP*, the python package manager, is included in this install.

## MacOS Machines
MacOS comes with a system install of python but its quite dated. 
```bash
SEA-ML-00027406:~ reynolds$ python --version
Python 2.7.10
```
Before installing Python, you’ll need to install GCC. GCC can be obtained by downloading Xcode or OSX-GCC-Installer package. If installing Xcode you need to also install the command line tools.
```bash
$ xcode-select --install
```
*Homebrew* is a popular package mangager for OSX.

To install Homebrew:
```bash
$ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ export PATH="/usr/local/opt/python/libexec/bin:$PATH"
```
To install a modern version of Python:
```bash
$ brew install python
```
This will take a minute or two to build from source. Your system python will still be in your path. For these exercises make sure you run:
```bash
$ python3
```

## Installing the _requests_ library
```bash
$ pip install requests
```
Note that this package might already be installed.

## Running a Python Script
```
C:\User>python example1.py
```
or
```bash
$ python3 example1.py
```
