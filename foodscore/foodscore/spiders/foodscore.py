import scrapy

class FoodScoreSpider(scrapy.Spider):
    name = "foodscores"
    start_urls = [
        'https://www.ewg.org/foodscores/products?page=1&per_page=5',
    ]

    def parse(self, response):
        total_products = int(response.css('span#span_pagination::text').get().strip().split()[-1].replace(',',''))
        total_products = 5
        page = 1
        products = 0
        products_per_page = 100

        for page,products in enumerate(range(products_per_page, total_products, products_per_page),1):
            url = 'https://www.ewg.org/foodscores/products?page=' + str(page) + '&per_page=' + str(products)
            # print(url)
            yield response.follow(url, callback=self.parse_products)

        if total_products - products > 0:
            url = 'https://www.ewg.org/foodscores/products?page=' + str(page+1) + '&per_page=' + str(total_products - products)
            # print(url)
            yield response.follow(url, callback=self.parse_products)

    def parse_products(self, response):
        # get products
        products = response.css('div#product_ind_result')
        for product in products:
            # Get product Image
            # product_img = product.css('img.img_delete_bg_noshow::attr(src)').get()
            # Get product Categeory
            # product_categeory = product.css('div.product_category_below_link a::attr(href)').get()
            # if product_categeory:
            #     product_categeory = product_categeory.split('=')
            # if product_categeory and len(product_categeory) > 1:
            #     product_categeory = product_categeory[1]
            # # Get product URL
            product_url = product.css('a.nounderlineahref::attr(href)').get()
            if product_url is not None:
                product_url = response.urljoin(product_url)
            # print('_'*20)

            yield {
                    'url': product_url,
                }