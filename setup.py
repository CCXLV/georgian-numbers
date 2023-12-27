from setuptools import setup
import re

version = ""
with open("georgian_numbers/__init__.py") as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError("version is not set")

packages = [
    "georgian_numbers",
    "georgian_numbers.utils"
]

setup(
    name="georgian-numbers",
    version=version,
    description="It converts numbers in Georgian Language",
    author="CCXLV",
    packages=packages,
    license="MIT"
)