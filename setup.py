from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='algoliaqb',
      version='0.0.1',
      description='Algolia Query Builder',
      long_description=readme(),
      keywords='funniest joke comedy flying circus',
      url='http://github.com/ryanb58/algoliaqb',
      author='Taylor Brazelton',
      author_email='taylor.r.brazelton@gmail.com',
      license='MIT',
      packages=['algoliaqb'],
      zip_safe=False
)