import setuptools 

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if not requirements: 
    print("The requirments file is either corrupt or not working.")

setuptools.setup(
    name = 'PiAware_Dump1090_Wrapper',#.py file name w/o extension
    version = '0.005', # Any version number you want
    install_requires = requirements,
    packages = setuptools.find_packages(),

    #metadata, anything we care about check docs for more info
    author = 'Kyle Cooper',
    author_email = 'kyle@cooperkyle.com',
    description = 'A module for sending aircraft data to a firebase Firestore',
    license = 'Public Domain',
)