def find_max_sum_hourglass(array):
    sums = []
    array_length = len(array)
    x_index = 0
    for x in array:
        x_length = len(x)
        for i in x:
            if i+2 >= x_length:
                continue
            top = x[i] + x[i+1] + x[i+2]

            if x_index+1 >= array_length:
                continue
            middle = array[x_index+1][i+1]

            if x_index+2 >= array_length:
                continue
            bottom_x = array[x_index+2]
            bottom = bottom_x[i] + bottom_x[i+1] + bottom_x[i+2]

            sum = top + middle + bottom
            sums.append(sum)
        x_index += 1

    sums.sort()
    return sums[len(sums)-1]


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))