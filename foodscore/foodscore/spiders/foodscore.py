import scrapy

class FoodScoreSpider(scrapy.Spider):
    name = "foodscores"
    start_urls = [
        'https://www.ewg.org/foodscores/products?page=1&per_page=5',
    ]

    def parse(self, response):
        # get products
        a = response.css('div#product_ind_result')
        for e in a:
            # Get product URL
            print(e.css('a.nounderlineahref::attr(href)').get())
            # Get product Image
            print(e.css('img.img_delete_bg_noshow::attr(src)').get())
            # Get product Categeory
            print(e.css('div.product_category_below_link a::attr(href)').get())
            print('_'*20)

        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href, self.parse)

    def parse_product_details(self, response):

        # Get Total Score
        print(response.css('div.updated_score img::attr(src)').get())
        # Get Title of Product
        print(response.css('h1.truncate_title_specific_product_page::text').get())
        # Get Nutrition Score
        print(response.css('div#dial_for_nutrition img.gage_2_bg_img::attr(src)').get())
        # Get Hazard/Ingredient Score
        print(response.css('div#dial_for_hazard img.gage_2_bg_img::attr(src)').get())
        # Get Processing Score
        print(response.css('div#dial_for_processing img.gage_2_bg_img::attr(src)').get())

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }