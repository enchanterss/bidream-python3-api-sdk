# API接口说明

---
## PRIVATE API
- 币币账户信息
```python
get_account(self)
```
- 提币
```python
withdraw(self, currencyCode, amount, address, memo)
```
- 下单
```python
order(self, symbol, side, atype, size, price, source=1)
```
- 撤销指定订单
```python
cancel_order(self, symbol, orderId)
```
- 批量撤销订单
```python
cancel_orders(self, symbol, orderId)
```
- 获取指定订单
```python
get_order_info(self, symbol, orderId)
```
- 批量获取未成交订单
```python
get_open_orders_info(self, side, symbol, page, rows)
```
- 批量获取已成交订单
```python
get_history_orders_info(self, side, symbol, page, rows)
```
- bancor下单
```python
bancor_order(self, product_id, side, size, source=1)
```

## PUBLIC API
- 获取币对信息
```python
get_product(self)
```
- ~~获取Ticker信息~~
```python
get_ticker(self, code)
```
- ~~获取深度数据~~
```python
get_depth(self, code)
```
- ~~获取成交数据~~
```python
get_deal(self, code, before='', after='', limit='')
```
- ~~获取K线数据~~
```python
get_kline(self, code, start, end, atype)
```
- 获取服务器时间
```python
get_time(self)
```

