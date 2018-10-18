# Lesson 3: Packaging a Library

In this lesson, we'll write a library we can install with `pip` just
like we installed `numpy`.

## Setup

Let's create and activate an environment for this lesson:

    $ python -m venv lesson-3-env
    $ source lesson-3-env/bin/activate

## Package declaration

In Python, we declare what our package contains and what it depends on
in a file called `setup.py`. Take a look at the `setup.py` for this
lesson now:

    from setuptools import setup
    
    setup(
        name='lesson-3',
        version='0.1',
        py_modules=['npgeometry'],
        install_requires=['numpy'],
        entry_points={
            'console_scripts': [
                'hypotenuse = npgeometry:hypotenuse_main',
            ]
        }
    )

This file describes what our package is called (`name` and `version`),
what modules our package provides (`py_modules`), what other packages
it needs to work right (`install_requires`), and also declares that it
will create a script named `hypotenuse` we can run from the command
line after installing (this names a module, `npgeometry`, and a "main
function" inside that module, `hypotenuse_main`, which runs when we
run the named script `hypotenuse`).

## Installing our package

You can install a package right from your filesystem with `pip`, as
long as it contains the special file `setup.py`:

    (lesson-3-env) $ pip install .
    Processing /home/leif/git/python-env-masterclass/lesson-3
    Collecting numpy (from lesson-3==0.1)
      Using cached https://files.pythonhosted.org/packages/98/44/94cc2e139b611b16458384ff3b9c87f217144b5915b0a9798c07a7295437/numpy-1.15.2-cp37-cp37m-manylinux1_x86_64.whl
    Installing collected packages: numpy, lesson-3
      Running setup.py install for lesson-3 ... done
    Successfully installed lesson-3-0.1 numpy-1.15.2

You can see that it also saw it needed `numpy`, and installed that as
well. That's great, because now when we give our package to someone
else, they can install it and get all of its dependencies
automatically. We don't need to remember to tell our colleague what
our package needs, we've already told `pip` that in `setup.py`.

## Using our package

We can go anywhere on our filesystem and run `python` (as long as we
have our virtualenv active) and import `npgeometry` and it will be the
installed copy in our virtualenv:

    (lesson-3-env) $ cd ~
    (lesson-3-env) $ python -c 'import npgeometry; print(npgeometry.__file__)'
    /home/leif/git/python-env-masterclass/lesson-3/lesson-3-env/lib/python3.7/site-packages/npgeometry.py

We can also run the `hypotenuse` script:

    (lesson-3-env) $ hypotenuse 5 12
    Base: 5.0
    Height: 12.0
    Hypotenuse: 13.0

## Recap

All we need for a redistributable Python package is a set of code, and
a `setup.py` script that declares:

1. What our package provides
1. What our package needs

We can then go anywhere, on any machine with Python installed, create
a virtualenv, and install our package into it, and it will work just
as we've declared it. Yay!

## More `setup.py`

There's a lot more you can do with `setup.py`, you can build native
extensions, publish "packages" (as opposed to just modules), declare
other kinds of entry points, write more metadata about what our
package does and how it runs, declare supported version ranges of the
packages we depend on, and so forth. You should read the [`setuptools`
documentation](https://setuptools.readthedocs.io/en/latest/setuptools.html)
to learn more.
