import functools
import logging

logger = logging.getLogger()


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{key}={value!r}" for key, value in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        logger.info(f"function {func.__name__} called with args {signature}")
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            logger.exception(f"Exception raise in {func.__name__}. exception: {str(e)}")
            raise e

    return wrapper