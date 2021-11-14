from setuptools import find_packages, setup

setup(
	name='ourpythonlib',
	packages=find_packages(exclude=['tests']),
	install_requires=[
		'numpy==1.21.2',
		'pandas==1.3.3',
		'scikit-learn==1.0.1'
	],
	version='0.1.0',
	description='Our first Python library',
	author='Schindler, Vicaria, Virguez',
	license='MIT',
)
