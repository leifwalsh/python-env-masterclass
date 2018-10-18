# Lesson 4: Editable installs

In lesson 3, we saw how to package our code and install it into a
virtualenv. In this lesson, we'll see how when we edit the code we
wrote, we still have to "reinstall" it to see its effects, and we'll
see how to install in a mode which makes this edit loop faster.

## Setup

As in previous lessons, let's create and activate a virtualenv for our
work in this lesson:

    $ python -m venv lesson-4-env
    $ source lesson-4-env/bin/activate
    
Let's install the code in this lesson into our virtualenv (it's the
same code from lesson 3):

    (lesson-4-env) $ pip install .
    Processing /home/leif/git/python-env-masterclass/lesson-4
    Collecting numpy (from lesson-4==0.1)
      Using cached https://files.pythonhosted.org/packages/98/44/94cc2e139b611b16458384ff3b9c87f217144b5915b0a9798c07a7295437/numpy-1.15.2-cp37-cp37m-manylinux1_x86_64.whl
    Installing collected packages: numpy, lesson-4
      Running setup.py install for lesson-4 ... done
    Successfully installed lesson-4-0.1 numpy-1.15.2
    
## Running our code

We can run the same script:

    (lesson-4-env) $ hypotenuse 5 12
    Base: 5.0
    Height: 12.0
    Hypotenuse: 13.0

Let's break our code! Edit `npgeometry.py` to make our function
incorrect:

    def hypotenuse(xs, ys):
        return np.sqrt(xs * xs - ys * ys)
        
If we run it, it should return a weird result, right?

    (lesson-4-env) $ hypotenuse 5 12
    Base: 5.0
    Height: 12.0
    Hypotenuse: 13.0

Hmm, it still gave us the right answer, even though we made the code
wrong. If we ask Python where it got `npgeometry` from, we can see
why:

    (lesson-4-env) $ cd /
    (lesson-4-env) $ python -c 'import npgeometry; print(npgeometry.__file__)'
    /home/leif/git/python-env-masterclass/lesson-4/lesson-4-env/lib/python3.7/site-packages/npgeometry.py
    (lesson-4-env) $ head -n6 /home/leif/git/python-env-masterclass/lesson-4/lesson-4-env/lib/python3.7/site-packages/npgeometry.py
    import argparse
    
    import numpy as np
    
    def hypotenuse(xs, ys):
        return np.sqrt(xs * xs + ys * ys)
        
When we import `npgeometry`, we're getting the version that was copied
into our virtualenv, not the one from the source location in
`lesson-4` that we installed! If we look at its contens, it still
contains the right hypotenuse code.

One way to fix this is to re-run `pip install` to copy the changed
file into our virtualenv:

    (lesson-4-env) $ pip install .
    (lesson-4-env) $ hypotenuse 5 12
    Base: 5.0
    Height: 12.0
    /home/leif/git/python-env-masterclass/lesson-4/npgeometry.py:6: RuntimeWarning: invalid value encountered in sqrt
      return np.sqrt(xs * xs - ys * ys)
    Hypotenuse: nan
    
Now, after reinstalling, we see the effect of our change: we broke our
library's logic!

But, there's a way to see how our changes effect our program without
re-running the install script every time.

## Editable installs

If we want to edit our code and quickly see the results, `pip`
provides us a different way of installing that allows this, called
"editable installs" (`-e`).

First, return `npgeometry.py` to its original state:

    def hypotenuse(xs, ys):
        return np.sqrt(xs * xs + ys * ys)

Let's recreate our environment:

    (lesson-4-env) $ deactivate
    $ rm -rf lesson-4-env
    $ python -m venv lesson-4-env
    $ source lesson-4-env/bin/activate

This time, let's make an __editable install__:

    (lesson-4-env) $ pip install -e .
    
If we run `hypotenuse` again, we get the right answer:

    (lesson-4-env) $ hypotenuse 5 12
    Base: 5.0
    Height: 12.0
    Hypotenuse: 13.0

If we break `npgeometry.py` again:

    def hypotenuse(xs, ys):
        return np.sqrt(xs * xs - ys * ys)

When we run the script now, we see that our change took effect:

    (lesson-4-env) $ hypotenuse 5 12
    Base: 5.0
    Height: 12.0
    /home/leif/git/python-env-masterclass/lesson-4/npgeometry.py:6: RuntimeWarning: invalid value encountered in sqrt
      return np.sqrt(xs * xs - ys * ys)
    Hypotenuse: nan
    
## Recap

This is not only useful for temporarily breaking our packages. When
we're working on new changes to the packages we're working on, it's a
good idea to install them with `-e` so that we can quickly re-run our
code without re-installing to see its effects.
