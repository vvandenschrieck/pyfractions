import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyfractions",
    version="0.0.1",
    author="Virginie Van den Schrieck",
    author_email="v.vandenschrieck@ephec.be",
    description="A small example package to manipulate pyfractions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vvandenschrieck/pyfractions.git",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)