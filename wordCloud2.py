# start with loading all neccessary libraries
# basic libs
import numpy as np
import pandas as pd
from os import path

from io import BytesIO
# import Image
from PIL import Image
'''from PIL import Image, ImageFile

    ImageFile.LOAD_TRUNCATED_IMAGES = True'''

from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
# visualization
import matplotlib.pyplot as plt
# % matplotlib inline
# warning
import warnings
warnings.filterwarnings("ignore")
# models

# load in the dataframe
# without index_col=0 -> read in row name (index)
df = pd.read_csv("data/winemag-data-139k-v2.csv", index_col=0)

# start with one review
text = df.description[0]
print("text =", text)

# changing optional word cloud arguments
# lower max_font_size, chnage the maximum number of word (max_words) & lighten the background (background_color):
wordcloud = WordCloud(max_font_size=50, max_words=100,
                      background_color="white").generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()

# save the image in the img folder
wordcloud.to_file("img/first_review.png")

# combining data
text = " ".join(review for review in df.description)
print("There are {} word in the combination of all review.".format(len(text)))

# create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavors"])
print("stopwords =", stopwords)

# # generate a word cloud image
# WordCloud(stopwords=stopwords, background_color="white").generate(text)

# display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')

# return plt
plt.savefig('wordCloud.png')
file = open('wordCloud.png', mode="rb")
