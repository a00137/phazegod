from setuptools import setup, find_packages

setup(
    name="phazegod",
    version="0.1.0",
    packages=find_packages(),
    author="Shaurya",
    author_email="your-email@example.com",  # replace or remove
    description="Command-line tool by Phazegod (Shaurya)",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/a00137/phazegod",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "phazegod = phazegod.main:main",
        ],
    },
)
