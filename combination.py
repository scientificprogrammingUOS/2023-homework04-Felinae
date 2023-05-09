import numpy as np 

# implement your function to combine two numpy arrays 

#had to rename function from 'combine' to 'combination' so the pytest works
def combination(nparr1, nparr2, axis=0):

    # delete the NotImplementedError when you write your function.
    
    #pytest can be cheated by just flattening the arrays
    #return np.concatenate((nparr1.flatten(),nparr2.flatten()), axis)

    if (axis > np.ndim(nparr1)) or (axis > np.ndim(nparr2)):
      raise ValueError("The given axis is bigger than the amount of dimensions the arrays have!")
    
    if np.ndim(nparr2) > axis:
      for i in range(np.ndim(nparr2) - axis):
        nparr2 = np.squeeze(nparr2)
    if np.ndim(nparr1) > axis:
      for i in range(np.ndim(nparr1) - axis):
        nparr1 = np.squeeze(nparr1)

    return np.concatenate((nparr1,nparr2), axis)

if __name__ == "__main__":
    # use this for your own testing!

    pass
