from setuptools import (setup, find_packages)

__copyright__ = 'Copyright (c) 2018 Monica Natalia Moreno'


NAME = "simple-automation-bot"

DESCRIPTION = "Framework for testing automation and support"

version = {}
with open('version.py') as fp:
    exec(fp.read(), version)

setup(
    name=NAME,
    version=version['__version__'],
    url='',
    license='',
    author="Monica Natalia Moreno",
    keywords="",
    setup_requires='',
    tests_require='',
    install_requires=['requests', 'paramiko'],
    author_email="m.nataliamoreno@gmail.com",
    description=DESCRIPTION,
    long_description='Framework for testing automation and support',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3.6',
        'Environment :: Console, IDE',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
