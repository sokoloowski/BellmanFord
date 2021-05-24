class AlgorithmException(Exception):
    """
    Exception raised for general algorithm errors
    """
    pass

class InputDataException(AlgorithmException):
    """
    Exception raised for errors in data values.
    """
    pass

class DataFormatException(AlgorithmException):
    """
    Exception raised for errors in data format.
    """
    pass

class MissingRouteException(AlgorithmException):
    """
    Exception raised for infinite cost of route
    (no route to destination is available)
    """
    pass
