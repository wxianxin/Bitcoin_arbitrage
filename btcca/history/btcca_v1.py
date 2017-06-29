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

            print lb_ask, lc_bid, bc_ask, arbitrage_btc,"\t", arbitrage_ltc, bc_bid, lc_ask, lb_bid
        
            if arbitrage_btc >= 1.0018:

                if lb_depth['market_depth']['ask'][0]['amount'] >= 18 and lc_depth['market_depth']['bid'][0]['amount'] >= 18:

                    bc_price = bc_ask + 0.5
                    lc_price = lc_bid - 0.03
                    bc_quantity = 18 * lc_bid / bc_ask

                    lb_buy_order_id = bc.lbbuy(lb_ask, 18)
                    lc_sell_order_id = bc.lcsell(lc_price, 18)                   
                    bc_buy_order_id = bc.bcbuy(bc_price, bc_quantity)
                    
                    
                    print '\a'
                    print '18!!!!!!!!!!!!!'
                    
                    order_file = open('log_order.txt','a')
                    order_file.write(' '.join(['BTC: 18',str(date) ,str(arbitrage_btc), str(lb_ask), str(lc_bid), str(bc_ask), ' | ', str(lb_buy_order_id), str(lc_sell_order_id), str(bc_buy_order_id), '\n']))
                    order_file.close()

                elif lb_depth['market_depth']['ask'][0]['amount'] >= 3 and lc_depth['market_depth']['bid'][0]['amount'] >= 3:

                    bc_price = bc_ask + 0.5
                    lc_price = lc_bid - 0.03
                    bc_quantity = 3 * lc_bid / bc_ask

                    lb_buy_order_id = bc.lbbuy(lb_ask, 3)
                    lc_sell_order_id = bc.lcsell(lc_price, 3)                   
                    bc_buy_order_id = bc.bcbuy(bc_price, bc_quantity)
                    
                    
                    print '\a'
                    print '3!!!!!!!!!!!!!'

                    order_file = open('log_order.txt','a')
                    order_file.write(' '.join(['BTC: 3',str(date) ,str(arbitrage_btc), str(lb_ask), str(lc_bid), str(bc_ask), ' | ', str(lb_buy_order_id), str(lc_sell_order_id), str(bc_buy_order_id), '\n']))
                    order_file.close()                    

            if arbitrage_ltc >= 1.0018:

                if lb_depth['market_depth']['bid'][0]['amount'] >= 18 and lc_depth['market_depth']['ask'][0]['amount'] >= 18:

                    bc_price = bc_bid - 0.5
                    lc_price = lc_ask + 0.03
                    bc_quantity = 18 * lc_ask / bc_bid

                    lb_sell_order_id = bc.lbsell(lb_bid, 18)
                    bc_sell_order_id = bc.bcsell(bc_price, bc_quantity)
                    lc_buy_order_id = bc.lcbuy(lc_price, 18)
                    
                    print '\a'
                    print '18!!!!!!!!!!!!!'
                    
                    order_file = open("xxxxx", 'a')
                    order_file.write(' '.join(['LTC: 18', str(date), str(lb_sell_order_id), str(bc_sell_order_id), str(lc_buy_order_id), ' | ', str(arbitrage_ltc), str(lb_bid), str(bc_bid), str(lc_ask), '\n']))
                    order_file.close()

                elif lb_depth['market_depth']['bid'][0]['amount'] >= 3 and lc_depth['market_depth']['ask'][0]['amount'] >= 3:

                    bc_price = bc_bid - 0.5
                    lc_price = lc_ask + 0.03
                    bc_quantity = 3 * lc_ask / bc_bid

                    lb_sell_order_id = bc.lbsell(lb_bid, 3)
                    bc_sell_order_id = bc.bcsell(bc_price, bc_quantity)
                    lc_buy_order_id = bc.lcbuy(lc_price, 3)
                    
                    print '\a'
                    print '3!!!!!!!!!!!!!'
                    
                    order_file = open("xxxxx", 'a')
                    order_file.write(' '.join(['LTC: 3', str(date), str(lb_sell_order_id), str(bc_sell_order_id), str(lc_buy_order_id), ' | ', str(arbitrage_ltc), str(lb_bid), str(bc_bid), str(lc_ask), '\n']))
                    order_file.close()

        except:
            file = open("xxxxx", 'a')
            file.write(str(i))
            file.close()
            i = i + 1
            bc = btcchina.BTCChina(access_key,secret_key)




if __name__ == '__main__':
    main()


