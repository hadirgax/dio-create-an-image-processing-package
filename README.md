# Creating an Image Processing Package

This repository was initially intended to solve the code challenge about creating a processing
image package with Python in development of the [DIO's](https://dio.me) bootcamp "Geração Tech
Unimed-BH - Ciência de Dados".

This repository contents a simple example about how to create a package using Python's Setuptools
package and publish it in the Pypi repository.

## Description

The package image_processing is used to:
    Processing:
        - Histogram matching
        - Structural Similarity
        - Resize image
    Utils:
        - Read image
        - Save image
        - Plot image
        - Plot result
        - Plot histogram

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable) to install the image_processing
package.
```bash
pip install dio_image_processing
```

## Usage

```python
from dio_image_processing import processing, utils
```

## How to publish a package in Pypi
```bash
python setup.py sdist bdist_wheel
python -m twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```

## Author
[Hadir Garcia](https://github.com/hadirga)

## License
[MIT](https://choosealicense.com/licenses/mit/)