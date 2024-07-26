class BaseCustomError(Exception):
    """Base class for custom errors"""
    def __init__(self, message, status_code):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message, self.status_code)


class GraphControllerError(BaseCustomError):
    """Raised when there's an error processing graph data"""
    def __init__(self, message, status_code=500):
        super().__init__(message, status_code)


class ElasticsearchError(BaseCustomError):
    """Raised when there's an error with Elasticsearch operations"""
    def __init__(self, message, status_code=500):
        super().__init__(message, status_code)


class NotFoundUserError(BaseCustomError):
    """Raised when can't search user from Elasticsearch"""
    def __init__(self, message, status_code=404):
        super().__init__(message, status_code)


class NotFoundUserError(BaseCustomError):
    """Raised when can't search user from Elasticsearch"""
    def __init__(self, message, status_code=404):
        super().__init__(message, status_code)


class GraphDataRequestParamsError(BaseCustomError):
    """Raised when there's an error with request parameters for graph data"""
    def __init__(self, message, status_code=400):
        super().__init__(message, status_code)


class RequestParamsError(BaseCustomError):
  def __init__(self, message, status_code=400):
        super().__init__(message, status_code)