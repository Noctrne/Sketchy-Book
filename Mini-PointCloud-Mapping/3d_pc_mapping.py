import numpy as np
import matplotlib.pyplot as plt



class CloudPlot:
    def __init__(self):
        pass

    def visualize(self):
        plt.figure()
        plt.axes(projection = '3d')
        plt.show()



def main():
    test = CloudPlot()
    test.visualize()



if __name__ == '__main__':
    main()