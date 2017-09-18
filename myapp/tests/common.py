import os
from pywps.tests import WpsClient, WpsTestResponse

TESTS_HOME = os.path.abspath(os.path.dirname(__file__))
CFG_FILE = os.path.join(TESTS_HOME, 'test.cfg')


class WpsTestClient(WpsClient):

    def get(self, *args, **kwargs):
        query = "?"
        for key, value in kwargs.iteritems():
            query += "{0}={1}&".format(key, value)
        return super(WpsTestClient, self).get(query)


def client_for(service):
    return WpsTestClient(service, WpsTestResponse)
