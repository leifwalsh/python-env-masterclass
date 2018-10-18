# Lesson 2: Installing Libraries

In this lesson, we'll see how to install a library (`numpy`), and use
it from our code.

## Creating a `virtualenv`

Before we install a library, we need to make a place to install
it. While you can install libraries directly in your system next to
the system-wide Python interpreter, it's best practice to create an
isolated environment to install them into. This helps you manage and
maintain the sets of libraries each of your projects needs,
independent of the system they're running on.

To create your first `virtualenv`, run the `venv` program in this
directory:

    python -m venv lesson-2-env
    
This creates the following structure:

    $ tree -L 2 lesson-2-env/
    lesson-2-env/
    ├── bin
    │   ├── activate
    │   ├── activate.csh
    │   ├── activate.fish
    │   ├── easy_install
    │   ├── easy_install-3.7
    │   ├── pip
    │   ├── pip3
    │   ├── pip3.7
    │   ├── python -> /usr/bin/python
    │   └── python3 -> python
    ├── include
    ├── lib
    │   └── python3.7
    ├── lib64 -> lib
    └── pyvenv.cfg

This looks like part of your root filesystem: it contains `bin/`,
`include/`, and `lib/` directories, and some other metadata.

## Activating your environment

Once you've created the environment, you need to "activate" it in your
shell. This modifies some variables (like your shell's `PATH`
variable), to make sure anything you do in that shell uses the
environment.

    $ source lesson-2-env/bin/activate

Now the Python interpreter you'll run is the one in the environment:

    (lesson-2-env) $ which python
    /home/leif/git/python-env-masterclass/lesson-2/lesson-2-env/bin/python

You can see that this adds an annotation to your prompt that shows
which environment is active. You can deactivate it by just running
`deactivate`. For the rest of the tutorial, you'll see the active
environment in paretheses before shell prompts:

    (lesson-2-env) $ deactivate
    $ which python
    /usr/bin/python
    
## Installing packages

Let's install the `numpy` (Numerical Python) package. Remember to
re-activate your environment first (you'll have to do this whenever
you start working with your project in a new terminal):

    $ source lesson-2-env/bin/activate

The package manager provided by Python is called `pip`. Mostly you'll
just run `pip install <package>`, but you can do other things with
`pip` too, try `pip --help` on your own time. We want to install
`numpy`, so we'll run this:

    (lesson-2-env) $ pip install numpy
    Collecting numpy
      Downloading https://files.pythonhosted.org/packages/98/44/94cc2e139b611b16458384ff3b9c87f217144b5915b0a9798c07a7295437/numpy-1.15.2-cp37-cp37m-manylinux1_x86_64.whl (13.8MB)
        100% |████████████████████████████████| 13.9MB 2.8MB/s 
    Installing collected packages: numpy
    Successfully installed numpy-1.15.2
    (lesson-2-env) $ python -c 'import numpy; print(numpy.__file__)'
    /home/leif/git/python-env-masterclass/lesson-2/lesson-2-env/lib/python3.7/site-packages/numpy/__init__.py
    
You can see that we can now import numpy, and it was installed inside
`lesson-2-env/lib/python3.7/site-packages`. That's where everything we
install in this environment will go, and that's good! Now we can
install some things in the env for one project and other things in the
env for another project, and keep things separate and clean.

## Using packages in our virtualenv

Now take a look at our module `npgeometry.py` and script
`script.py`. We've rewritten our `hypotenuse()` function to use
`numpy` arrays so that it can compute many hypotenuses at once:

    (lesson-2-env) $ python script.py 
    Bases: [3 5 8]
    Heights: [ 4 12 15]
    Hypotenuses: [ 5. 13. 17.]
    
You'll notice that we didn't have to do anything special to our path
in order to import `numpy`: since we have the virtualenv active, it's
already on our path (the last entry here):

    (lesson-2-env) $ python -c 'import sys; print(sys.path)'
    ['', '/usr/lib/python37.zip', '/usr/lib/python3.7', '/usr/lib/python3.7/lib-dynload', '/home/leif/git/python-env-masterclass/lesson-2/lesson-2-env/lib/python3.7/site-packages']

You'll also notice that we still didn't need to do anything special
for `script.py` to find `npgeometry.py`, the script's directory is
still on the path Python will search. That's okay for now, but in the
next lesson we'll show how to also install your own modules into the
virtualenv for safety.

If you deactivate your env and try running `script.py`, it might fail
because it can't find `numpy` (or it might succeed if you happen to
have `numpy` installed system-wide, but let's ignore that for now).

    (lesson-2-env) $ deactivate
    $ python script.py
    Traceback (most recent call last):
      File "script.py", line 1, in <module>
        import numpy as np
    ModuleNotFoundError: No module named 'numpy'

## Appendix

When you search the internet for "Python virtualenvs", you'll find a
lot of tools that will help you manage them, like `mkvirtualenv`,
`pyvenv`, `conda`, `pipenv`, `poetry`, etc. They're all built around
the same fundamental ideas as the `venv` tool (`pyvenv` actually used
to be an independent project, but it was imported into Python in
version 3.4 as the `venv` module we used above), but some add extra
functionalities or helpers.

For portability, in this class we're just going to use `venv`, but you
should be able to take the information in this class and apply it to
those other tools if you want to use them.

For completeness, here's a quick overview (quite heavy with my
opinions), but don't feel compelled to read this before proceeding
with the next lesson:

* `mkvirtualenv`: Shell script wrappers around the `virtualenv` tool
  that help you manage multiple environments, list the ones you've
  created, associate them with project directories, etc.
* `pyvenv`: An old third-party project that was imported into the
  Python main distribution as `venv`.
* `conda`: A big tool that helps you create environments and also has
  its own package format, kind of a combination of `venv` and `pip` in
  that you can `conda create -n environment-name` and also `conda
  install numpy`. `conda` used to have better support than `pip` for
  "binary packages", which basically means packages that contain
  compiled extension modules (which basically means "fast"), but `pip`
  has gotten better at packaging extension modules since then and you
  don't necessarily need `conda` these days.
* `pipenv`: A tool built on top of `venv` that helps library
  maintainers manage their dependencies. I quite like it, but it's
  more than you need for basic virtualenv usage, and it's not ported
  to Windows so I can't use it in this class. If you are packaging a
  library for lots of people to consume, I do recommend trying it, and
  you can ask me after the class if you want more information.
* `poetry`: Another `pipenv`-like thing which uses different syntax
  (toml), and is somewhat inspired by Rust's `cargo`. I don't
  particularly think the world needs another `pipenv` with different
  syntax, but it exists and you should know about it. The author has
  submitted a PEP to standardize its package format, if that gets
  accepted and replaces `pipenv`, you probably want to be aware.
