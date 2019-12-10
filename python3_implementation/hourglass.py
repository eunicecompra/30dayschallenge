def find_max_sum_hourglass(array_2d):
    sums = []
    array_len = len(array_2d)
    x_index = 0
    for x_axis in array_2d:
        x_len = len(x_axis)
        for y_axis in x_axis:
            if y_axis+2 >= x_len:
                continue
            top = x_axis[y_axis] + x_axis[y_axis+1] + x_axis[y_axis+2]

            if x_index+1 >= array_len:
                continue
            middle = array_2d[x_index+1][y_axis+1]

            if x_index+2 >= array_len:
                continue
            bottom_x = array_2d[x_index+2]
            bottom = bottom_x[y_axis] + bottom_x[y_axis+1] + bottom_x[y_axis+2]

            sum = top + middle + bottom
            sums.append(sum)
        x_index += 1

    sums.sort()
    return sums[len(sums)-1]


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))