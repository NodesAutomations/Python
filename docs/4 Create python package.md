---
title: Create Package
---

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