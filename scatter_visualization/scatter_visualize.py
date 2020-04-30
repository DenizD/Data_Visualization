import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

def getImage(path):
    im = plt.imread(path)
    return OffsetImage(im, zoom=0.15)

class ScatterPlotVis():

    def __init__(self, names, dataX, dataY, xLabel, yLabel):

        self.x = dataX
        self.y = dataY
        self.names = names
        self.xLabel = xLabel
        self.yLabel = yLabel


    def show(self):
        fig, ax = plt.subplots()
        ax.scatter(self.x, self.y)

        for ii, name in enumerate(self.names):
            ab = AnnotationBbox(getImage("scatter_visualization/images/"+name + ".png"), (self.x[ii], self.y[ii]), frameon=False)
            ax.add_artist(ab)

        # for i, txt in enumerate(self.names):
        #     ax.annotate(txt, (self.x[i], self.y[i]))

        plt.xlabel(self.xLabel)
        plt.ylabel(self.yLabel)
        plt.show()