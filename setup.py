import setuptools 

with open('README.md') as readme_f: 
    README = readme_f.read()

with open('HISTORY.md') as history_f: 
    HISTORY = history_f.read()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name = 'PiAware_Dump1090_Wrapper',
    version = '1.0.0',
    install_requires = requirements,
    packages = setuptools.find_packages(),
    long_description_content_type = "text/markdown",
    long_description = f'{README} \n\n {HISTORY}',
    author = 'Kyle Cooper',
    url = 'https://github.com/kc8/piawaredump1090wrapper',
    author_email = 'kyle@cooperkyle.com',
    description = 'A module for reading aircraft a PiAware device is sensing',
    license = 'MIT',
)
