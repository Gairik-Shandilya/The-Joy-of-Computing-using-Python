n = int(input())
m_row = 1
n_row = 1

for row in range(1, n+1):
    b = 0
    for space in range(1, n-row+1):
        print(" ", end="")

    a = row
    left = []
    while(a != n_row):
        if a > 9:
            left.append(str(b))
            b += 1
        else:
            left.append(str(a))
        a += 1

    if row == n:
        print("".join(left) + str(m_row) + "".join(left[::-1]), end="")
    else:
        print("".join(left) + str(m_row) + "".join(left[::-1]))

    if (m_row+2 > 9):
        m_row = -1
    m_row += 2
    n_row += 2
