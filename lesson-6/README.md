# Lesson 6: Freezing and thawing

In Lesson 3, we learned how to declare the dependencies for a piece of
software you've written, so that you can reinstall it, or give it to a
friend. Recall that you declare your package's _requirements_ in
`setup.py`:

    install_requires=['numpy']

But sometimes you install things that aren't strictly needed for your
library to work, and you just want to save what you've got in order to
get it back later.

Or, sometimes you want to write down _exactly_ what you had installed
at a certain time, though it might not be "semantically" what your
software requires. That is, maybe in theory your software could use
any version of numpy, but for reproducibility's sake, you want to run
with numpy 1.13.3 because that's what you used last time you ran it
(this is common in data science and research workflows).

## Freezing

`pip` remembers everything it's installed for us, and can repeat it
back to us:

    (lesson-5-env) $ pip freeze
    backcall==0.1.0
    bleach==3.0.2
    decorator==4.3.0
    ...
    wcwidth==0.1.7
    webencodings==0.5.1
    widgetsnbextension==3.4.2
    
If we save this to a file (it's commonly named `requirements.txt`)...

    (lesson-5-env) $ pip freeze > requirements.txt
    
Then we can save that and use it to re-create that environment on a
different computer, or just restore what we had later on.

## Thawing

Let's deactivate and destroy `lesson-5-env`. Maybe the hard drive it
was on got corrupted or something.

    (lesson-5-env) $ deactivate
    $ rm -rf lesson-5-env
    $ cd ../lesson-6
    
Now, we still have `requirements.txt`, so let's restore it! First,
create a fresh virtualenv:

    $ python -m venv lesson-6-env
    $ source lesson-6-env/bin/activate

(Since the `lesson-4` package isn't available in a package index, it's
just on our filesystem, we have to install it first; if you've only
installed things from known locations like PyPI or GitHub, you can
ignore this:)

    (lesson-6-env) $ pip install -e ../lesson-4
    ...
    
Now, install from the `requirements.txt` file:

    (lesson-6-env) $ pip install -r ../lesson-5/requirements.txt
    Collecting backcall==0.1.0 (from -r ../lesson-5/requirements.txt (line 1))
      Using cached https://files.pythonhosted.org/packages/84/71/c8ca4f5bb1e08401b916c68003acf0a0655df935d74d93bf3f3364b310e0/backcall-0.1.0.tar.gz
    Collecting bleach==3.0.2 (from -r ../lesson-5/requirements.txt (line 2))
      Using cached https://files.pythonhosted.org/packages/d4/0d/4696373c3b714f6022d668fbab619690a42050dbeacede6d10ed97fbd3e2/bleach-3.0.2-py2.py3-none-any.whl
    ...
    Successfully installed Jinja2-2.10 MarkupSafe-1.0 Pygments-2.2.0 Send2Trash-1.5.0 backcall-0.1.0 bleach-3.0.2 decorator-4.3.0 defusedxml-0.5.0 entrypoints-0.2.3 ipykernel-5.1.0 ipython-7.0.1 ipython-genutils-0.2.0 ipywidgets-7.4.2 jedi-0.13.1 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.2.3 jupyter-console-6.0.0 jupyter-core-4.4.0 mistune-0.8.4 nbconvert-5.4.0 nbformat-4.4.0 notebook-5.7.0 pandocfilters-1.4.2 parso-0.3.1 pexpect-4.6.0 pickleshare-0.7.5 prometheus-client-0.4.2 prompt-toolkit-2.0.6 ptyprocess-0.6.0 python-dateutil-2.7.3 pyzmq-17.1.2 qtconsole-4.4.2 simplegeneric-0.8.1 six-1.11.0 terminado-0.8.1 testpath-0.4.2 tornado-5.1.1 traitlets-4.3.2 wcwidth-0.1.7 webencodings-0.5.1 widgetsnbextension-3.4.2

We've successfully gotten back everything we had before! Crisis
averted.

## Recap

1. You can use `pip freeze` at any time to save the current set of
   packages you have installed. Save this to a file usually called
   `requirements.txt`.
2. You can install everything from such a requirements file with `pip
   install -r`.

This is often used to save an environment to reproduce research
results later, or to copy an environment to another machine.

### Footnote

Often you will see software libraries provide a `requirements.txt`
file in addition to requirements specified in `setup.py`.

Usually the ones in `setup.py` mean "I truly require these packages
with these version restrictions, for some fundamental reason", and the
ones in `requirements.txt` mean "this is what I used last time I
updated this, so if you want to do development on this package and
make sure you're running the tests and things in exactly the same way,
use these versions". There's no official standard, it's just common
practice.
