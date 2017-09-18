import pytest
from pywps import Service
from pywps.tests import assert_response_success

from .common import client_for, CFG_FILE
from myapp.processes.plotter import SimplePlot


@pytest.mark.online
def test_wps_simple_plot():
    client = client_for(Service(processes=[SimplePlot()], cfgfiles=CFG_FILE))
    url = "https://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/ncep.reanalysis/surface/air.sig995.2012.nc"
    datainputs = "dataset=@xlink:href={0};variable=air".format(url)
    resp = client.get(
        service='WPS', request='Execute', version='1.0.0', identifier='simple_plot',
        datainputs=datainputs)
    assert_response_success(resp)
