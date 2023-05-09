import numpy as np

# implement the function gaussian_analysis

def gaussian_analysis(loc, scale, lower_bound,upper_bound):
        
    # delete the NotImplementedError when you write your function.

    #check if values are numbers
    if not(isinstance((loc), (int,float))) or not(isinstance((scale), (int,float))) or not(isinstance((lower_bound), (int,float))) or not(isinstance((upper_bound), (int,float))):
        raise TypeError("The parameters have to to be numbers!")      
    #lower bound smaller than upper bound 
    elif lower_bound >= upper_bound:
        raise ValueError("The lower bound must be smaller than the upper bound!")
     #analysis part
    else:
        samples = np.random.normal(loc,scale, 100)
        filtered = []
        for i in range(0,99):
            if ((samples[i] > lower_bound) and (samples[i]< upper_bound)):
                 filtered.append(samples[i])
        return (np.mean(filtered),np.std(filtered))


if __name__ == "__main__":
    # use this for your own testing!

    #gaussian_analysis(1,2,3,2)
    #gaussian_analysis(1,2,'a',4)
    gaussian_analysis(1,2,3,4)

