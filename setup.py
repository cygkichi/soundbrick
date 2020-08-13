import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wavetile",
    version="0.0.5",
    author="cygkichi",
    author_email="",
    description="A simple sound file viewer like a brickwork",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cygkichi/soundbrick",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
