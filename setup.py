from setuptools import find_packages
from setuptools import setup


setup(name='algoliaqb',
      version='0.1',
      description='Algolia Query Builder',
      url='http://github.com/ryanb58/algoliaqb',
      author='Taylor Brazelton',
      author_email='taylor.r.brazelton@gmail.com',
      license='MIT',
      packages=['algoliaqb'],
      packages=find_packages(exclude=("tests",)),
      zip_safe=False
)