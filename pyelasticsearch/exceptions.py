from requests import Timeout

from elasticsearch import exceptions

ConnectionError = exceptions.ConnectionError
ElasticHttpError = exceptions.TransportError
ElasticHttpNotFoundError = exceptions.NotFoundError

class IndexAlreadyExistsError(ElasticHttpError):
    """Exception raised on an attempt to create an index that already exists"""


class InvalidJsonResponseError(Exception):
    """
    Exception raised in the unlikely event that ES returns a non-JSON response
    """
    @property
    def response(self):
        return self.args[0]

    def __unicode__(self):
        return u'Invalid JSON returned from ES: %r' % (self.response,)
