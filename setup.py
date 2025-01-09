from setuptools import setup, find_packages

setup(
    name="file_name_formatter",
    version=0.2,
    packages=find_packages(),
    install_requires=[],
    author="Felix Omondi",
    author_email="felixomondi590@gmail.com",
    description="A Python module for formatting file names",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Felix-svg/file_name_formatter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
