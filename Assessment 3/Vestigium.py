t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    N = int(input())
    input_matrix = []
    for i in range(N):
        raw_input = input().split(" ")
        input_matrix.append([int(s) for s in raw_input])

    main_diagonal = 0
    repeated_row = 0
    repeated_column = 0
    for j in range(N):
        main_diagonal += input_matrix[j][j]
        tmp_set = set(input_matrix[j])
        if len(tmp_set) != N:
            repeated_row += 1

    for j in range(N):
        tmp_set = set()
        for k in range(N):
            tmp_set.add(input_matrix[k][j])
        if len(tmp_set) != N:
            repeated_column += 1

    print("Case #{}: {} {} {}".format(i, main_diagonal, repeated_row, repeated_column))
