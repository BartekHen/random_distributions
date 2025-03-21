from setuptools import setup, find_packages

setup(
    name="random_distributions",
    version="0.1",
    packages=find_packages(),
    description="Pakiet do generowania liczb o różnych rozkładach.",
    author="Twoja Nazwa",
    author_email="twoj@email.com",
    url="https://github.com/BartekHen/random_distributions",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)