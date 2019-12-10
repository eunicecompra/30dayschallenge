def find_max_sum_hourglass(array):
    sums = []
    x_index = 0
    for x in array:
        for i in x:
            top = x[i] + x[i+1] + x[i+2]
            middle = array[x_index+1][i+1]
            bottom_x = array[x_index+2]
            bottom = bottom_x[i] + bottom_x[i+1] + bottom_x[i+2]
            sum = top + middle + bottom
            sums.append(sum)
        x_index += 1


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))