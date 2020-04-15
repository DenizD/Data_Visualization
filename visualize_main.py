from wordcloud_visualization.wordcloud_visualize import WordCloudVis
from heatmap_visualization.heatmap_visualize import HeatMapVis
import pandas as pd
visMode = "heatmap"

## Wordcloud visualization
if(visMode == "wordcloud"):
    textFile = "./wordcloud_visualization/dog.txt"
    maskFile = "./wordcloud_visualization/dog.png"
    wc = WordCloudVis(textFile=textFile, maskFile=maskFile)
    wc.show()

## Heatmap visualization
elif(visMode == "heatmap"):
    data = pd.read_csv("./heatmap_visualization/autos.csv")
    columns = ["bore", "stroke", "compression-ratio", "horsepower", "city-mpg", "price"]

    corrMatrix = data[columns].corr()

    hm = HeatMapVis(corrMatrix)
    hm.show()