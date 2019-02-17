# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

from FARA_scraper.items import FaraScraperItem


lua_script = """

function main(splash, args)
    splash.images_enabled = false
    
    assert(splash:go(splash.args.url))
    splash:wait(1)

    --[[ getting max rows from page (registered principals) --]]
    local pagination_text = splash:select('.pagination > span'):text()
    max_rows = string.sub(pagination_text, 11);
    splash:wait(0.5)

    --[[ uncheck_CountryLocation_Represented_checkmark
    --unchecking this checkmark represents country in the data row (easier to scrape) --]]
    splash:evaljs("javascript:gReport.column.break_toggle(this,'COUNTRY_NAME');")
    splash:wait(5)

    --[[ setting max_rows to 6411, which represents all the data in a database --]]
    splash:evaljs("javascript:gReport.navigate.paginate('pgR_min_row=16max_rows=6411rows_fetched=15')")
    splash:wait(30)

    return {
        html = splash:html(),
        max_rows = tonumber(max_rows)
    }
end

"""

class FARA_scraper(scrapy.Spider):
    name = "FARA_scraper"

    def start_requests(self):
        yield SplashRequest(
            url = 'https://efile.fara.gov/pls/apex/f?p=185:130:0::NO:RP,130:P130_DATERANGE:N', 
            callback = self.parse,
            endpoint = 'execute',
            args = {'lua_source': lua_script, 'timeout': 90},
        )


    def parse(self, response):
        tr = '2'
        
        while(1):
            if tr == response.data['max_rows'] + 2: # max rows from the pagination + 2, because tr starts from '2' 
                break

            tr = str(tr)

            url = 'https://efile.fara.gov/pls/apex/' + response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[1]/a/@href')[0].extract()
            Foreign_Principal = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[2]/text()')[0].extract()
            Foreign_Principal_Registration_Date = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[3]/text()')[0].extract()
            
            if response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()'):
                Address = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()')[0].extract()
            
            if response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()[2]'):
                Address = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()')[0].extract() + ', ' + \
                            response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()[2]')[0].extract()
            
            if response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()[3]'):
                Address = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()')[0].extract() + ', ' + \
                            response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()[2]')[0].extract() + ', ' + \
                            response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[4]/text()[3]')[0].extract()

            if response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[5]/text()'):
                State = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[5]/text()')[0].extract()
            else:
                State = 'null'

            Country_Location_Represented = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[6]/text()')[0].extract()
            Registrant = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[7]/text()')[0].extract()
            Registration_Num = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[8]/text()')[0].extract()
            Registration_Date = response.xpath('//*[@id="555215554758934859"]/tbody/tr[' + tr + ']/td[9]/text()')[0].extract()       
            
            tr = int(tr) + 1


            item = FaraScraperItem()

            item['url'] = url
            item['Foreign_Principal'] = Foreign_Principal
            item['Foreign_Principal_Registration_Date'] = Foreign_Principal_Registration_Date
            item['Address'] = Address.replace(u'\xa0\xa0', u'\xa0').replace(u'\xa0', u' ').strip()
            item['State'] = State
            item['Country_Location_Represented'] = Country_Location_Represented
            item['Registrant'] = Registrant
            item['Registration_Num'] = Registration_Num
            item['Registration_Date'] = Registration_Date

            yield item