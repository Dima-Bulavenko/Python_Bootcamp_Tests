def get_hash(string):
    n = len(string)
    p = 4
    my_hash = 0
    for p_degree, char in enumerate(string):
        my_hash = (my_hash + ord(char) * p ** p_degree) % 2**n
    else:
        return my_hash

s = "Python Bootcamp"
print(get_hash(s))
