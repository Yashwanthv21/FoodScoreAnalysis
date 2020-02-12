# FoodScoreAnalysis
Scrape the Data from EWG Website, combine it with Amazon and Analyze it
 
 ## To run the script
 ```
 cd foodscore\foodscore
 scrapy crawl foodScoreProductURLs -o product_urls.jl
 scrapy crawl foodScoreProductDetails -o product_details.jl
 ```
 
 - The first spider crawls the URL's of all the products and dumps into a file.
 - The second spider reads each URL in the `product_urls.jl` file and crawls the site to get the product information. The result is dumped into `product_dfetails.jl` file.
 
 - Each product detail is scraped and saved as a json for exmaple
 ```
 {
  "product_url": "https://www.ewg.org/foodscores/products/099482453817-365EverydayValueOrganicBlackChiaSeed",
  "product_img": "https://phorcys-static.ewg.org/brand_logo/logos/3215/medium.png?1346374049",
  "categeory": [
    "Home",
    "Grains",
    "Chia",
    "365 Everyday Value"
  ],
  "total_score": "10",
  "product_title": "365 Everyday Value Organic Black Chia Seed",
  "nutrition_score": "1",
  "ingredient_score": "0",
  "processing_score": "1",
  "EWG's Top Findings": [
    [
      "positive",
      "Certified organic product [read more]"
    ],
    [
      "positive",
      "No ingredient concerns identified for this product [read more]"
    ],
    [
      "positive",
      "Does not contain artificial or industrial ingredients [read more]"
    ],
    [
      "positive",
      "Per gram, high in protein [read more]"
    ],
    [
      "positive",
      "Per gram, high in naturally occurring fiber [read more]"
    ],
    [
      "positive",
      "Product has been classified as having low processing concerns"
    ]
  ],
  "EWG Food Reports": [
    [
      "EWG's Good Food On A Tight Budget",
      "https://www.ewg.org/goodfood/"
    ],
    [
      "EWG's Shopper's Guide to Pesticide in Produce",
      "https://www.ewg.org/foodnews/"
    ],
    [
      "Children's Cereal: Sugar by the Pound",
      "https://www.ewg.org/research/childrens-cereals"
    ],
    [
      "Meat Eater's Guide to Climate Change + Health",
      "https://www.ewg.org/meateatersguide/"
    ],
    [
      "How Much is Too Much? Excess Vitamins and Minerals in Food Can Harm Kids' Health",
      "https://www.ewg.org/research/how-much-is-too-much"
    ]
  ],
  "Ingredient List": [
    "ORGANIC BLACK CHIA SEED."
  ],
  "Other Information": [
    [
      "positive",
      "This product is certified organic and, therefore, was produced without the use of synthetic pesticides and fertilizers, and free of genetically engineered ingredients. [read more]"
    ]
  ],
  "calories": "Amount Per 1 Tbsp Calories 60 ",
  "serving_size": "1 Tbsp (1x)",
  "nutrients": {
    "QUICK FACTS:": {
      "Total Fat  3 g": "5.0",
      "Total Carbs  4 g": "1.0",
      "Sugars  0 g": "",
      "Protein  3 g": 0
    },
    "AVOID TOO MUCH:": {
      "Saturated Fat  0 g": "0.0",
      "Trans Fat  0.0g": "",
      "Polyunsaturated Fat  3 g": "",
      "Monounsaturated Fat  0 g": "",
      "Cholesterol  0 mg": "0.0",
      "Sodium  0 mg": "0.0",
      "Added Sugar Ingredients:  none listed": ""
    },
    "NUTRIENTS:": {
      "Dietary Fiber  4 g": "16.0",
      "Vitamin D (no value on present label)": "",
      "Vitamin A": "0.0",
      "Vitamin C": "0.0",
      "Calcium": "6.0",
      "Iron": "6.0",
      "Potassium (no value on present label)": "",
      "Phosphorus": "8.0",
      "Zinc": "4.0",
      "Manganese": "50.0"
    }
  }
}
 ```
 
 This information can be used to further Analyze the script.
