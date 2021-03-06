#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  setup.py
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the project nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#

import os
import sys

base_directory = os.path.dirname(__file__)
lib_directory = os.path.join(base_directory, 'lib')
if os.path.isdir(os.path.join(lib_directory, 'protocon')):
	sys.path.insert(0, lib_directory)

from protocon import __version__

try:
	from setuptools import setup, find_packages
except ImportError:
	print('Protocon needs setuptools in order to build. Install it using')
	print('your package manager (usually python-setuptools) or via pip (pip')
	print('install setuptools).')
	sys.exit(1)

try:
	import pypandoc
	long_description = pypandoc.convert(os.path.join(base_directory, 'README.md'), 'rst')
except (ImportError, OSError):
	long_description = None

DESCRIPTION = """\
Protocon is a socket-centric framework for rapidly prototyping connections \
through simple send and receive transcripts.\
"""

with open(os.path.join(base_directory, 'requirements.txt'), 'r') as file_h:
	requirements = file_h.readlines()
requirements = [line.strip() for line in requirements]

setup(
	name='protocon',
	version=__version__,
	author='Spencer McIntyre',
	author_email='zeroSteiner@gmail.com',
	maintainer='Spencer McIntyre',
	description=DESCRIPTION,
	long_description=long_description,
	url='https://github.com/zeroSteiner/protocon',
	license='BSD',
	install_requires=requirements,
	package_dir={'': 'lib'},
	packages=find_packages('lib'),
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Environment :: Console',
		'Intended Audience :: Developers',
		'Intended Audience :: Information Technology',
		'Intended Audience :: System Administrators',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
		'Topic :: Security',
		'Topic :: Software Development :: Libraries :: Python Modules'
	],
	scripts=['protocon']
)
