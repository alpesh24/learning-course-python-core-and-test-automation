from contextlib import ContextDecorator
import datetime
from numbers import Number
import time

class LogFile(ContextDecorator):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        end_time = datetime.datetime.now()
        execution_time = end_time - self.start_time
        with open(self.filename, 'a') as file:
            file.write(f"Start: {self.start_time} | Run: {execution_time} | An error occurred: {exc_value}\n")
        if exc_type is not None:
            return False
        return True
   
@LogFile('my_trace.log')
def some_func():
    try:
        result = 1 / 0
        if isinstance(result, Number) :
            return result
        else:
            raise ZeroDivisionError("division by zero")
    except ZeroDivisionError as e:
        return(e)

print(some_func())
