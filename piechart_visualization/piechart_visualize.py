import matplotlib.pyplot as plt

class PieChartVis():

    def __init__(self, labels, values, explode):
        self.labels = labels
        self.values = values
        self.explode = explode
        
    def show(self):
        fig, ax = plt.subplots()
        
        ax.pie(self.values,
                explode=self.explode,
                labels=self.labels,
                autopct="%1.1f%%",
                shadow=False,
                startangle=0)

        ax.axis("equal")

        plt.show()