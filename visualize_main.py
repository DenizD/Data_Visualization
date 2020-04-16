from wordcloud_visualization.wordcloud_visualize import WordCloudVis
from heatmap_visualization.heatmap_visualize import HeatMapVis
from barchart_visualization.barchart_visualize import BarChartVis
import pandas as pd
import requests

visMode = "wordcloud"

## Wordcloud visualization
if(visMode == "wordcloud"):
    textFile = "./wordcloud_visualization/dog.txt"
    maskFile = "./wordcloud_visualization/dog.png"
    wc = WordCloudVis(textFile=textFile, maskFile=maskFile)
    wc.show()

## Heatmap visualization
elif(visMode == "heatmap"):
    data = pd.read_csv("./heatmap_visualization/autos.csv")
    columns = ["bore", "stroke", "horsepower", "city-mpg", "price"]

    corrMatrix = data[columns].corr()

    hm = HeatMapVis(corrMatrix)
    hm.show()

## Barchart visualization
elif(visMode == "barchart"):

    ## get top 10 countries in coronovirus deaths
    url = "https://pomber.github.io/covid19/timeseries.json"  # url for timeseries data for coronavirus statistics

    req = requests.get(url=url).json()
    countries = [country for country in req]
    totalDeaths = [req[country][-1]["deaths"] for country in countries]
    totalDeaths, countries = zip(*sorted(zip(totalDeaths, countries), reverse=True))

    values = totalDeaths[0:10]
    labels = countries[0:10]
    # colors = ["dodgerblue", "gold", "cornflowerblue", "royalblue", "crimson", "green", "red", "darkorange", "silver", "olive"]

    bc = BarChartVis(values=values, labels=labels, colors=None, textTitle="Top 10 Countries in Coronavirus Deaths", valuesTitle="Deaths")
    bc.show()