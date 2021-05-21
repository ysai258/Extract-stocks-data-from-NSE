import requests # FOR WEB SCRAPPING

def extractCookie(url):
    # HEADER TO GET THE DATA FROM GIVEN URL
    header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36','accept-language': 'en-US,en','accept-encoding':'gzip, deflate'}
    # GETTING DATA FOR GIVEN URL WITH GIVEN HEADER
    response = requests.get(url,headers=header)
    return response.cookies.get_dict()     # RETURNING SITE COOKIES IN DICTIONARY FORMAT

def getConnection():
    # GETTING COOKIES FOR NES SITE
    cookie_dict = extractCookie('https://www.nseindia.com/')
    # CREATING SESSION
    session = requests.session()
    # ADDING EACH COOKIE TO THE SESSION
    for cookie in cookie_dict:
        session.cookies.set(cookie,cookie_dict[cookie])
    return session    # RETURNING SESSION

def getData(session,url):
    # HEADER TO GET THE DATA FROM GIVEN URL
    header={'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36','accept-language': 'en-US,en','accept-encoding':'gzip, deflate'}
    # GETTING DATA THROUGH SEESION FOR GIVEN URL WITH HEADER    
    response = session.get(url,headers=header)
    return response.json()     # RETURNING THE JSON (DICTIONARY FORMAT) DATA

def data(company,session):
    # URL WHICH HAS COMPANY PRICE INFO
    url='https://www.nseindia.com/api/quote-equity?symbol='+company
    # GETTING DATA FOR GIVEN URL
    data1=getData(session,url)
    # URL WHICH HAS COMPANY TRADE INFO
    url='https://www.nseindia.com/api/quote-equity?symbol='+company+'&section=trade_info'
    data2=getData(session,url)
    priceInfo = data1['priceInfo']
    sec = data2['securityWiseDP']
    # RETURNING DICTIONARY FOR ASKED VALUES
    return {'Open':priceInfo['open'],'Close':priceInfo['close'],'High':priceInfo['intraDayHighLow']['max'],
    'Low':priceInfo['intraDayHighLow']['min'],'Volume':sec['quantityTraded'],
    'DeliveryData':sec['deliveryQuantity'],'DeliveryPercentage': sec['deliveryToTradedQuantity']}

def func(stocknames):
    l={} # EMPTY DICTIONARY
    session = getConnection() # GETTING CONNECTION TO NSE SITE
    for stock in stocknames: # ACCESSING EACH STOCK
        l[stock]=data(stock,session)  # GETTING REQUIRED DATA FOR THE STOCK
    return l    # RETURNING THE DICTIONARY WITH KEY AS STOCK AND VALUE AS STOCK DATA

#stocks = ['RELIANCE', 'HDFCBANK', 'ADANIPORTS', 'ITC', 'SBIN', 'IOC', 'RBLBANK', 'SBIN']
stocks=[input('Enter company symbol:')]
result = func(stocks)
for stock in result:
    print(stock)
    for data in result[stock]:
        print("\t",data,result[stock][data])
    print()
