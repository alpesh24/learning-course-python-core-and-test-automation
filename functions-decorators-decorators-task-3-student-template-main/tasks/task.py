
def validate(fn):
    '''
    Add corresponded arguments and implementation here. 
    '''
    def wrapper(*args):
       res = list(map(lambda a: a in range(0, 257), args))
       print(res)
       if all(res):
          return fn(*args)
       else:
          return "Function call is not valid!"
       
    return wrapper


@validate
def set_pixel(x: int, y: int, z: int) -> str:
  return "Pixel created!"

print(set_pixel(0, 127, 300))
print(set_pixel(0,127,250))
