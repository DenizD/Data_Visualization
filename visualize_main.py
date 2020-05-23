from wordcloud_visualization.wordcloud_visualize import WordCloudVis
from heatmap_visualization.heatmap_visualize import HeatMapVis
from barchart_visualization.barchart_visualize import BarChartVis
from scatter_visualization.scatter_visualize import ScatterPlotVis
from piechart_visualization.piechart_visualize import PieChartVis
import pandas as pd
import requests

visMode = "barchart"

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

## Scatter plot visualization of ppg and age for the top 20 NBA player in ppg in 2019-2020 season
elif(visMode == "scatter"):
    data = pd.read_excel("scatter_visualization/2019-2020_NBA_Player_Stats_NBAstuffer.xlsx", sheet_name="Sheet1", header=1)
    data = data.sort_values("PPGPointsPoints per game.", ascending=False)
    data = data.head(20)
    names = data["FULL NAME"]
    ppgs = data["PPGPointsPoints per game."]
    ages = data["AGE"]

    names = names.tolist()
    names = list(map(lambda name: name.replace(" ", "_").lower(), names))
    dataX = ages.tolist()
    dataY = ppgs.tolist()
    xLabel = "Age"
    yLabel = "PPG"


    sp = ScatterPlotVis(names, dataX, dataY, xLabel, yLabel)
    sp.show()

## Pie chart visualization for top 10 popular programming languages (Ref: http://pypl.github.io/PYPL.html)
elif(visMode == "piechart"):
    labels = ["Python", "Java", "Javascript", "C#", "PHP", "C/C++", "R", "Objective-C", "Swift", "Other"]
    percentages = [31.17, 17.75, 7.99, 7.05, 6.09, 5.67, 3.93, 2.4, 2.26, 15.69]
    explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    pc = PieChartVis(labels, percentages, explode)
    pc.show()