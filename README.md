# Scrapy Test Task: DressLily Hoodies
This is a web scraping project using the Scrapy framework
to scrape information for men's hoodies from the [DressLily](https://www.dresslily.com) website.

## Requirements
- Python 3.7 or higher
- Scrapy framework

## Installation
1. Clone the repository: `git clone https://github.com/L1nk3rrr/dresslily_hoodies_scrap.git`
2. Create environment `python3 -m venv venv`
3. Activate environment `source venv/bin/activate`
4. Install the required packages: `pip3 install -r <your_path>/requirements.txt`

## Usage
To run the spiders and save the scraped data to CSV files, run the following command:

`scrapy crawl reviewsspider`

`scrapy crawl hoodiesspider`

## Output
The output files will be saved in the scraped_data directory.

### Products data
- product_id
- product_url
- name
- discount (%)
- discounted_price (0 if no sale)
- original_price
- total_reviews
- product_info (formatted string, e.g. “Occasion:Daily;Style:Fashion” )
### Reviews data
- product_id
- rating
- timestamp (Unix timestamp)
- text
- size
- color
