# Author: Steven Wang    Date: 20160823
# python 2.7.12

import btcchina
import time


def main():

# Initilize everything

    access_key=raw_input("access key: ")
    secret_key=raw_input("secret key: ")

    bc = btcchina.BTCChina(access_key,secret_key)
    result = bc.get_account_info()
    print result

###################################################################################
    i = 0
    while True:

        try:
            bc_depth = bc.get_bcmarket_depth2()
            lc_depth = bc.get_lcmarket_depth2()
            lb_depth = bc.get_lbmarket_depth2()

            bc_ask = bc_depth['market_depth']['ask'][0]['price']
            lc_bid = lc_depth['market_depth']['bid'][0]['price']
            lb_ask = lb_depth['market_depth']['ask'][0]['price']
            arbitrage_btc = 1.0 / lb_ask * lc_bid / bc_ask

            bc_ask_1 = bc_depth['market_depth']['ask'][1]['price']
            lc_bid_1 = lc_depth['market_depth']['bid'][1]['price']
            lb_ask_1 = lb_depth['market_depth']['ask'][1]['price']
            arbitrage_btc_1 = 1.0 / lb_ask_1 * lc_bid_1 / bc_ask_1

            lb_bid = lb_depth['market_depth']['bid'][0]['price']
            bc_bid = bc_depth['market_depth']['bid'][0]['price']
            lc_ask = lc_depth['market_depth']['ask'][0]['price']
            arbitrage_ltc = lb_bid * bc_bid / lc_ask

            lb_bid_1 = lb_depth['market_depth']['bid'][1]['price']
            bc_bid_1 = bc_depth['market_depth']['bid'][1]['price']
            lc_ask_1 = lc_depth['market_depth']['ask'][1]['price']
            arbitrage_ltc_1 = lb_bid_1 * bc_bid_1 / lc_ask_1

            date = bc_depth['market_depth']['date']

            order_file = open("logging.txt",'a')
            order_file.write(' '.join(["BTC:", str(date), str(arbitrage_btc), str(bc_ask), str(lc_bid), str(lb_ask), ' | ', str(lb_depth['market_depth']['ask'][0]['amount']), str(lc_depth['market_depth']['bid'][0]['amount']), '\n']))
            order_file.close()

            print lb_ask, lc_bid, bc_ask, arbitrage_btc,"\t", arbitrage_ltc, bc_bid, lc_ask, lb_bid


        
            if arbitrage_btc >= 1:

                order_file = open("logging.txt",'a')
                order_file.write(' '.join(["BTC:", str(date), str(arbitrage_btc), str(bc_ask), str(lc_bid), str(lb_ask), ' | ', str(lb_depth['market_depth']['ask'][0]['amount']), str(lc_depth['market_depth']['bid'][0]['amount']), '\n']))
                order_file.close()
                print 'done'

                 

            if arbitrage_ltc >= 1:

                order_file = open("logging.txt",'a')
                order_file.write(' '.join(["LTC:", str(date), str(arbitrage_ltc), str(bc_bid), str(lc_ask), str(lb_bid), str(lb_depth['market_depth']['bid'][0]['amount']), str(lc_depth['market_depth']['ask'][0]['amount']), '\n']))
                order_file.close()
                print 'done'


        except:
            file = open("error.txt", 'a')
            file.write(str(i))
            file.close()
            i = i + 1
            bc = btcchina.BTCChina(access_key,secret_key)


if __name__ == '__main__':
    main()

