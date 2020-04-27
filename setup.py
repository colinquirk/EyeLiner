import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="eyeliner",
    version="0.0.1",
    author="Colin Quirk",
    author_email="cquirk@uchicago.edu",
    description="Turns eyetracking data into images for CNN analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/colinquirk/eyeliner",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.5',
)