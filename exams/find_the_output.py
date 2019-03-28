def fn(inputs):
    z = 0
    x = 0
    y = 0
    for i in range(0, len(inputs)-1):
        total = inputs[i] + inputs[i + 1]
        if total > z:
            x = inputs[i]
            y = inputs[i + 1]
            z = total
    print(x, y, z)


inputs = [1, 2, 3, 40, 5, 11, 5, 1, 10, 3]
fn(inputs)
