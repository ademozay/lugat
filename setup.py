import re
from setuptools import setup


version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('lugat/__version__.py').read(),
    re.M
).group(1)


with open("README.rst", "rb") as f:
    long_descr = f.read().decode("utf-8")


setup(
    name="lugat",
    packages=["lugat"],
    entry_points={
        "console_scripts": ['lugat = lugat.__main__:main']
    },
    version=version,
    description="TDK Güncel Türkçe Sözlük için komut satırı uygulaması.",
    long_description=long_descr,
    long_description_content_type="text/x-rst",
    keywords="tdk,cli",
    author="Adem Özay",
    author_email="ozayadem@gmail.com",
    url="https://github.com/ademozay/lugat",
    install_requires=['termcolor'],
    python_requries='>=3.7'
)
