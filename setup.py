# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')


setup(
	name='jwt_frappe',
	version="1.0.2",
	description='auth with token for mobile and frontend applications ',
	author='ahmadragheb',
	author_email='Ahmedragheb75@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
