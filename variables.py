a = 1       # a WILL be extracted
b = 2       # b WILL be extracted

c = a + b   # c WILL be extracted

def sum(a, b):
    d = a + b   # d will NOT be extracted
    return d

e = sum(a, b)   # e WILL be extracted

my_num = 1.23           # my_num WILL be extracted
my_str = "test"         # my_str will NOT be extracted
my_bool = True          # my_bool will NOT be extracted
my_list = [1, 2, 3]     # my_list will NOT be extracted
my_dict = {a: 1, b: 2}  # my_dict will NOT be extracted
