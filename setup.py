#/usr/bin/python

from setuptools import setup

setup(name='pyqver',
      version="0.1",
      scripts=[
          'pyqver2',
          'pyqver3',
      ],
      author='Greg Hewgill',
      author_email='greg@hewgill.com',
      description='query required Python version of a Python script',
      long_description='This script attempts to identify the minimum version'
                       'of Python that is required to execute a particular'
                       'source file.',
      keywords='python version checking',
      license='zlib',
      url='https://github.com/ghewgill/pyqver',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: zlib/libpng License',
          'Natural Language :: English',
          'Operating System :: POSIX',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 3',
          'Topic :: Software Development',
          'Topic :: Utilities',
      ])
