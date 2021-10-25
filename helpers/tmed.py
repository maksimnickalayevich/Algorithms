from datetime import datetime


def tmed(template):
    """
    Used to find an execution time of a wrapped function
    :param template: will be used in logging to console as [NAME_OF_THE_FUNC] Execution Time...
    :return:
    """
    def wrapped_fun(fn):
        def wrapper(*args, **kwargs):
            startTime = datetime.now()
            result = fn(*args, **kwargs)
            endTime = datetime.now()
            print(f"[{template}] Execution Time: {endTime - startTime}")
            return result

        return wrapper

    return wrapped_fun
