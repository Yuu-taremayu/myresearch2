import numpy as np
import matplotlib.pyplot as plt

def f(_x):
    return 0.1*(_x-0.2)**3 - 0.01*_x + 0.005

def main():
    x = np.arange(-0.5, 1, 0.01)
    
    plt.plot(x, f(x))
    plt.vlines([0], -0.2, 0.6, 'black', linestyle='-')
    plt.hlines([0], -0.2, 0.6, 'black', linestyle='-')
    plt.grid(which='major', color='black', linestyle='-')
    plt.grid(which='minor', color='black', linestyle='-')
    plt.xlim(-0.2, 0.6)
    plt.ylim(-0.001, 0.005)
    plt.xticks(color='None')
    plt.yticks(color='None')
    plt.show()

if __name__ == '__main__':
    main()
