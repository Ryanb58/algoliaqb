import os

from setuptools import setup

readme_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'README.md')
try:
    from m2r import parse_from_file
    readme = parse_from_file(readme_file)
except ImportError:
    # m2r may not be installed in user environment
    with open(readme_file) as f:
        readme = f.read()


setup(name='algoliaqb',
      version='0.0.9',
      description='Algolia Query Builder',
      long_description=readme,
      keywords='search algolia query builder',
      url='http://github.com/ryanb58/algoliaqb',
      author='Taylor Brazelton',
      author_email='taylor.r.brazelton@gmail.com',
      license='MIT',
      packages=['algoliaqb'],
      zip_safe=False
)