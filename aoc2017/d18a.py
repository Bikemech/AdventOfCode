# registers starts wth value 0 implicitly
# ergo if a register is not present then it should be added with value 0 when first called.

def format_data(line):
    return [string.strip() for string in line.split()]

def duet(data):
    ptr = 0


data = [format_data(string) for string in open("d18.input", "r").readlines()]

registers = dict()

def dec(func):
    a = 40
    def inner(args):
        print(a)
        a = args
        return func(args)
    return inner

@dec
def test(x):
    return x

test(9)