import scrapy
import csv

url = "/workspaces/Web-Scraping-Tool/ParseHub_ Showtimes.html"
class MoviesSpider(scrapy.Spider):
    name = 'movies'
    allowed_domains = ['parsehub.com']
    #start_urls = ['http://parsehub.com/']
    start_urls = [f'file://{url}']

    def parse(self, response):
        rows = []
        column_names =['Movie Title','Show Times']
        movies = response.xpath('//li')[:10]
        try:
            for movie in movies:
             title = movie.xpath('div/span/a/text()').extract()
             show_times= movie.xpath('div/span//div/span/text()').extract()
             rows.append(title+show_times)
             
        except IndexError:
            pass
        
        print(rows)

        csv_file= open('movies.csv', 'w')
        writer= csv.writer(csv_file)
        writer.writerow(column_names)
        writer.writerows(rows)
        csv_file.close()
