import os
from dotenv import load_dotenv

from util import mongodb
from crawling import crawl as cr, navermap

load_dotenv()

def chatWithReviews(name):
    # Search for name in database / naver map
        # Return selected name and link, Check if selected one is correct
    # Crawl reviews, save in database / translate
    # Start chat
    # Get user query, retrieve relevant reviews from database
        # Also return source (url, full text, author, date etc.)
    # synthesize reviews and use GPT-3.5 to generate a response
        # Cite sources
    pass

def main():
    crawling = True
    db = mongodb.DB('ReviewChat')
    tourism_collecgion = db.get_collection('tourism')
    reviews_collection = db.get_collection('reviews')
    item_1 = {
        "item_name" : "Blender",
        "item_price" : 100,
        "item_quantity" : 10
    }
    # collection.insert_one(item_1)
    # data = collection.find_one({'item_name' : 'Blender'}, {'_id': 1})
    # print(data)

    crawl = cr.Crawler()
    page = crawl.get_page()
    while True:
        place = input("Enter place:\n")

        # Go to naver map search result page
        url = navermap.get_map_search_url(place)
        print(url)
        crawl.go_to_page(url)
        name_selector = '#app-root > div > div > div > div:nth-child(6) > div > div.place_section.no_margin.vKA6F > div > div > div.O8qbU.tQY7D > div > a > span.LDgIH'
        navermap.go_to_place_page(page, name_selector)

        # Get information
        place_page_url = page.url
        place_id = navermap.get_map_id(place_page_url)
        print('id', place_id)
        place_info = navermap.get_place_info(page)
        print(place_info)
        # Save place info
        place_obj = {
            'place_id': place_id,
            'name': place_info['name'],
            'type': place_info['place_type'],
            'rating': float(place_info['rating']),
            'other': place_info['other'],
            'url': place_page_url
        }
        tourism_collecgion.insert_one(place_obj)
        print('Saved place info')

        # Get reviews
        review_url = navermap.get_map_review_url(place_id)
        review1_selector = '#app-root > div > div > div > div:nth-child(7) > div:nth-child(2) > div.place_section.lcndr > div.place_section_content > ul > li:nth-child(1) > div.ZZ4OK > a > span.zPfVt'
        name_selector = '#_title > span.Fc1rA'
        crawl.go_to_page(review_url, name_selector)
        reviews = navermap.get_reviews(page, place_obj)
        # Save reviews
        reviews_collection.insert_many(reviews)
        print('Saved reviews')

        # Translate

        # Get blog reviews



if __name__ == "__main__":
    main()