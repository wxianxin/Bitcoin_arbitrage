# Author: Steven Wang    Date: 20160706
# python 2.7.12
# No real performance gain

import threading
import btcchina

class bcDepth(btcchina.BTCChina, threading.Thread):
    def __init__(self,access,secret):
        btcchina.BTCChina.__init__(self,access,secret)
        threading.Thread.__init__(self)

    def run(self):
        bc_depth = self.get_market_depth2("btccny")
        bc_ask = bc_depth['market_depth']['ask'][0]['price']
        print 'bc_ask =', bc_ask

class lcDepth(btcchina.BTCChina, threading.Thread):
    def __init__(self,access,secret):
        btcchina.BTCChina.__init__(self,access,secret)
        threading.Thread.__init__(self)

    def run(self):
        lc_depth = self.get_market_depth2("ltccny")
        lc_ask = lc_depth['market_depth']['ask'][0]['price']
        print 'lc_ask =', lc_ask


class lbDepth(btcchina.BTCChina, threading.Thread):
    def __init__(self,access,secret):
        btcchina.BTCChina.__init__(self,access,secret)
        threading.Thread.__init__(self)

    def run(self):
        lb_depth = self.get_market_depth2("ltcbtc")
        lb_ask = lb_depth['market_depth']['ask'][0]['price']
        print 'lb_ask =', lb_ask

def main():

    access_key=raw_input("access key: ")
    secret_key=raw_input("secret key: ")

    bc = bcDepth(access_key,secret_key)
    lc = lcDepth(access_key,secret_key)
    lb = lbDepth(access_key,secret_key)

    result = bc.get_account_info()
    print result

    global bc_depth
    global lc_depth
    global lb_depth
    global bc_ask
    global lc_ask
    global lb_ask

    bc_depth = bc.get_market_depth2("btccny")
    lc_depth = bc.get_market_depth2("ltccny")
    lb_depth = bc.get_market_depth2("ltcbtc")
    bc_ask = bc_depth['market_depth']['ask'][0]['price']
    bc_bid = bc_depth['market_depth']['bid'][0]['price']
    lc_ask = lc_depth['market_depth']['ask'][0]['price']
    lc_bid = lc_depth['market_depth']['bid'][0]['price']
    lb_ask = lb_depth['market_depth']['ask'][0]['price']
    lb_bid = lb_depth['market_depth']['bid'][0]['price']

    i = 1
    while True:
 #       try:
            bc.start()
            lc.start()
            lb.start()
            bc.join()
            lc.join()
            lb.join()


#            arbitrage_btc = 1.0 / lb_ask * lc_bid / bc_ask
            '''
            if arbitrage_btc > 1.002 and lb_depth['market_depth']['ask'][0]['amount'] >= 5:
                order_file = open('order.txt','a')
                order_file.write('1')
                order_file.close()
                
                lb_buy_order_id = bc.lbbuy(0.0001,0.01)
                lc_sell_order_id = bc.lcsell(10000,0.001)
                bc_buy_order_id = bc.bcbuy(0.01,0.001)
                
                order_file = open('order.txt','a')
                order_file.write(' '.join([str(date), str(lb_buy_order_id), str(lc_sell_order_id), str(bc_buy_order_id)]))
                order_file.close()
            '''
            #print arbitrage_btc
'''
        except:
            file = open("text.txt", 'a')
            file.write(str(i))
            file.close()
            i = i + 1
            bc = bcDepth(access_key,secret_key)
            if i > 10:
                break
'''

#    x = raw_input('wait')


if __name__ == '__main__':
    main()