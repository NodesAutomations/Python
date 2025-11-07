# Packages

### Explore python packages
- https://anaconda.org/anaconda/repo
- https://anaconda.cloud/package-categories

### Install PIP
- use `pip --version` to check for current pip version
- use `python -m ensurepip --default-pip` to install pip
- use `python.exe -m pip install --upgrade pip` to update pip
- you can find your install python packages @`C:\Users\Ryzen2600x\AppData\Local\Programs\Python\Python311\Lib\site-packages`

### Install new Python package
- use `pip install pybrot` to install new packages, you need name of package to use this command
- Local python package Directory : `C:\Users\Ryzen2600x\AppData\Local\Programs\Python\Python311\Lib\site-packages`
- when you use any python package, you can double click on any class to explore it's code, you'll also able to see it's file location on vscode

### Uninstall python package
- use `pip uninstall pybrot` to remove any package you don't like

### Sample code to use pybrot library
- this also require numpy and matplotlib package
```python
from pybrot.Mandelbrot import Mandelbrot

m=Mandelbrot()
m.show()
```

# Steps to create local python package

### References
- [Publish your own python package](https://www.youtube.com/watch?v=tEFkHEKypLI)

### Prepare all files
- To create python package you'll need 4 things
    - solution folder : This contains all python script files related to your package
    - setup.py : file which contain package meta data
    - README : 
    - LICENSE : package license
- refer this github repo : [vidstream](https://github.com/NeuralNine/vidstream)
- Sample setup.py file

    ```python
    from setuptools import setup, find_packages
    import codecs
    import os

    here = os.path.abspath(os.path.dirname(__file__))

    with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
        long_description = "\n" + fh.read()

    VERSION = '0.0.13'
    DESCRIPTION = 'Streaming video data via networks'
    LONG_DESCRIPTION = 'A package that allows to build simple streams of video, audio and camera data.'

    # Setting up
    setup(
        name="vidstream",
        version=VERSION,
        author="NeuralNine (Florian Dedov)",
        author_email="<mail@neuralnine.com>",
        description=DESCRIPTION,
        long_description_content_type="text/markdown",
        long_description=long_description,
        packages=find_packages(),
        install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
        keywords=['python', 'video', 'stream', 'video stream', 'camera stream', 'sockets'],
        classifiers=[
            "Development Status :: 1 - Planning",
            "Intended Audience :: Developers",
            "Programming Language :: Python :: 3",
            "Operating System :: Unix",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
    )
    ```
### Create *.whl file 
- install wheel package using `pip install wheel`
- create python package using `python setup.py bdist_wheel`
- this should generate build and dist folder on your project directory
- you can find *.whl file in dist folder

### install package using *.whl file
- just use `pip install package.whl` command to install package on your local system, if package.whl is not in your current directory then you might need to specify whole path
- find this package on directory `C:\Users\Ryzen2600x\AppData\Local\Programs\Python\Python311\Lib\site-packages`
