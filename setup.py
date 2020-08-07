from setuptools import setup, Extension

ax25_module = Extension('ax25', libraries = ['ax25', 'ax25io'], sources = ['pythonax25module.c'])

setup(
	name = 'AX25',
	version = '1.0',
	ext_modules = [ ax25_module ],

	# Metadata
	author = 'Josef Matondang',
	author_email = 'admin@josefmtd.com',
	description = 'Simple python extension to create packet socket and datagram socket for AX.25',
	url = 'http://github.com/josefmtd/ax25',
)
