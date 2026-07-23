import numpy as np
from numpy import pi
import matplotlib.pyplot as plt

class SinSignal:
    def __init__(self, amplitude: int, freq: int, ):
        self.xt
        self.amp = amplitude
        self.f = freq
    
    def plot(self, times: int):

class CosSignal:
    def __init__(self, amplitude: int, freq: int):
        self.xt
        self.amp = amplitude
        self.f = freq

    def plot(self):



def main():
    while True:
        try:
            print('Which type of signal need to plot?\n 1. Single sin\n 2. Single cos\n 3. Mixed signal')
            get_signal_type = int(input('Type 1/2/3'))
            if get_signal_type not in [1,2,3]:
                print('Input between 1 2 or 3')
            else:
                break
        except ValueError:
            print('Print only number ')
    match get_signal_type:
        case 1:
            '''sin signal'''
            signal = SinSignal()
        case 2:
            '''cos signal'''
            signal = CosSignal()
        case 3:
            '''mixed mechanism signal'''
            while True:
                print('how many s')



if __name__ == '__main__':
    main()