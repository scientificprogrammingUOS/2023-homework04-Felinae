import numpy as np

# implement the function strange pattern

def strange_pattern(shape):
    # delete the NotImplementedError when you write your function.
    arr = np.ndarray((shape), dtype=bool)
    
    for i in range(shape[0]):
        for j in range(shape[1]):
            #true values are in places where sum of row number and column number is divisible by 3
            if (i+j)%3 == 0:
                arr[i][j] = 1
            else:
                arr[i][j] = 0
    
    return arr


if __name__ == "__main__":
    # use this for your own testing!

    print(strange_pattern((6,8)))

