import numpy as np
import matplotlib.pyplot as plt



class CloudPlot:
    def __init__(self, len_t: int, freq: int):
        self.Z = len_t
        self.freq = freq

    def cos_sin_plot(self):
        self.z_data = np.linspace(0,self.Z,1001)
        x_data = np.cos(2*np.pi*self.freq*self.z_data)
        y_data = self.z_data*np.sin(2*np.pi*self.freq*self.z_data)
        return x_data, y_data

    def visualize(self):
        x, y = self.cos_sin_plot()
        plt.figure()
        ax = plt.axes(projection = '3d')
        ax.plot3D(x, y, self.z_data)
        plt.show()



def main():
    test = CloudPlot(len_t=10, freq=1)
    test.visualize()



if __name__ == '__main__':
    main()