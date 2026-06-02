import numpy as np

def add_num_suffix(num):
    num = num + 1
    if num == 1:
        return "1st"
    elif num == 2:
        return "2nd"
    elif num == 3:
        return "3rd"
    else:
        return "{}th".format(num)

def evaluate(row, col, value):
    row_term = add_num_suffix(row)
    col_term = add_num_suffix(col)
    is_term = "is" if value > 0.5 else "is not"
    sentence = "The {} row and {} column has a value of {} and {} bigger than 0.5".format(row_term, col_term, value, is_term)
    return sentence

if __name__ == '__main__':
    # generate array
    rng = np.random.default_rng()
    a = rng.random((4, 8))

    # evaluate elements
    for r in range(a.shape[0]):
        for c in range(a.shape[1]):
            sentence = evaluate(r, c, a[r, c])
            print(sentence)
