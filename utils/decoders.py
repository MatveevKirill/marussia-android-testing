import time

from common.exceptions import UnclassifiedException


def wait(_method, _error=UnclassifiedException, _timeout=10, _interval=0.5, _check=False, **kwargs):
    st = time.time()
    last_exception = None
    while time.time() - st < _timeout:
        try:
            result = _method(**kwargs)
            if _check:
                if result:
                    return result
                last_exception = f'Method {_method.__name__} returned {result}'
            else:
                return result
        except _error as e:
            last_exception = e
        time.sleep(_interval)

    raise TimeoutError(f'Method {_method.__name__} timeout in {_timeout}sec with exception: "{last_exception}"')
