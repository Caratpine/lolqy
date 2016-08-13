# -*- encoding: UTF-8 -*-

from setuptools import setup, find_packages

VERSION = '0.1.1'

setup(name='lolqy',
      version=VERSION,
      description="A terminal tools for LOL duowanBox Base on Python",
      long_description='just a toy',
      classifiers=[], #
      keywords='python lol duowan terminal',
      author='caratpine',
      author_email='bepox0531@gmail.com',
      url='https://github.com/Caratpine/lolqy',
      license='MIT',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
        'requests',
        'prettytable',
        'click',
      ],
      entry_points={
        'console_scripts':[
            'lolqy = lolqy.command:main'
        ]
      },
)