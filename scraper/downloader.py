import csv
import shutil
import requests


BRANDS = [
  'rolex',
  'audemarspiguet',
  'breitling',
  'iwc',
  'jaegerlecoultre',
  'omega',
  'panerai',
  'patekphilippe',
  'cartier',
  'gucci',
  'seiko',
  'movado',
  'zenith'
]


def download():
    for brand in BRANDS:
        f = open('./data/{}.csv'.format(brand))
        lines = csv.reader(f)
        counter = 0
        for line in lines:
            counter += 1
            url = line[0]
            price = line[1]

            r = requests.get(url, stream=True)
            if r.status_code == 200:
                path = './images/{}-{}-{}.jpg'.format(brand, counter, price)
                with open(path, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)


if __name__ == '__main__':
    download()
