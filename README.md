# Python3 scrapy-splash parser example

## Parses Foreign Agents Registration Act (FARA) for all [Active Foreign Principals by Country or Location](https://efile.fara.gov/pls/apex/f?p=185:130:0::NO:RP,130:P130_DATERANGE:N).

Instructions: 
(I tested it only for Ubuntu 18.04, for lower versions of Ubuntu you may need to install python3)

0. Get docker:

`sudo apt-get update && sudo apt-get install docker.io`

1. Run splash docker image 
(Downloading docker image if there is no such image):

`sudo docker run -p 8050:8050 scrapinghub/splash`

2. Open new terminal and install pip3:

`sudo apt-get update && sudo apt-get install python3-pip`

3. Then install virtualenv using pip3:

`sudo pip3 install virtualenv`

4. Create a virtual environment:

`cd Desktop && virtualenv -p /usr/bin/python3 venv`

5. Activate your virtual environment:

`source venv/bin/activate`

6. Install Scrapy and scrapy-splash from source code:

`pip install scrapy && pip install scrapy-splash`

7. *Run main.py in FARA_scraper folder:

`cd FARA_scraper/FARA_scraper/ && python main.py`

7. *OR run the same command from the terminal

`scrapy crawl 'FARA_scraper'`

*After that items.json file will be created (or modified) at FARA_scraper/items.json
