# tut url: https://www.datacamp.com/tutorial/wordcloud-python
# dataset url: https://www.kaggle.com/datasets/zynicide/wine-reviews

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

# function


def transform_format(val):
    print("val =", val)
    if val == 0:
        return 255
    else:
        return val


# load in the dataframe
# without index_col=0 -> read in row name (index)
df = pd.read_csv("data/winemag-data-139k-v2.csv", index_col=0)

'''# looking at first 5 rows of the dataset
df.head()
print("df.head() = \n{}".format(df.head()))

print("df.shape = ", df.shape)
print("There are {} observation and {} feature in this dataset. \n".format(df.shape[0], df.shape[1]))
print("There are {} types of wine in this dataset, such as {}... \n".format(len(df.variety.unique()), 
                                                                            ", ".join(df.variety.unique()[0:5])))
print("There are {} countries producing wine in this dataset, such as {}... \n".format(len(df.country.unique()),
                                                                                        ", ".join(df.country.unique()[0:5])))

print('df[["country", "description", "points"]].head()\n', df[["country", "description", "points"]].head())

# Groupby by country
country = df.groupby("country")

# summary statistic of all countries
print("country.describe().head() = \n", country.describe().head())

# top 5 highest average points
print('country.mean().sort_values(by="points", ascending=False).head() = \n', country.mean().sort_values(by="points", ascending=False).head())'''

'''# plot the data
print("country.size() = \n", country.size())
print("country.size().sort_values(ascending=False) = \n", country.size().sort_values(ascending=False))
plt.figure(figsize=(15,10))
country.size().sort_values(ascending=False).plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Country of Origin")
plt.ylabel("Number of Wines")
plt.show()'''

'''# examine data
print("country.max() = \n", country.max())
print('country.max().sort_values(by="points", ascending=False) = \n', country.max().sort_values(by="points", ascending=False))
print('country.max().sort_values(by="points", ascending=False)["points"] = \n', country.max().sort_values(by="points", ascending=False)["points"])
plt.figure(figsize=(15,10))
country.max().sort_values(by="points", ascending=False)["points"].plot.bar()
plt.xticks(rotation=50)
plt.xlabel("Country of Origin")
plt.ylabel("Highest point of Wines")
plt.show()'''

# === setting up a basic word cloud in Python ===
# ?function
# ?WordCloud

# start with one review
text = df.description[0]
print("text =", text)

'''# create and generate a word cloud image
wordcloud = WordCloud().generate(text)

# display the generate image
plt.imshow(wordcloud, interpolation='bilinear')   # interpolation='bilinear' -> make image appear smoothly
plt.axis("off")   # "off" -> don't show axis no
plt.show()'''

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

# generate a word cloud image
WordCloud(stopwords=stopwords, background_color="white").generate(text)

# display the generated image:
plt.imshow(wordcloud, interpolation='bilinear')

# unwrap outer array layer # OPT: "", 'img/wine_mask.png', "wine_mask.png", '/Users/zrhun/Desktop/Coding/Word Cloud from Twitter/img/wine_mask.png'   # CAN'T WORK
# wine_mask = np.array(Image.open("img/wine_mask.png"))[0]   // MAYBE GOT PROBLEM
wine_mask = np.array(Image.open("img/wine_mask.png"))
print("wine_mask =", wine_mask)
'''wine_mask = "img/wine_mask.png"   # OPT: "wine_mask.png", "cup.png", "cup.png"
with Image.open(wine_mask) as wine_mask:
    # wine_mask
    print("wine_mask =", wine_mask)'''

# transform your mask into a new one that will work with the function
transformed_wine_mask = np.ndarray(
    (wine_mask.shape[0], wine_mask.shape[1]), np.int32)

for i in range(len(wine_mask)):
    transformed_wine_mask[i] = list(map(transform_format, wine_mask[i]))

# check the expected result of your mask
# print("transformed_wine_mask =", transformed_wine_mask)
print("transformed_wine_mask =")
print(transformed_wine_mask)

# create a word cloud image
"""wc = WordCloud(background_color="white", max_words=1000, mask=transformed_wine_mask,
               stopwords=stopwords, contour_width=3, contour_color='firebrick')"""
wc = WordCloud(background_color="white", max_words=1000, mask=transformed_wine_mask,
               stopwords=stopwords, contour_color='firebrick',
               # contour_width=3
               width=800, height=400
               )

# # generate a wordcloud
# wc.generate(text)   # TODO: chk in doc

# # store to file
# wc.to_file("img/wine2.png")

# show
plt.figure(figsize=[20, 10])
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
