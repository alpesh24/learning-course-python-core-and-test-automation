import inspect
import time


def log(fn):
    """
    Add your code here or call it from here   
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = fn(*args, **kwargs)
        end_time = time.time()
        total_time = end_time-start_time
        total_time = format(total_time, ".2f")
        args_name = inspect.getfullargspec(fn).args

        with open("log.txt", "a") as file:
            file.write(f"{fn.__name__}; ")
            file.write(f"args: ")
            for i,a in enumerate(args):
                if(i==len(args)-1):
                    file.write(f"{args_name[i]}={a}; ")
                else:    
                    file.write(f"{args_name[i]}={a}, ")
            file.write(f"kwargs: ")
            for i,k in enumerate(kwargs):
                if(i==len(kwargs)-1):
                    file.write(f"{args_name[len(args)+i]}={kwargs[k]}; ")
                else:
                    file.write(f"{args_name[len(args)+i]}={kwargs[k]}, ")
            
            file.write(f"execution_time: {total_time} sec.\n")

        return result
    
    return wrapper

@log
def foo(a, b, c):
    time.sleep(0.3)
    return a+b+c

foo(1, 2, c=3)