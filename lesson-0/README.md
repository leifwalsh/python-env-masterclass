# Lesson 0: Installation

To begin, you should have a working Python interpreter installed, with
the `pip` package manager.

## Checking

Try running the following command:

    python -c 'print(3 + 4)'
    
It should print `7`.

Next, check that you have `pip`:

    pip search tenacity
    
If either of these errors, try again by specifying a version:

    python3 -c 'print (3 + 4)'
    pip3 search tenacity
    
Some distributions name their programs this way. If these work for
you, use them throughout this class.

If you still don't have a working setup, follow the instructions
below.

## Installing

### Windows

Install [Python
3.7](https://www.python.org/ftp/python/3.7.0/python-3.7.0.exe).

### Mac OS X

Install [Python
3.7](https://www.python.org/ftp/python/3.7.0/python-3.7.0-macosx10.9.pkg),
or use [homebrew](https://docs.brew.sh/Homebrew-and-Python) (`brew
install python`).

### Linux

Install the latest Python your package manager provides, and `pip`,
the Python package manager. In most cases, this is already installed,
but check that you can run Python as below, if not, try one of the
below commands.

#### Ubuntu and Debian

`sudo apt-get install python3 python3-pip`

#### Arch Linux

`sudo pacman -S python python-pip`

#### Fedora

`sudo dnf install python37`

#### CentOS

`sudo yum install -y python36u python36u-libs python36u-devel
python36u-pip`
