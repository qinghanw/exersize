def uniquePaths(m: int, n: int) -> int:
        temp = {}
        if m == 1 or n == 1:
            temp['(1, n)'] = temp['(m, 1)'] = 1
        for i in range(2, m):
            for j in range(2, n):
                temp['({}, {})'.format(i, j)] = temp['({}, {})'.format(i-1, j)] + temp['({}, {})'.format(i, j-1)]

        return temp['({}, {})'.format(m,n)]

total = uniquePaths(7, 3)
print(total)