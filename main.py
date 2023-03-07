# tut url: https://anderfernandez.com/en/blog/how-to-create-api-python/

from fastapi import FastAPI
from fastapi.responses import StreamingResponse   # show plot
# app =from fastapi import FastAPI   // CAN'T WORK
app = FastAPI()

# # Version 1.1 - without user input
# @app.get("/my-first-api")
# def hello():
#     return ("Hello world!")

# # Version 1.2 - with user input
# @app.get("/my-first-api")
# def hello(name: str):
#     return ('Hello ' + name + '!')

# Version 3 - without or with user input


@app.get("/my-first-api")
def hello(name=None):

    if name is None:
        text = 'Hello!'

    else:
        text = 'Hello ' + name + '!'

    return text

# ===return different data types with FastAPI===
# return dataframe


@app.get("/get-iris")
def get_iris():

    import pandas as pd
    url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    return iris


# return plot
@app.get("/plot-iris")
def get_iris():

    import pandas as pd
    import matplotlib.pyplot as plt

    url = 'https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')
    file = open('iris.png', mode="rb")

    return StreamingResponse(file, media_type="image/png")
