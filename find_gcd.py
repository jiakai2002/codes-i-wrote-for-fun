import math


def find_square_root(a):
    while True:
        x = a / 2
        y = (x + a / x) / 2
        epsilon = 0.000001
        if abs(y - x) < epsilon:
            break
        x = y
    return y


for i in range(1, 10):
    print(
        i,
        "\t",
        find_square_root(i),
        "\t",
        math.sqrt(i),
        "\t",
        abs(math.sqrt(i) - find_square_root(i)),
        "\n",
    )
