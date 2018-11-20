import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def process_data():
    md = pd.read_csv('4p.csv')
    md = md.sort_values('winPlacePerc')
    md = md.reset_index()
    return md

PLOTS_PER_ROW = 5
def plot_data(data):
    num = len(data.columns)
    rows = np.ceil(num / PLOTS_PER_ROW)
    index = 1

    plt.figure(figsize=(30,40))
    for c in data.columns:
        if data[c].dtype in [np.int, np.int64, np.float64, np.float]:
            plt.subplot(rows, PLOTS_PER_ROW, index)
            index += 1
            plt.plot(data[c])
            plt.title(c)
    plt.show()

if __name__ == '__main__':
    data = process_data()
    plot_data(data)
