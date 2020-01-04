
def count_max_consecutive_1(n):
    max = 0
    binary = "{0:b}".format(n)
    print(binary)
    ones = binary.split("0")
    for i in ones:
        size = len(i)
        max = size if max < size else max
    return max

if __name__ == '__main__':
    n = int(input())
    print(count_max_consecutive_1(n))
