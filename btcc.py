# Author: Steven Wang    Date:20160630
# Python 3.5.2

def ltcbtc_arbitrage():

    from urllib.request import urlopen
    import json

    data = urlopen('https://data.btcchina.com/data/ticker?market=all')
    json_data = json.loads(data.read().decode("utf-8"))

    date = json_data['ticker_btccny']['date']

    btccny_buy= json_data['ticker_btccny']['buy']
    btccny_sell= json_data['ticker_btccny']['sell']
    ltccny_buy= json_data['ticker_ltccny']['buy']
    ltccny_sell= json_data['ticker_ltccny']['sell']
    ltcbtc_buy= json_data['ticker_ltcbtc']['buy']
    ltcbtc_sell= json_data['ticker_ltcbtc']['sell']

    arbitrage_0 = 1.0 / float(ltcbtc_sell) * float(ltccny_buy) / float(btccny_sell)
    arbitrage_1 = float(ltcbtc_buy) * float(btccny_buy) / float(ltccny_sell)

    ''' 
    print (date)
    print (arbitrage_0, '\t |', btccny_sell, '\t |', ltccny_buy, '\t |', ltcbtc_sell)
    print (arbitrage_1, '\t |', btccny_buy, '\t |', ltccny_sell, '\t |', ltcbtc_buy)
    print ('-----------------------------------------------------------------')
    '''
    print(str(ltcbtc_sell), str(ltccny_buy), str(btccny_sell), str(arbitrage_0), str(arbitrage_1), str(btccny_buy), str(ltccny_sell), str(ltcbtc_buy))

    if arbitrage_0 > 1.0018:
        print('\a')
        file = open('log.txt','a')
        file.write(' '.join(['0:',str(date) ,str(arbitrage_0), btccny_sell, ltccny_buy, ltcbtc_sell, '\n']))
        file.close()
    if arbitrage_1 > 1.0018:
        print('\a')
        file = open('log.txt','a')
        file.write(' '.join(['1:',str(date) ,str(arbitrage_1), btccny_buy, ltccny_sell, ltcbtc_buy, '\n']))
        file.close()

while (1):
	ltcbtc_arbitrage()