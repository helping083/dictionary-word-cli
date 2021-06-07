from setuptools import setup

setup(
    name='Dictionary-word',
    version='1.0.0',
    description='Simple dictionary cli',
    long_description='A cli tool that helps searching and saving words in a json format',
    url='https://github.com/helping083/dictionary-word-cli',
    author='helping083',
    author_email='helping083@gmal.com',
    license='The Unlicense',
    packages=['dictionary-word-cli'],
    zip_safe=False,
    install_requires=['requests']
)