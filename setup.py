import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="iwg-samanage",
    version="0.0.1",
    author="Rodney Jan Mandap",
    author_email="rodneyjan.mandap@iwgplc.com",
    description="This is a package to easily call request to Samanage API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rodneymandap/iwg-samanage",
    packages=setuptools.find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=['requests'],
)