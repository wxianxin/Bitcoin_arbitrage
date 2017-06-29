# Author: Steven Wang    Date: 20161011

import btcchina
import time

def order_btc(bc_ask, lc_bid, lb_ask, l_quantity):
# place btc order
    bc_price = bc_ask + 0.5
    lc_price = lc_bid - 0.03
    bc_quantity = l_quantity * lc_bid / bc_ask

    lb_buy_order_id = bc.lbbuy(lb_ask, l_quantity)
    lc_sell_order_id = bc.lcsell(lc_price, l_quantity)                   
    bc_buy_order_id = bc.bcbuy(bc_price, bc_quantity)

    print '\a'
    print "BTC:", l_quantity 
    
    order_file = open("log_order.txt",'a')
    order_file.write(' '.join(["BTC:", str(l_quantity), str(date), str(arbitrage_btc), str(bc_ask), str(lc_bid), str(lb_ask), ' | ', str(bc_buy_order_id), str(lc_sell_order_id), str(lb_buy_order_id), '\n']))
    order_file.close()

def order_ltc(bc_bid, lc_ask, lb_bid, l_quantity):
# place ltc order
    bc_price = bc_bid - 0.5
    lc_price = lc_ask + 0.03
    bc_quantity = l_quantity * lc_ask / bc_bid

    lb_sell_order_id = bc.lbsell(lb_bid, l_quantity)
    bc_sell_order_id = bc.bcsell(bc_price, bc_quantity)
    lc_buy_order_id = bc.lcbuy(lc_price, l_quantity)
    
    print '\a'
    print "LTC:", l_quantity 
    
    order_file = open("log_order.txt",'a')
    order_file.write(' '.join(["LTC:", str(l_quantity), str(date), str(bc_sell_order_id), str(lc_buy_order_id), str(lb_sell_order_id), ' | ', str(arbitrage_ltc), str(bc_bid), str(lc_ask), str(lb_bid), '\n']))
    order_file.close()

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

            print lb_ask, lc_bid, bc_ask, arbitrage_btc,"\t", arbitrage_ltc, bc_bid, lc_ask, lb_bid
        
            if arbitrage_btc >= 1.0018:

                if lb_depth['market_depth']['ask'][0]['amount'] >= 3 and lc_depth['market_depth']['bid'][0]['amount'] >= 3:
                    order_btc(bc_ask, lc_bid, lb_ask, 3)

                elif lb_depth['market_depth']['ask'][0]['amount'] >= 1 and lc_depth['market_depth']['bid'][0]['amount'] >= 1:
                    order_btc(bc_ask, lc_bid, lb_ask, 1)

                order_file = open("logging.txt",'a')
                order_file.write(' '.join(["BTC:", str(date), str(arbitrage_btc), str(bc_ask), str(lc_bid), str(lb_ask), ' | ', str(lb_depth['market_depth']['ask'][0]['amount']), str(lc_depth['market_depth']['bid'][0]['amount']), '\n']))
                order_file.close()
                 

            if arbitrage_ltc >= 1.0018:


                if lb_depth['market_depth']['bid'][0]['amount'] >= 3 and lc_depth['market_depth']['ask'][0]['amount'] >= 3:
                    order_ltc(bc_bid, lc_ask, lb_bid, 3)

                elif lb_depth['market_depth']['bid'][0]['amount'] >= 1 and lc_depth['market_depth']['ask'][0]['amount'] >= 1:
                    order_ltc(bc_bid, lc_ask, lb_bid, 1)

                order_file = open("logging.txt",'a')
                order_file.write(' '.join(["LTC:", str(date), str(arbitrage_ltc), str(bc_bid), str(lc_ask), str(lb_bid), ' | ', str(lb_depth['market_depth']['bid'][0]['amount']), str(lc_depth['market_depth']['ask'][0]['amount']), '\n']))
                order_file.close()

        except:
            file = open("error.txt", 'a')
            file.write(str(i))
            file.close()
            i = i + 1
            bc = btcchina.BTCChina(access_key,secret_key)


if __name__ == '__main__':
    main()
