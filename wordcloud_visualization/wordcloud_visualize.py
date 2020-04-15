from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

class WordCloudVis():

    def __init__(self,
                 textFile,
                 stopWordsSet={}, # words that you want to exclude from wordcloud
                 max_font_size=50,
                 max_words=1000,
                 background_color="white",
                 maskFile=None,
                 contour_color="saddlebrown",
                 contour_width=2,
                 fig_size=[7,7]):

        self.text = open(textFile).read()
        self.stopWordsSet = stopWordsSet
        self.max_font_size=max_font_size
        self.max_words=max_words
        self.background_color=background_color
        self.mask = np.array(Image.open(maskFile)) if maskFile else np.array([[0]])
        self.contour_color=contour_color
        self.contour_width = contour_width
        self.fig_size = fig_size


    def show(self):
        stopwords = set(STOPWORDS)
        stopwords = stopwords.union(self.stopWordsSet)

        wordcloud = WordCloud(stopwords=stopwords,
                              max_font_size=self.max_font_size,
                              max_words=self.max_words,
                              background_color=self.background_color,
                              mask=self.mask if np.sum(self.mask) else None,
                              contour_color=self.contour_color,
                              contour_width=self.contour_width)
        wordcloud.generate(self.text)

        image_colors = ImageColorGenerator(self.mask) if np.sum(self.mask) else None
    
        plt.figure(figsize=self.fig_size)
        plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
        plt.axis("off")
        plt.show()

