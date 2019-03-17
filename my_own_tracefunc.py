import sys


def tracefunc(frame, event, arg):
    """Tracefunction works correct for Python3.7"""
    if event == "return" and len([*frame.f_locals]) > 0:
        print("function:", frame.f_code.co_name, ", local vars:", [*frame.f_locals])
    return tracefunc


<<<<<<< HEAD
def foo():
    friends = ["Bob", "Tom"]
    for f in friends:
        print("Hi {}!".format(f))
    return len(friends)


def tracefoo(target_function):
    sys.settrace(tracefunc)
    target_function()


tracefoo(foo)
=======
def tracefoo(target_function):
    sys.settrace(tracefunc)
    target_function()
>>>>>>> 491ae6cd0e35636c0e893625021e539aacbfcf6f
