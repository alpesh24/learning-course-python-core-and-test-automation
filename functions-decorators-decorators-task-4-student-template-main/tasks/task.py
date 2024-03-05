
def decorator_apply(lambda_func):
    '''
    Add your implementation here
    '''
    def decorator(func_to_decorate):
        def wrapper(*args, **kwargs):
            
            result = lambda_func(*args, **kwargs)
            return func_to_decorate(result)
        
        return wrapper
    return decorator


@decorator_apply(lambda user_id: user_id + 1)
def return_user_id(num: int) ->int:
    return num

print(return_user_id(42))