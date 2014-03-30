import urllib

# unique resource location
url = "http://learnpythonthehardway.org/book/ex6.html"
# hyper text transfer protocol

urllib.urlretrieve(url, "myfile.html")

url2 = "http://imgnews.naver.net/image/001/2014/03/24/GYH2014032400100004400_P2_59_20140324165907.jpg"
urllib.urlretrieve(url2, "myfile2.jpg")
