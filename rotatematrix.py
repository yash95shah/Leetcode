matrix = [[1, 4, 5],
          [3, 4, 7],
          [6, 5, 2]
          ]


def rotatematrix(input_array, n):
    input_array = input_array[::-1]
    for i in range(n):
        for j in range(i):
            input_array[i][j], input_array[j][i] = input_array[j][i], input_array[i][j]

    return input_array


print(rotatematrix(input_array=matrix, n=3))
