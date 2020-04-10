import setuptools 

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

if not requirements: 
    print("The requirments file is either corrupt or not working.")

setuptools.setup(
    name = 'PiAware_Dump1090_Wrapper',
    version = '1.0',
    install_requires = requirements,
    packages = setuptools.find_packages(),

    #metadata, anything we care about check docs for more info
    author = 'Kyle Cooper',
    author_email = 'kyle@cooperkyle.com',
    description = 'A module for reading aircraft a PiAware device is sensing',
    license = 'MIT',
)