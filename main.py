from bs4 import BeautifulSoup
import requests

def sulpak():
    base_url = "https://www.sulpak.kz/f/noutbuki?selectedTagsTokens=1198&page="
    num_pages = 2

    all_macbook_prices = []

    for page in range(1, num_pages + 1):
        url = base_url + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        laptops = soup.find_all("div", class_="products__items products__items-js flex__block")

        macbook_prices = []
        for laptop in laptops:
            name = laptop.find("div", class_="product__item-name")
            if name:
                name_text = name.text.strip()
                if "MacBook" in name_text:
                    price = laptop.find("div", class_="product__item-price").text.strip()
                    macbook_prices.append(float(price.replace(' ', '').replace('₸', '')))

        all_macbook_prices.extend(macbook_prices)

    return all_macbook_prices

def technodom():
    base_url = "https://www.technodom.kz/catalog/noutbuki-i-komp-jutery/noutbuki-i-aksessuary/noutbuki/f/brands/apple?page="
    num_pages = 2

    all_macbook_prices = []

    for page in range(1, num_pages + 1):
        url = base_url + str(page)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        laptops = soup.find_all("ul", class_="ProductList_block__nJTj5 CategoryPageList_productList__zMI0I")

        macbook_prices = []

        for laptop in laptops:
            name = laptop.find("p", class_="Typography ProductCardV_title__U38HX ProductCardV_loading___io2a Typography__M")
            if name:
                name_text = name.text.strip()
                if 'MacBook' in name_text:
                    price = laptop.find("p", class_="Typography ProductCardPrices_price__oCsLy Typography__Subtitle").text.strip()
                    price_cleaned = float(price.replace(' ', '').replace('₸', '').replace('\xa0', '').replace(',', ''))
                    macbook_prices.append(price_cleaned)

        all_macbook_prices.extend(macbook_prices)

    return all_macbook_prices

sulpak_prices = sulpak()
technodom_prices = technodom()

if sulpak_prices and technodom_prices:
    min_sulpak_price = min(sulpak_prices)
    min_technodom_price = min(technodom_prices)

    if min_sulpak_price < min_technodom_price:
        best_price = min_technodom_price
        print(f"Минимальная цена на MacBook на сайте Technodom: {best_price} тенге.")
    elif min_technodom_price < min_sulpak_price:
        best_price = min_sulpak_price
        print(f"Минимальная цена на MacBook на сайте Sulpak: {best_price} тенге.")
    else:
        print(f"Минимальная цена на MacBook на сайте Technodom: {min_sulpak_price} тенге.")
        print(f"Минимальная цена на MacBook на сайте Sulpak: {min_technodom_price} тенге.")
else:
    print("MacBook не найден на одном из сайтов.")
    