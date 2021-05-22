import setuptools

setuptools.setup(
	name="sts_utility",
	version="0.0.1",
	author="636",
	author_email="win.stitch.23@gmail.com",
	description="636 Utility Package",
	url="https://github.com/0187773933/sts-utility",
	packages=setuptools.find_packages(),
	classifiers=[
		"Programming Language :: Python :: 3",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	python_requires='>=3.6',
)

install_requires = [
	'json',
	'pathlib',
	'time',
	'pint',
]