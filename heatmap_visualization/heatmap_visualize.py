## Reference: https://towardsdatascience.com/better-heatmaps-and-correlation-matrix-plots-in-python-41445d0f2bec

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import gridspec

numColors = 100
cmap = sns.diverging_palette(20, 220, n=numColors)
color_min, color_max = [-1, 1]
def value_to_color(val):
    val_position = float((val - color_min)) / (color_max - color_min)
    ind = int(val_position * (numColors - 1))
    return cmap[ind]


class HeatMapVis():

    def __init__(self, data):
        self.data = data

    def show(self):
        dataColNames = self.data.columns
        dataVals = self.data.values
        nRows = self.data.shape[0]
        nCols = self.data.shape[1]

        fig = plt.figure(figsize=(10, 10))
        gs = gridspec.GridSpec(1, 15, hspace=0.2, wspace=0.1)
        ax = plt.subplot(gs[:,:-1])
        ax_legend = plt.subplot(gs[:,-1])

        # fig.tight_layout()

        # scatter plot for showing correlation heatmaps (the bigger rectangle size, the more correlated data values are)
        scale = 1000
        for y in range(0,nRows):
            for x in range(0,nCols):
                size = abs(dataVals[y][x]) * scale
                ax.scatter(x,nRows-y-1,size, color=value_to_color(dataVals[y][x]), marker="s")
                # ax.text(x-0.3,y-0.05,("%.2f" % dataVals[nRows-y-1][x]))

        # adjust figure x and y labels
        ax.xaxis.set_ticks_position("top")
        ax.set_xticks(range(0,nCols))
        ax.set_xticklabels(dataColNames, rotation=45, horizontalalignment="left")
        ax.set_yticks(range(0,nRows))
        ax.set_yticklabels(dataColNames[::-1])

        # put grid into background
        ax.set_facecolor("snow")
        ax.axis("scaled")
        ax.grid(False, "major")
        ax.grid(True, "minor")
        ax.set_xticks([x + 0.5 for x in ax.get_xticks()], minor=True)
        ax.set_yticks([y + 0.5 for y in ax.get_yticks()], minor=True)
        ax.set_xlim(-0.5, nCols-0.5)
        ax.set_ylim(-0.5, nRows-0.5)

        # remove border lines
        ax.spines["top"].set_visible(False)
        ax.spines["right"].set_visible(False)
        ax.spines["bottom"].set_visible(False)
        ax.spines["left"].set_visible(False)

        # plot legend for colorbar
        ax_legend.barh(y=np.linspace(-1, 1, numColors), width=[5]*len(cmap), left=[0]*len(cmap), height=3/numColors, color=cmap, linewidth=0)
        ax_legend.set_xlim(0, 1)
        ax_legend.set_facecolor("white")
        ax_legend.set_xticks([])
        ax_legend.set_yticks(np.linspace(-1, 1, 3))
        ax_legend.yaxis.tick_right()

        ax_legend.spines["top"].set_visible(False)
        ax_legend.spines["right"].set_visible(False)
        ax_legend.spines["bottom"].set_visible(False)
        ax_legend.spines["left"].set_visible(False)


        plt.show()