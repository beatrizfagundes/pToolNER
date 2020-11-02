from setuptools import find_packages, setup

setup(name='pToolNER',
      packages=find_packages(),
      install_requires=['nltk', 'flair', 'unidecode']
)
