from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse   # show plot
# app =from fastapi import FastAPI   // CAN'T WORK

app = FastAPI()


@app.get("/get-tweet-text")
def get_tweet_text(keyword=None, hashtag=None):   # OPT: async def func_name:

    from packages.twitter_text import get_text
    text = get_text(keyword, hashtag)
    return text


@app.get("/get-word-cloud")
def get_word_cloud(text=None):

    from packages.word_cloud_hidden_mask import get_word_cloud_from_text
    if text is None:
        text = "This is a very very very long text"
    wc = get_word_cloud_from_text(text)

    # store to file
    # - save the image in the img folder
    filePath = "img/word_cloud.png"
    wc.to_file(filePath)

    return FileResponse(filePath)


@app.get("/get-word-cloud-from-text")
def get_word_cloud(keyword=None, hashtag=None):
    ############################################################
    # NOT WORK - MAKE IT WORK
    # print(f"keyword = {keyword}")
    # print(f"hashtag = {hashtag}")

    # text = get_tweet_text(keyword, hashtag)
    # print(f"text = {text}")
    # return get_word_cloud(text)
    ############################################################

    from packages.twitter_text import get_text
    text = get_text(keyword, hashtag)

    from packages.word_cloud_hidden_mask import get_word_cloud_from_text
    if text is None:
        text = "This is a very very very long text"
    wc = get_word_cloud_from_text(text)

    # store to file
    # - save the image in the img folder
    filePath = "img/word_cloud.png"
    wc.to_file(filePath)

    return FileResponse(filePath)


# Reusable / small function(s) // Testing
@app.get("/get-image")
def get_image():
    return FileResponse("img/first_review.png")


@app.get("/get-word-cloud00")
def get_word_cloud00():

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
    # plt.figure()
    # plt.imshow(wordcloud, interpolation="bilinear")
    # plt.axis("off")
    # plt.show()

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

    # # display the generated image:
    # plt.imshow(wordcloud, interpolation='bilinear')

    # # return plt
    # plt.savefig('wordCloud.png')
    # file = open('wordCloud.png', mode="rb")

    # save the image in the img folder
    wordcloud.to_file('img/word_cloud.png')

    # return StreamingResponse(file, media_type="image/png")
    return FileResponse('img/word_cloud.png')
