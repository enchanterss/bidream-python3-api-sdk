from .client import Client
from .consts import *


class Spot(Client):

    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, api_url=API_URL):
        Client.__init__(self, api_key, api_secret_key, passphrase, use_server_time, api_url)

    # query account
    def get_account(self):
        return self._request_without_params(GET, SPOT_ACCOUNT)

    # withdraw
    def withdraw(self, currencyCode, amount, address, memo):
        params = {'currencyCode': currencyCode, 'amount': amount, 'address': address, 'memo': memo}
        return self._request_with_params(POST, WITHDRAW, params)

    # order
    def order(self, symbol, side, atype, size, price, source=1):
        params = {'symbol': symbol, 'side': side, 'type': atype, 'size': size, 'price': price, 'source': source}
        return self._request_with_params(POST, SPOT_ORDER, params)

    # cancel order by ID
    def cancel_order(self, symbol, orderId):
        return self._request_without_params(DELETE, SPOT_CANCEL_ORDER.format(symbol=symbol, orderId=orderId))

    # cancel orders by symbol
    def cancel_orders(self, symbol, orderId):
        params = {'symbol': symbol, 'orderId': orderId}
        return self._request_with_params(DELETE, SPOT_CANCEL_ORDERS, params)

    # query order by ID
    def get_order_info(self, symbol, orderId):
        return self._request_without_params(GET, SPOT_ORDER_INFO.format(symbol=symbol, orderId=orderId))

    # query open orders by symbol
    def get_open_orders_info(self, symbol, side, page, rows):
        params = {'page': page, 'rows': rows}
        return self._request_with_params(POST, SPOT_OPEN_ORDERS_INFO.format(symbol=symbol, side=side), params)

    # query history orders by symbol
    def get_history_orders_info(self, symbol, side, page, rows):
        params = {'page': page, 'rows': rows}
        return self._request_with_params(POST, SPOT_HISTORY_ORDERS_INFO.format(symbol=symbol, side=side), params)

    # query product
    def get_product(self):
        return self._request_without_params(GET, SPOT_PRODUCTS)

    # query ticker
    def get_ticker(self, code):
        return self._request_without_params(GET, SPOT_TICKER + str(code) + '/ticker')

    # query depth
    # def get_depth(self, code):
    #     return self._request_without_params(GET, SPOT_DEPTH + str(code) + '/orderbook')

    # query deal
    def get_deal(self, code, before='', after='', limit=''):
        params = {'before': before, 'after': after, 'limit': limit}
        return self._request_with_params(GET, SPOT_DEAL + str(code) + '/fills', params, cursor=True)

    # query k-line
    def get_kline(self, code, atype, start, end):
        params = {'type': atype, 'start': start, 'end': end}
        return self._request_with_params(GET, SPOT_KLINE + str(code) + '/candles', params)

    # query server-time
    def get_time(self):
        return self._request_without_params(GET, SERVER_TIMESTAMP)

    # bancor order
    def bancor_order(self, product_id, side, size, source=1):
        params = {'product_id': product_id, 'order_side': side, 'order_size': size, 'source': source}
        return self._request_with_params(POST, SPOT_BANCOR_ORDER, params)


