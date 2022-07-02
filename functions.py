from bs4 import BeautifulSoup
import pandas as pd

def write_html(soup, name) :
    with open(f"amazon_{name}.html", "w", encoding = 'utf-8') as file:
        file.write(str(soup))

def read_html(name) :
    with open(f"amazon_{name}.html", "r", encoding = 'utf-8') as file:
        soup = BeautifulSoup(file, "html.parser")
    return soup

def url_parser(pages):
    url_list = []
    for i in range(0, pages):
        url = f"https://www.amazon.in/earpods/s?k=earpods&page={i}&qid=1656743330&ref=sr_pg_{i}"
        url_list.append(url)
    return url_list

def parser(soup):

    titles = soup.findAll('span', {'class': 'a-size-medium a-color-base a-text-normal'})
    review_count = soup.findAll('span', {'class': 'a-size-base s-underline-text'})
    rating = soup.findAll('span', {'class': 'a-icon-alt'})
    
    df_title = []
    df_review = []
    df_rating = []

    for index, (value1, value2, value3) in enumerate(zip(titles, review_count, rating)):
        print(f"Index: {index}, title: {value1.get_text()}  Review Count: {value2.get_text()}  Rating: {value3.get_text()}")
        df_title.append(value1.get_text())
        df_review.append(value2.get_text())
        df_rating.append(value2.get_text())

        dict = {'Title': df_title, 'Review': df_review, 'Rating': df_rating}

        df = pd.DataFrame(dict)
        df.to_csv('data.csv', mode='a', header=False)
        
