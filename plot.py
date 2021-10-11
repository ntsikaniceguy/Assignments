import matplotlib.pyplot as plt
import numpy as np

if __name__ == '__main__':

    filepath = 'convergence_plots_f1.txt'  # TODO: add path to your data file here
    names = ["Steepest Descent", "Newton's Method", "Quasi-Newton's Method", "Conjugate Gradient Method"]  # TODO: add the names of each sorting method in the order they are saved in the text file
    x = list(range(1, 10001, 1))  # this is the range of input sizes tested
    
    with open(filepath, 'r') as file:
        for i, line in enumerate(file):
  
            y = list( map(float, line.split(',')) )
            plt.plot(x, y, label=names[i])

    plt.xticks(range(0, 10000, 100))
    plt.yticks(range(0, 200, 10))
    plt.xlabel('No. of Iterations')
    plt.ylabel('convergence criteria')
    plt.title('Comparison of convergence rates')
    plt.legend()
    plt.savefig("sorting_f1.pdf")
    plt.show()
    