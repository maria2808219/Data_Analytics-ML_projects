import requests
from bs4 import BeautifulSoup
import json
import csv

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}

# for i in range(1, 12):
#     url = 'https://gemini.pl/kategoria/zdrowie/witaminy-i-mineraly/witaminy/witamina-d?page=' + str(i) + '&sort=price_desc'
#     req = requests.get(url, headers=headers)
#     src = req.text
#     with open('page' + str(i) + '.html', "w", encoding="utf-8") as file:
#         file.write(src)
#
# all_categories_gict = {}
#
# for i in range(1, 12):
#     page_name = 'page' + str(i) + '.html'
#     with open(page_name, encoding="utf-8") as file:
#         src = file.read()
#     soup = BeautifulSoup(src, 'lxml')
#     all_products_hrefs = soup.find_all(class_='absolute inset-0 z-10')
#     for item in all_products_hrefs:
#         item_text = item['title']
#         item_link = 'https://gemini.pl' + item['href']
#
#         all_categories_gict[item_text] = item_link
#
# new_path = open("all_categories_gict.csv", "w", encoding="utf-8")
# z = csv.writer(new_path)
# for new_k, new_v in all_categories_gict.items():
#     z.writerow([new_k, new_v])
# new_path.close()
#
# with open('all_categories_gict.json', 'w', encoding="utf-8") as file:
#     json.dump(all_categories_gict, file, indent=4, ensure_ascii=False)


with open("all_categories_gict.json", encoding="utf-8") as file:
    all_categories = json.load(file)

with open("final_data.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file, lineterminator="\r", delimiter=';')
    writer.writerow(
        (
            'product_name',
            'product_ingredients',
            'manufacturer',
            'distributor',
            'age',
            'product_character',
            'product_key_ingredients',
            'product_price',
            'product_price_for_volume'
        )
    )
n = 0
product_information = []
for product_name, product_link in all_categories.items():
    req = requests.get(url=product_link, headers=headers)
    src = req.text
    soup = BeautifulSoup(src, 'lxml')

    product_name = soup.find(class_='text-19 my-2 text-black').get_text().strip()
    product_info = soup.find_all(class_='text-19 mb-2 font-bold text-black')
    categories = []

    for category in product_info:
      categories.append(category.get_text().strip())

    if 'Inne wersje tego produktu' in categories:
        categories.remove('Inne wersje tego produktu')

    product_info1 = soup.find_all(class_='text-14 text-black scroll-spy-section')

    if 'Składniki' in categories:
        index = categories.index('Składniki')
        product_ingredients = product_info1[index].get_text().strip().replace('\n', ' ')
    else:
        product_ingredients = 'Brak informacji'

    if 'Producent' in categories:
        index = categories.index('Producent')
        manufacturer = product_info1[index].get_text().strip().replace('\n', ' ')
    else:
        manufacturer = 'Brak informacji'

    if 'Dystrybutor' in categories:
        index = categories.index('Dystrybutor')
        distributor = product_info1[index].get_text().strip().replace('\n', ' ')
    else:
        distributor = 'Brak informacji'

    product_info2 = soup.find_all(class_='break-words')[0].find_all(class_='block text-black underline cursor-pointer hover:text-primary-action')
    age = ''
    for info in product_info2:
        age += info.get_text().strip() + ', '

    product_character = soup.find_all(class_='break-words')[1].find(class_='block text-black underline cursor-pointer hover:text-primary-action').get_text().strip().replace('\n', ' ')

    product_key_ingredients_info = soup.find_all(class_='break-words')[2].find_all(class_='block text-black underline cursor-pointer hover:text-primary-action')
    product_key_ingredients = ''
    for key_ingredient in product_key_ingredients_info:
        product_key_ingredients += key_ingredient.get_text().strip() + ', '

    product_price = soup.find(class_='font-bold text-primary mr-2 text-14').get_text().strip().replace('\n', ' ')

    product_price_for_volume = soup.find_all(class_='text-14 text-black')[-1].get_text().strip().replace('\n', ' ')

    with open("final_data.csv", "a", encoding="utf-8") as file:
        writer = csv.writer(file, lineterminator="\r", delimiter=';')
        writer.writerow(
            (
                product_name,
                product_ingredients,
                manufacturer,
                distributor,
                age,
                product_character,
                product_key_ingredients,
                product_price,
                product_price_for_volume)
        )
    product_information.append(
        {
            'product_name': product_name,
            'product_ingredients': product_ingredients,
            'manufacturer': manufacturer,
            'distributor': distributor,
            'age': age,
            'product_character': product_character,
            'product_key_ingredients': product_key_ingredients,
            'product_price': product_price,
            'product_price_for_volume': product_price_for_volume
        }
    )

    n += 1
    print(f'Product #{n} is successfully appending')

with open('final_data.json', "a", encoding="utf-8") as file:
    json.dump(product_information, file, indent=4, ensure_ascii=False)