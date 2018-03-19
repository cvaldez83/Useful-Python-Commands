import requests
import time
import bs4
#from bs4 import BeautifulSoup as BS

def unitedPrice(URL,depDate,retDate):
    # Date format: 'Apr 1, 2018'
    depTimeSelector = r'#sr_product_ECONOMY_91-2398\7c 875-UA > div > div.price-point.price-point-revised.use-roundtrippricing'
    headers = {
        'Content-Type':'application/x-www-form-urlencoded',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'Host':'www.united.com',
        'Content-Length':'586',
        'Accept-Language': 'en-US,en;q=0.9,es;q=0.8',
        'Referer':'https://www.united.com/ual/en/us/',
    }
    payload = {
        'FareTypes':'lf',
        'hdnMaxAllowedTravelersCount':'9',
        'SearchTypeMain':'roundTrip',
        'autoCompAirportText':'See full airport list',
        'clearHisText':'Clear history',
        'recentsearchLazyload':'True',
        'recentSearchSubmit':'False',
        'recentsearchTripCloning':'True',
        'Origin':'SAN',
        'Destination':'HND',
        'Flexible':'false',
        'CorporateBooking':'false',
        'DepartDate':depDate,
        'ReturnDate':retDate,
        'flexMonth':'3/15/2018',
        'tripLength':'6',
        'NumOfAdults':'1',
        'NumOfSeniors':'0',
        'NumOfChildren04':'0',
        'NumOfChildren03':'0',
        'NumOfChildren02':'0',
        'NumOfChildren01':'0',
        'NumOfInfants':'0',
        'NumOfLapInfants':'0',
        'cabinType':'econ',
        'awardCabinType':'awardEcon',
        'AwardTravel':'false',
        'NonStopOnly':'false',
    }

    res = requests.get(URL, headers=headers, params=payload)
    print('status code: ' + str(res.status_code))
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    print(soup)
    return soup.select(depTimeSelector)
    #return elem[0].text.strip()

unitedURL = 'https://www.united.com/ual/en/us/flight-search/book-a-flight'
unitedPrice(unitedURL,'Apr 1, 2018','May 1, 2018')

