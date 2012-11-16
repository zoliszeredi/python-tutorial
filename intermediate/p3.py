import time

def time_slow(threshold = 0.5):
    def decorator(f):
        def wrap(*args):
            """wrap docstring"""
            start = time.time()
            f(*args)
            stop = time.time()
            diff = stop - start
            if diff > threshold:
                stream = open('slow.log', 'a')
                stream.write('{} : {}\n'.format(f.__name__, diff))
                stream.close()                     
        wrap.__name__ = f.__name__
        wrap.__doc__ = f.__doc__
        wrap.__dict__.update(f.__dict__)
        return wrap
    return decorator

@time_slow(threshold = 0.1)
def first(time_in_float):
    """first's docstring"""
    time.sleep(time_in_float)

@time_slow
def second():
    """second's docstring"""
    time.sleep(1.0)

first(0.2)
first.foo = 5
#second()
#second.bar = 10
assert(first.__name__ == "first")
assert(first.__doc__ == """first's docstring""")
assert(first.__dict__ == { 'foo': 5 })
#assert(second.__name__ == "bar")
#assert(second.__doc__ == """bar's docstring""")
#assert(second.__dict__ == { 'bar': 10 })
