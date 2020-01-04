def find_max_sum_hourglass(array_2d):
    sums = []
    array_len = len(array_2d)
    y_index = 0
    for y_axis in array_2d:
        y_len = len(y_axis)
        x_index = 0
        for x_axis in y_axis:
            if x_index+2 >= y_len:
                continue
            top = x_axis + y_axis[x_index+1] + y_axis[x_index+2]

            if y_index+1 >= array_len:
                break
            middle = array_2d[y_index+1][x_index+1]

            if y_index+2 >= array_len:
                break
            bottom_x = array_2d[y_index+2]
            bottom = bottom_x[x_index] + bottom_x[x_index+1] + bottom_x[x_index+2]

            sum = top + middle + bottom
            sums.append(sum)
            x_index += 1

        y_index += 1

    sums.sort()
    return sums[len(sums)-1]


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    print(find_max_sum_hourglass(arr))