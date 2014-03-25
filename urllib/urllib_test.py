import urllib

# unique resource location
url = "http://learnpythonthehardway.org/book/ex6.html"
# hyper text transfer protocol

urllib.urlretrieve(url, "myfile.html")
