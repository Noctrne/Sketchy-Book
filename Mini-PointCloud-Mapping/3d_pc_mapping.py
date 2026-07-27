import numpy as np
import matplotlib.pyplot as plt


class CloudPlot:
    def __init__(self, len_t: int, freq: int):
        self.Z = len_t
        self.freq = freq

    def _cos_sin_plot(self):
        self.z_data = np.linspace(0, self.Z, 1001)
        x_data = np.cos(2 * np.pi * self.freq * self.z_data)
        y_data = self.z_data * np.sin(2 * np.pi * self.freq * self.z_data)
        return x_data, y_data

    def _visualize(self):
        x, y = self._cos_sin_plot()

        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        ax.plot3D(x, y, self.z_data, color='blue')

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.show()


class BoxPlot:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    @staticmethod
    def _gen_lins(data):
        return np.linspace(0, data, 1001)

    def _visualize(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')

        linex = self._gen_lins(self.x)
        liney = self._gen_lins(self.y)
        linez = self._gen_lins(self.z)

        '''align with x axis (from 0yz to xyz)'''
        ax.plot3D(linex,np.zeros_like(linex),np.zeros_like(linex))
        ax.plot3D(linex,np.zeros_like(linex),np.full_like(linex, self.z))
        ax.plot3D(linex,np.full_like(linex, self.y),np.zeros_like(linex))
        ax.plot3D(linex,np.full_like(linex, self.y),np.full_like(linex, self.z))

        '''align with y axis (from x0z to xyz)'''
        ax.plot3D(np.zeros_like(liney),liney,np.zeros_like(liney))
        ax.plot3D(np.zeros_like(liney),liney,np.full_like(liney, self.z))
        ax.plot3D(np.full_like(liney, self.x),liney,np.zeros_like(liney))
        ax.plot3D(np.full_like(liney, self.x),liney,np.full_like(liney, self.z))

        '''align with z axis (from xy0 to xyz)'''
        ax.plot3D(np.zeros_like(linez),np.zeros_like(linez),linez)
        ax.plot3D(np.zeros_like(linez),np.full_like(linez, self.y),linez)
        ax.plot3D(np.full_like(linez, self.x),np.zeros_like(linez),linez)
        ax.plot3D(np.full_like(linez, self.x),np.full_like(linez, self.y),linez)

        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")

        plt.show()


def main():
    # cloud = CloudPlot(len_t=10, freq=1)
    # cloud._visualize()

    box = BoxPlot(10, 10, 10)
    box._visualize()


if __name__ == '__main__':
    main()