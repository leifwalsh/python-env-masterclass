# Lesson 1: Scripts and Modules

Python scripts are short programs you can execute.

## Simple scripts

There's one in this directory, `simple_script.py`. Open it up in your
editor, look at what it's doing, and then try running in on the
command line.

Make sure you're in this directory (`lesson-1`), and then run:

    $ python simple_script.py
    Base: 5
    Height: 12
    Hypotenuse: 13.0
    
## Modules

You can also have modules, which are Python source files that just
define classes and functions that other Python scripts and modules can
use. There's one of those here too, `geometry.py`. Take a look at
that, and also look at a script that uses it, `importing_script.py`.

Notice how `importing_script.py` has a line `import geometry`: this
loads the file `geometry.py` and uses the function in it by calling
`geometry.hypotenuse()` later on.

Run that now:

    $ python importing_script.py
    Base: 8
    Height: 15
    Hypotenuse: 17.0

In Python, it's best to organize your code in scripts that you run
when you need to do something, and modules that you import in other
scripts or modules, when you need to share functionality that they
provide.

## Finding modules

When you write `import geometry` in a Python script or another module,
what happens? Python will try to find a script named `geometry.py`
(or, if you ran `import hyperbole`, it would look for `hyperbole.py`),
but where is it looking?

Python has a notion of a "path", or a sequence of directories it will
search when it wants to find a module to import.

You can see what Python will search by default, by looking at the list
`sys.path`. On my machine, this looks like this:

    $ python what_is_my_path.py
    ['/home/leif/git/python-env-masterclass/lesson-1', '/usr/lib/python37.zip', '/usr/lib/python3.7', '/usr/lib/python3.7/lib-dynload', '/home/leif/.local/lib/python3.7/site-packages', '/usr/lib/python3.7/site-packages']
    
You can see that Python will first look in the current directory (the
first entry in the list), then a sequence of system paths provided by
your Python installation.

When `importing_script.py` ran `import geometry`, it found
`geometry.py` in the current directory. When Python loaded
`geometry.py` and that ran `import math`, it found `math.py` in one of
the system directories.

### Controlling Python's path

There are a few ways to make your modules available to Python, and
we'll explore a few of them in this class. There are tradeoffs to be
made between the simplicity of how you tell Python where your modules
are, and how easy it is to share your modules with other people.

When you run a script with Python, the directory containing that
script is put on the path by default. That's why when you ran
`importing_script.py`, it was able to find `geometry.py` in the same
directory.

The script `importing_script_from_path.py` names a module that's not
in the current directory, so it fails if we just run it by itself:

    $ python importing_script_from_path.py
    Traceback (most recent call last):
      File "importing_script_from_path.py", line 1, in <module>
        import euclid
    ModuleNotFoundError: No module named 'euclid'

There are two easy ways to add directories to Python's search path:
you can set the environment variable `PYTHONPATH` before starting the
interpreter, or you can append to `sys.path` inside your script. Let's
see how each of these work.

    $ PYTHONPATH=lib python importing_script_from_path.py
    Origin: (0, 0)
    Target: (3, 4)
    Distance: 5.0
    
Here, we told python that it can look inside `./lib` for modules, and
then `import euclid` found `lib/euclid.py`.

In `importing_script_after_changing_path.py`, we append `lib` to
`sys.path` before trying to run `import euclid`. Open it and read how
it does this before running the code:

    $ python importing_script_after_changing_path.py 
    Origin: (0, 0)
    Target: (3, 4)
    Distance: 5.0
    
However, these are not the best ways to share libraries with others,
whether they're your coworkers, or yourself in the future, or just
yourself on another machine. In the next lesson, we'll see how to
consume a library someone else wrote, and in the subsequent lessons,
we'll learn how to publish a library so someone else can use it just
as easily.
