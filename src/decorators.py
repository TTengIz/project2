from time import time
from typing import Any


def log(filename: Any = None) -> Any:
    """ Декоратор, котрый записывает результат работы функции или ее ошибок."""
    def my_decorartors(func):
        def wrapper(*args, **kwargs):
            try:
                start_time = time()
                result = func(*args, **kwargs)
                stop_time = time()
                log_result = (f'{func.__name__} start of work: {start_time},function result: {result},'
                              f' end of work: {stop_time}, \n')
            except Exception as e:
                log_result = f'{func.__name__} error: {e}. Inputs: ({args}, {kwargs})\n'
                raise
            finally:
                if filename:
                    with open(filename, 'a', encoding='utf8') as names_file:
                        names_file.write(log_result)
                elif not filename:
                    print(log_result)
            return result
        return wrapper
    return my_decorartors


@log(filename="mylog.txt")
def my_function(x: int, y: int) -> int:
    return x + y

print(my_function(3, 1))