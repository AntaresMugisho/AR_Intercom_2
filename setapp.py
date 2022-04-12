"""
This is a setup.py script generated by py2applet
Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['main.py']
DATA_FILES = ['resources/Arlogo.icns']
OPTIONS = {
    'iconfile': 'resources/Arlogo.icns',
    'argv_emulation': True,
    'packages':['sounddevice']
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
