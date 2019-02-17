# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class FaraScraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    url                                 = scrapy.Field()
    Foreign_Principal                   = scrapy.Field()
    Foreign_Principal_Registration_Date = scrapy.Field()
    Address                             = scrapy.Field()
    State                               = scrapy.Field()
    Country_Location_Represented        = scrapy.Field()
    Registrant                          = scrapy.Field()
    Registration_Num                    = scrapy.Field()
    Registration_Date                   = scrapy.Field()