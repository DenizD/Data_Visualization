import random
import numpy as np
import matplotlib.pyplot as plt

class BarChartVis():
    def __init__(self, values, labels, colors=None, figSize=(15,8), textTitle=None, valuesTitle=None):
        self.values = values
        self.labels = labels
        self.values, self.labels = zip(*sorted(zip(self.values, self.labels), reverse=True)) # sort the values and labels in descending order if it is not sorted
        self.colors = colors if colors is not None else [(random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1)) for i in range(len(self.labels))]
        self.figSize = figSize
        self.textTitle = textTitle
        self.valuesTitle = valuesTitle

    ## show bar chart
    def show(self):

        fig, ax = plt.subplots(figsize=self.figSize)

        xData = self.values
        yData = self.labels

        # Styles for texts and colors on bar graph
        ax.set_yticks(np.arange(len(yData)))
        ax.set_yticklabels(yData)
        ax.invert_yaxis()
        ax.grid(which="major", axis="x", linestyle="-")
        ax.xaxis.set_ticks_position("top")

        ax.text(0, 1.1, self.textTitle, transform=ax.transAxes, size=16, fontweight="bold", color="#777777")
        ax.text(0, 1.05, self.valuesTitle, transform=ax.transAxes, size=12, color="#777777")

        # Show values on bars
        dx = xData[0] / 100
        for ii, val in enumerate(xData):
            ax.text(val + dx, ii + 0.1, str(val), color=self.colors[ii], fontweight="bold")

        plt.box(False)

        ax.barh(yData, xData, align="center", color=self.colors)

        plt.show()
