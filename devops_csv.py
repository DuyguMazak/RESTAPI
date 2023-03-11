import pandas as pd
from pymongo import MongoClient

#Veritabanı bağlantısını oluşturur.
client= MongoClient('mongodb://localhost:27017/')

#Veritabanı ve koleksiyon oluşturur.
db= client['london_houses']
collection=db['houses']

#CSV dosyasını yükleme
df=pd.read_csv('London.csv')

#Verileri MongoDB'ye aktar
data=df.to_dict(orient='records')
#print(data)
collection.insert_many(data)
#print(result.inserted_ids)
#Bu kod, CSV dosyanızı yükler, verileri pandas dataframe'e dönüştürür ve sonra verileri MongoDB'ye aktarır.

