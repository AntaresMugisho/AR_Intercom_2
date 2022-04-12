# -*- coding:utf-8 -*-

# ======================================= BUILD THE WINDOWS .EXE FILE ==================================================
import sys, os

#  MAC OS SETUP
if sys.platform == "darwin":
    from setuptools import setup
    """
    This is an adaptation from a setup.py script generated by py2applet
    Usage:
        python setup.py py2app
    """

    APP = ['ArIntercom.py']
    DATA_FILES = ['resources/Arlogo.icns']
    OPTIONS = {
        'iconfile': 'resources/Arlogo.icns',
        'argv_emulation': True,
        'packages': ['sounddevice']
    }

    setup(
        app=APP,
        data_files=DATA_FILES,
        options={'py2app': OPTIONS},
        setup_requires=['py2app'],
    )

# WINDOWS AND LINUX SETUP
else:
    from cx_Freeze import setup, Executable

    # PREPARING OPTIONS

    # Modules path
    path = sys.path

    # Icon path
    icone = "resources\ARsoftlogo.ico"

    # To able translations
    includefiles = []
    includefiles += [(r"C:\Users\Antares\AppData\Roaming\Python\Python39\site-packages\PyQt5\Qt\translations",
                      "translations")]
    includefiles += [(r"D:\Coding\Python\Reseau\AR_Intercom_v2\resources", "resources")]

    # Options dictionnary
    options = {"path": path,
               "include_files": includefiles,
               "compressed": False}

    # Include dll on windows
    if sys.platform == "win32":
        options["include_msvcr"] = True

    setup(name="AR Intercom",
          version="2.0",
          description="AR Intercom",
          author="Antares",
          executables=[Executable(script="ArIntercom.py", base="Win32GUI", icon=icone)]
          )
# ===================================================== END ============================================================