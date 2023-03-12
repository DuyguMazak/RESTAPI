from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import json_util
import json
app = Flask(__name__)

# MongoDB veritabanına bağlanmak için kullanılacak bağlantı URL'si
MONGO_URI = 'mongodb://localhost:27017/london_houses'

# MongoClient sınıfı ile MongoDB sunucusuna bağlanma
client = MongoClient(MONGO_URI)

# Veritabanına erişim
db = client['london_houses']

# 'houses' koleksiyonunu seçme
houses = db['houses']

# PUT yöntemi
@app.route('/houses', methods=['PUT'])
def add_house():
    data = request.get_json()  # İstek gövdesinden verileri al
    houses.insert_one(data)   # Verileri 'houses' koleksiyonuna ekle
    return jsonify({'message': 'Data added successfully!'})

# GET yöntemi
@app.route('/houses', methods=['GET'])
def get_houses():
    data = request.args.to_dict()  # İstek parametrelerini sözlük olarak al
    results = houses.find(data)    # Verileri filtreleyerek 'houses' koleksiyonundan al
    houses_list = [house for house in results]  # Koleksiyonu liste haline getir
    return jsonify({'data': json.loads(json_util.dumps(houses_list))})


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
