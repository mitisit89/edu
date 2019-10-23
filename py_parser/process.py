import json
import csv



def main():
    items=json.load(open('items.json','rt'))['items']
    with open('items.csv',"w",encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(['Заголовок','Цена','Ссыллка'])
        for item  in items:
            writer.writerow([item['title'],item['price'],item['url']])
if __name__ == '__main__':
    main()
