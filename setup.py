from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name='pyfrac',
    version='0.0.1',
    description='A python package to work with fractions',
    py_modules=['pyfrac'],
    package_dir = {'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    extras_require = {
        "dev": [
            "pytest>=3.7",
        ],
    },
    url="https://github.com/EeshaanJain/pyfrac",
    author="Eeshaan Jain",
    author_email="jaineeshaan17@gmail.com",
)