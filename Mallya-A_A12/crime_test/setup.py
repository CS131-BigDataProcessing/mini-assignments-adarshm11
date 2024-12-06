#setup.py

from setuptools import setup, find_packages

setup(
	name='crime_test',
	version='1.0.0',
	package=find_packages(),
	install_requires=[
		'pandas',
		'numpy',
	],
	description='A package to validate columns of the crime dataset',
	long_description=open('README.md').read(),
	long_description_content_type='text/markdown',
	author='Adarsh Mallya',
	author_email='adarsh.mallya@sjsu.edu',
	url='https://github.com/CS131-BigDataProcessing/mini-assignments-adarshm11,
	python_requires='>=3.6',
)
