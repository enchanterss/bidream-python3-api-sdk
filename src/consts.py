# HTTP HEADER
API_URL = 'https://www.zhuibi.com'
CONTENT_TYPE = 'Content-Type'
ACCESS_KEY = 'ACCESS-KEY'
ACCESS_SIGN = 'ACCESS-SIGN'
ACCESS_PASSPHRASE = 'ACCESS-PASSPHRASE'
ACCESS_TIMESTAMP = 'ACCESS-TIMESTAMP'

ACCEPT = 'Accept'
COOKIE = 'Cookie'
LOCALE = 'Locale='
APPLICATION_JSON = 'application/json'

GET = "GET"
POST = "POST"
DELETE = "DELETE"

# PRIVATE
SPOT_ACCOUNT = '/api/v1/spot/account/assets'
WITHDRAW = '/api/v1/spot/account/withdraw'

SPOT_ORDER = '/api/v1/spot/orders/add'
SPOT_CANCEL_ORDER = '/api/v1/spot/orders/cancel/{symbol}/{orderId}'
SPOT_CANCEL_ORDERS = '/api/v1/spot/orders/cancel'
SPOT_ORDER_INFO = '/api/v1/spot/orders/detail/{symbol}/{orderId}'
SPOT_OPEN_ORDERS_INFO = '/api/v1/spot/orders/open/detail/{symbol}/{side}'
SPOT_HISTORY_ORDERS_INFO = '/api/v1/spot/orders/history/detail/{symbol}/{side}'
SPOT_BANCOR_ORDER = '/api/v1/spot/orders/add-bancor'

# PUBLIC
SPOT_PRODUCTS = '/public/api/v1/products'
SPOT_TICKER = '/api/v1/spot/public/products/'
SPOT_DEPTH = '/api/v1/spot/public/products/'
SPOT_DEAL = '/api/v1/spot/public/products/'
SPOT_KLINE = '/api/v1/spot/public/products/'

SERVER_TIMESTAMP = '/public/api/v1/time'
