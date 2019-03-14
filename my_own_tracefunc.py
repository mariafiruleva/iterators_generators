import sys


def tracefunc(frame, event, arg):
    """Tracefunction works correct for Python3.7"""
    if event == "return" and len([*frame.f_locals]) > 0:
        print("function:", frame.f_code.co_name, ", local vars:", [*frame.f_locals])
    return tracefunc


def tracefoo(target_function):
    sys.settrace(tracefunc)
    target_function()
