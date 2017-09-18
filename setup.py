import os

from setuptools import setup, find_packages

version = __import__('myapp').__version__
here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()

reqs = [line.strip() for line in open('requirements/deploy.txt')]

classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Science/Research',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: POSIX',
    'Programming Language :: Python',
    'Topic :: Scientific/Engineering :: Atmospheric Science',
]

setup(name='myapp',
      version=version,
      description='A WPS template/example for CP4CDS',
      long_description=README + '\n\n' + CHANGES,
      classifiers=classifiers,
      #author='CP4CDS',
      #author_email='wps@dkrz.de',
      url='https://github.com/cp4cds/cp4cds-wps-template',
      license="Apache License v2.0",
      keywords='wps pywps birdhouse cp4cds copernicus',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='myapp',
      install_requires=reqs,
      entry_points={
          'console_scripts': [
             'myapp=myapp:main'
          ]
      },
      )
