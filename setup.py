from setuptools import setup

setup(
	name='GoodR',
	version='1.0',
	py_module=['goodr'],
	install_requires=[
		'Click',
		'requests',
		'BeautifulSoup4',
			],
	entry_points='''
		[console_scripts]
		goodr=goodr:cli
		''',
)
