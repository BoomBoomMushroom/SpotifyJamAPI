from setuptools import setup, find_packages

with open("README.md", "r") as f:
    longDescription = f.read()

setup(
    name='spotify-jam',
    description='spotify-jam is a package that allows you to manage Spotify Jams',
    long_description=longDescription,
    long_description_content_type="text/markdown",
    version='0.2',
    packages=find_packages(),
    install_requirements=[
        'requests==2.32.4'
    ],
)