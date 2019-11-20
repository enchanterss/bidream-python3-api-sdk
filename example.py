# coding=utf-8
from src.spot import Spot


if __name__ == '__main__':

    # input your personal api info
    api_key = ''
    seceret_key = ''
    passphrase = ''

    # make a spot instance
    spot_instance = Spot(api_key, seceret_key, passphrase, True)

    # spot function

    # query account
    # example = spot_instance.get_account()

    # withdraw
    # example = spot_instance.withdraw('usdt', 100, '')

    # order
    example = spot_instance.order('epra_eos', 1, 0, 100, 0.000059)

    # cancel order by ID
    # example = spot_instance.cancel_order('epra_eos', 48638652826640)

    # cancel orders by symbol
    # example = spot_instance.cancel_orders('epra_eos', [48638628238352, 48638610509840])

    # query order by ID
    # example = spot_instance.get_order_info('epra_eos', 48638652826640)
 
    # query open orders by symbol
    # example = spot_instance.get_open_orders_info('epra_eos', 2, 1, 50)

    # query history orders by symbol
    # example = spot_instance.get_history_orders_info('epra_eos', 2, 1, 50)

    # query product
    # example = spot_instance.get_product()

    # query ticker
    # example = spot_instance.get_ticker('epra_eos')

    # query deal
    # example = spot_instance.get_deal('epra_eos', before='', after='', limit='')

    # query k-line
    # example = spot_instance.get_kline('epra_eos', '1min', 1534132800000, 1534150800000)

    # query server-time
    # example = spot_instance.get_time()

    # bancor order
    # example = spot_instance.bancor_order(0, 1, 100)

    print(example)
