import requests
from PIL import Image
import io

# get plot
resp = requests.get('http://127.0.0.1:8000/plot-iris')
file = io.BytesIO(resp.content)
im = Image.open(file)
im.show()

# get text
resp = requests.get("http://127.0.0.1:8000/my-first-api?name=Ander")
resp.text   # will not show
print("resp.text =", resp.text)
print(f"resp.text = {resp.text}")
