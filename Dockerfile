FROM python:3.8

# Uygulamanızın çalışacağı klasörü oluşturun ve çalışma dizininizi ayarlayın
WORKDIR /app
# Gerekli Python paketlerini yükleyin
COPY requirements.txt .
RUN pip install -r requirements.txt

# Uygulamanızı Docker container'da çalıştırmak için gerekli dosyaları ekleyin
COPY . .

EXPOSE 5000

# Flask uygulamanızın çalıştırılması için gerekli komut
CMD ["python", "restapi.py"]

