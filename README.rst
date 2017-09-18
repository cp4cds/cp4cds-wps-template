MyApp: a WPS template for CP4CDS
================================

.. image:: https://travis-ci.org/cp4cds/cp4cds-wps-template.svg?branch=master
   :target: https://travis-ci.org/cp4cds/cp4cds-wps-template
   :alt: Travis Build

MyApp is a minimal WPS to be used as a template to setup Web Processing Services (WPS)
in the CP4CDS Copernicus project.

Currently it is using the `PyWPS`_ WPS implementation.


Installation
************

The installation is done with `Buildout`_. It is using the Python distribution
system `Anaconda`_ to maintain software dependencies.

If Anaconda is not available then a minimal Anaconda will be installed during
the installation process in your home directory ``~/anaconda``.

The installation process setups a conda environment named ``myapp``. All
additional packages are going into this conda environment.
The location is ``~/.conda/envs/myapp``.

Now, check out the code from the GitHub repo as ``myapp`` and start the installation::

   $ git clone https://github.com/cp4cds/cp4cds-wps-template.git myapp
   $ cd myapp
   $ make clean install

After successful installation you need to start the services. All installed files (config etc ...)
are by default in your home directory ``~/birdhouse``. Now, start the services::

   $ make start  # starts supervisor services
   $ make status # shows supervisor status

The deployed WPS service is available on http://localhost:5000/wps?service=WPS&version=1.0.0&request=GetCapabilities.

Check the log files for errors::

   $ cd ~/birdhouse
   $ tail -f  var/log/pywps/myapp.log
   $ tail -f  var/log/supervisor/myapp.log

For other install options run ``make help`` and read the documention of the
`Makefile <http://birdhousebuilderbootstrap.readthedocs.org/en/latest/>`_.

Configuration
*************

If you want to run on a different hostname or port then change the default values in ``custom.cfg``::

   $ cd wps
   $ vim custom.cfg
   $ cat custom.cfg
   [settings]
   hostname = localhost
   http-port = 5000

After any change to your ``custom.cfg`` you **need** to run ``make update`` (offline mode) or ``make install`` again
and restart the ``supervisor`` service::

  $ make install
  $ make restart
  $ make status


  .. _Copernicus: http://climate.copernicus.eu/
  .. _PyWPS: http://pywps.org/
  .. _Buildout: http://www.buildout.org/
  .. _Anaconda: http://www.continuum.io/
