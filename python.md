# Installing Python

For the course, you'll need a the ability to run `python` from the command line and have a couple standard libraries installed (`numpy`, `scipy` and `matplotlib`). You should be running Python 3. To check if you have Python installed and which version, run
```
python --version
```
from the command line. It should print something like:
```
Python 3.9.2
```
if it's properly installed.

## Easy install through Anaconda

The easiest way to install Python and standard scientific libraries on Mac or Windows is through Anaconda. Go here [www.anaconda.com/products/individual](https://www.anaconda.com/products/individual) and follow instructions to download and install.

## More future-proof install on Mac

Anaconda is convenient, but I prefer having more control over dependencies that are installed. For a quick install on an Intel Mac, the following should hopefully work for you:

Install [Homebrew](https://brew.sh/)

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

Install Python with Homebrew

```
brew install gcc
brew install python
brew install zmq
```

Install pip package manager

```
sudo easy_install pip
```

Install Python packages

```
pip install numpy
pip install scipy
pip install matplotlib
```

----------------------------

On M1 Macs, you'll need to do the following instead:

Install Python with Homebrew

```
brew install gcc
brew install python
brew install zmq
brew install cython
brew install numpy
brew install scipy

brew link python@3.9
ln -s -f /opt/homebrew/opt/python/bin/python3 /opt/homebrew/opt/python/bin/python
```

Install pip package manager

```
ln -s -f /opt/homebrew/opt/python/bin/pip3 /opt/homebrew/opt/python/bin/pip
```

Install Python packages

```
pip install matplotlib
```

----------------------------

# MyBinder

It's probably best to have a local install of Python on your computer, but if it's being difficult, you can always use MyBinder for the course exercises.

To do so, click on:

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/trvrb/sismid/HEAD)

It will take a little while to launch, but you'll get a working Jupyter Notebook interface and you'll be able to navigate through the repo contents to find `.ipynb` files to run within your browser.
