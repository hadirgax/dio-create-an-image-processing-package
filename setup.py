from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()


setup(
    name="dio_image_processing",
    version="0.0.1",
    author="Hadir Garcia",
    description="Image processing package in Python using the Skimage package",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hadirga/dio-create-an-image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.7"
)