from elasticsearch import exceptions

ConnectionError = exceptions.ConnectionError
ElasticHttpError = exceptions.TransportError
ElasticHttpNotFoundError = exceptions.NotFoundError
InvalidJsonResponseError = exceptions.SerializationError

class IndexAlreadyExistsError(ElasticHttpError):
    """Exception raised on an attempt to create an index that already exists"""

