import scrapy
from bs4 import BeautifulSoup
import json
from scrapy.http import Request


class FoodScoreSpider(scrapy.Spider):
    name = "foodscores12"
    start_urls = [
        'https://www.ewg.org/foodscores/products?page=1&per_page=5',
    ]

    def parse(self, response):
        # get products
        with open('product_urls.jl') as f:
            for line in f:
                product = json.loads(line)
                product_url = product['url']
                if product_url is not None:
                    # print(product_url)
                    # print('-'*25)
                    yield Request(product_url, self.parse_product_details)

    def parse_product_details(self, response):

        product_data = {}
        # Get Page URL
        product_data['product_url'] =  response.request.url
        # Product Image
        product_data['product_img'] = response.css('img.img_delete_bg_noshow::attr(src)').get()
        # Get Categeory
        product_data['categeory'] = response.css('div#breadcrumbs a::text').getall()
        # Get Total Score
        product_data['total_score'] = response.css('div.updated_score img::attr(src)').get().split('score')[1].split('-')[0].replace('_','')
        # Get Title of Product
        product_data['product_title'] = response.css('h1.truncate_title_specific_product_page::text').get()
        # Get Nutrition Score
        product_data['nutrition_score'] = response.css('div#dial_for_nutrition img.gage_2_bg_img::attr(src)').get().split('scores')[1].split('-')[0].split('_')[1]
        # Get Hazard/Ingredient Score
        product_data['ingredient_score'] = response.css('div#dial_for_hazard img.gage_2_bg_img::attr(src)').get().split('scores')[1].split('-')[0].split('_')[1]
        # Get Processing Score
        product_data['processing_score'] = response.css('div#dial_for_processing img.gage_2_bg_img::attr(src)').get().split('scores')[1].split('-')[0].split('_')[1]

        soup = BeautifulSoup(response.body, "lxml")
        # get all boxes.
        boxes = soup.find_all('div', class_='bottom_space')
        for box in boxes:
            if box.find('h1').text == "EWG's Top Findings" or box.find('h1').text == 'Other Information':
                product_data[box.find('h1').text] = box_data = []
                p = box.find_all('p')
                sent = ''
                for item in p:
                    if 'neutral' in item.img['src']:
                        sent = 'neutral'
                    elif 'negative' in item.img['src']:
                        sent = 'negative'
                    elif 'positive' in item.img['src']:
                        sent = 'positive'
                    box_data.append([sent, item.get_text().strip()])

            elif box.find('h1').text == 'EWG Food Reports':
                product_data[box.find('h1').text] = box_data = []
                p = box.find_all('p')
                for item in p:
                    box_data.append([item.find('a').text, item.a['href']])

            elif box.find('h1').text == 'Ingredient List': 
                product_data[box.find('h1').text] = box_data = []   
                p = box.find('p').text
                box_data.append(p)

            elif box.find('h1').text == 'Selected Certifications and Seals':
                product_data[box.find('h1').text] = box_data = []
                p = box.find_all('p')
                for item in p:
                    box_data.append(item.text.strip())

        nut = soup.find('table', class_='performance-facts__table')

        # get the calories
        cal_box = nut.find('thead').find_all('th')
        product_data['calories'] = ' '.join(list(map(lambda x: getattr(x, 'text').strip(), cal_box)))

        #get the serving size
        serving_size = soup.find('option',selected=True)
        if serving_size:
            product_data['serving_size'] = serving_size.text

        # nutrients value
        facts = nut.find('tbody').find('tbody')
        rows = facts.find_all('tr')
        product_data['nutrients'] = data = {}
        curr_dict = None
        for row in rows:
            if row.find('th'):
                #start new section
                data[row.find('th').text.strip()] = curr_dict = {}
            else:
                cols = row.find_all('td')
                n = map(lambda x: getattr(x,'text').strip(),cols)
                left, right = list(n)
                if left:
                    left = left.split('\n')
                    if len(left) > 1:
                        left = left[1]
                    else:
                        left = 0
                right = right.replace('\n',' ')
                curr_dict[right] = left

        yield product_data