# Lesson 5: Using packages in Jupyter

In this lesson, we'll practice using external packages and our own
libraries in a Jupyter notebook.

## Setup

As in previous lessons, let's create and activate a virtualenv for our
work in this lesson:

    $ python -m venv lesson-5-env
    $ source lesson-5-env/bin/activate
    
Since we want to use Jupyter, let's install it:

    (lesson-5-env) $ pip install jupyter
    Collecting jupyter
      Downloading https://files.pythonhosted.org/packages/83/df/0f5dd132200728a86190397e1ea87cd76244e42d39ec5e88efd25b2abd7e/jupyter-1.0.0-py2.py3-none-any.whl
    <...>
    Installing collected packages: six, wcwidth, prompt-toolkit, pygments, simplegeneric, backcall, pickleshare, decorator, ipython-genutils, traitlets, ptyprocess, pexpect, parso, jedi, ipython, tornado, jupyter-core, pyzmq, python-dateutil, jupyter-client, ipykernel, jupyter-console, webencodings, bleach, pandocfilters, testpath, defusedxml, entrypoints, jsonschema, nbformat, MarkupSafe, jinja2, mistune, nbconvert, qtconsole, prometheus-client, terminado, Send2Trash, notebook, widgetsnbextension, ipywidgets, jupyter
      Running setup.py install for simplegeneric ... done
      Running setup.py install for backcall ... done
      Running setup.py install for tornado ... done
      Running setup.py install for pandocfilters ... done
      Running setup.py install for MarkupSafe ... done
      Running setup.py install for prometheus-client ... done
    Successfully installed MarkupSafe-1.0 Send2Trash-1.5.0 backcall-0.1.0 bleach-3.0.2 decorator-4.3.0 defusedxml-0.5.0 entrypoints-0.2.3 ipykernel-5.1.0 ipython-7.0.1 ipython-genutils-0.2.0 ipywidgets-7.4.2 jedi-0.13.1 jinja2-2.10 jsonschema-2.6.0 jupyter-1.0.0 jupyter-client-5.2.3 jupyter-console-6.0.0 jupyter-core-4.4.0 mistune-0.8.4 nbconvert-5.4.0 nbformat-4.4.0 notebook-5.7.0 pandocfilters-1.4.2 parso-0.3.1 pexpect-4.6.0 pickleshare-0.7.5 prometheus-client-0.4.2 prompt-toolkit-2.0.6 ptyprocess-0.6.0 pygments-2.2.0 python-dateutil-2.7.3 pyzmq-17.1.2 qtconsole-4.4.2 simplegeneric-0.8.1 six-1.11.0 terminado-0.8.1 testpath-0.4.2 tornado-5.1.1 traitlets-4.3.2 wcwidth-0.1.7 webencodings-0.5.1 widgetsnbextension-3.4.2
    
Since we also want to use the module we've developed, let's install
that too. Since we just broke the one in lesson-4 on purpose, let's
use the one from lesson-4. We'll do an editable install:

    (lesson-5-env) $ pip install -e ../lesson-4
    Processing /home/leif/git/python-env-masterclass/lesson-4
    Collecting numpy (from lesson-4==0.1)
      Using cached https://files.pythonhosted.org/packages/98/44/94cc2e139b611b16458384ff3b9c87f217144b5915b0a9798c07a7295437/numpy-1.15.2-cp37-cp37m-manylinux1_x86_64.whl
    Installing collected packages: numpy, lesson-4
      Running setup.py install for lesson-4 ... done
    Successfully installed lesson-4-0.1 numpy-1.15.2

## Usage

Now we've got both Jupyter and our package from the previous lesson
installed. Let's give it a try!

    (lesson-5-env) $ jupyter notebook .
    [I 20:54:11.563 NotebookApp] Serving notebooks from local directory: /home/leif/git/python-env-masterclass/lesson-5
    [I 20:54:11.563 NotebookApp] The Jupyter Notebook is running at:
    [I 20:54:11.564 NotebookApp] http://localhost:8888/?token=<elided>
    [I 20:54:11.564 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).

Open up `notebook.ipynb` and run its cells. You'll see that since we
started our notebook inside our virtualenv, we can import `npgeometry`
and call its functions.

### Effects of code changes in the notebook

Go back to `npgeometry.py` in Lesson 4 and edit the `hypotenuse`
function again. Make it do something crazy.

Then go back to your notebook and try using it again. It doesn't seem
like we changed anything! Re-run the `import npgeometry` cell and try
again.

Still nothing. A module is only loaded once per Python process, and
every time we ask for it again, Python says "I've already loaded that,
here it is" and doesn't look for changes. (This is a good
optimization, most of the time.)

There are two things you can do about this:

1. You can restart your kernel (the kernel is the Python process
   running your code): this will reset you to a clean interpreter with
   *no* state (including variables you've created), so imports will
   see changed code again.
2. You can use `importlib.reload()`. Try that now:

       import importlib
       importlib.reload(npgeometry)
       
   You have to remember to run this after you make changes, but it
   works great<sup>1</sup>.
3. You can use the [autoreload
   extension](https://ipython.org/ipython-doc/3/config/extensions/autoreload.html)
   to automatically do what `importlib.reload()` does before executing
   each cell. This is usually easier than `importlib.reload()`, but
   because it's ✨magic✨, sometimes it fails in strange ways.
   
<sup>1</sup> Note that only the module and the functions it defines
get reloaded, if you use `from module import function` syntax, or
construct objects that have behavior defined in the module, those
objects won't be recreated, so you might still have surprising
behavior. When in doubt, just restart your kernel.

## Recap

For Jupyter notebooks, that's about all there is! If you work inside a
virtualenv, you can use the same modules from your notebook that you
can use inside your scripts.

There are some Jupyter extensions that let you select environments as
"kernels" if you are using Conda to manage your virtualenvs; all this
means is that the process running the code in your notebook uses the
virtualenv kernel you've selected. If you understand how things get
installed into virtualenvs, you can use these "Conda kernels" the same
as other kernels and know what to expect.
