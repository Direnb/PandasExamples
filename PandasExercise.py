import pandas as pd
df =  pd.read_csv("imdb.csv")

"""
1- Dosya hakkındaki bilgiler.
2- İlk 5 kaydı gösterin.
3- Son 10 kaydı gösterin.
4- Sadece Movie_Title kolonunu alın.
5- Sadece Movie_Title kolonunu içeren ilk 5 kaydı alın.
6- Sadece Movie_Title ve Rating kolonunu içeren ilk 1 kaydı alın.
7- Sadece Movie_Title ve Raiting kolonunu içeren ikinci 5 kaydı alın.
8- Sadece Movie_Title ve Raiting kolonunu içeren ve imdb puanı 8.0 ın üzerinde olan ilk 50 kaydı alınız.
9- Yayın tarihi 2014-2015 olan filmlerin isimlerini getiriniz.
10- Değerlendirme sayısı (NUm-Reviews) 100.000 den büyük ya da imdb puanı 8 ile 9 arasında olan filmleri listeleyiniz.

"""


result = df  #1
result = df.head() #2
result = df.tail(10) #3

result = df["Movie_Title"] #4
result = df["Movie_Title"].head() #5
result = df[["Movie_Title", "Rating"]].head(1) #6
result = df[5:10][["Movie_Title", "Rating"]] #7

result =df[df["Rating"] >= 8.0][["Movie_Title", "Rating"]].head(50) #8

#print(df.columns)
result = df[(df["YR_Released"] >=2014) & (df["YR_Released"] <=2015)][["Movie_Title", "YR_Released"]] #9

print(result)

