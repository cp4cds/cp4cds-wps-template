
from pywps import Process, LiteralInput, ComplexInput, ComplexOutput
from pywps import Format

import logging
LOGGER = logging.getLogger('PYWPS')

import matplotlib.pylab as plt
import cartopy.crs as ccrs
from netCDF4 import Dataset
import matplotlib
matplotlib.use('Agg')  # no X11 server


def simple_plot(resource, variable=None, output=None):
    output = output or 'plot.png'
    ds = Dataset(resource)
    values = ds.variables[variable]
    fig = plt.figure(figsize=(20, 10))
    ax = plt.axes(projection=ccrs.PlateCarree())
    plt.contourf(values[0, :, :])
    ax.stock_img()
    ax.coastlines()
    plt.colorbar()
    fig.savefig(output)
    plt.close()
    return output


class SimplePlot(Process):
    def __init__(self):
        inputs = [
            ComplexInput('dataset', 'Dataset', supported_formats=[Format('application/x-netcdf')],
                         default='https://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/ncep.reanalysis/surface/air.sig995.2012.nc',  # noqa
                         abstract='Default: https://www.esrl.noaa.gov/psd/thredds/fileServer/Datasets/ncep.reanalysis/surface/air.sig995.2012.nc'),  # noqa
            LiteralInput('variable', 'Variable', data_type='string',
                         default='air',
                         abstract='Please enter the variable name to be plotted. Default: air'),
        ]
        outputs = [
            ComplexOutput('output', 'Simple Plot', supported_formats=[Format('image/png')],
                          as_reference=True),
        ]

        super(SimplePlot, self).__init__(
            self._handler,
            identifier='simple_plot',
            title='Simple Plot',
            abstract='Returns a nice and simple plot.',
            version='1.0',
            inputs=inputs,
            outputs=outputs,
            store_supported=True,
            status_supported=True
        )

    def _handler(self, request, response):
        variable = request.inputs['variable'][0].data
        output = simple_plot(
            resource=request.inputs['dataset'][0].file,
            variable=variable)
        LOGGER.info("produced output: %s", output)
        response.outputs['output'].file = output
        response.update_status("simple_plot done", 100)
        return response
