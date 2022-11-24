import fxcmpy

con = fxcmpy.fxcmpy('7d11ae11911f15db8a75fc88c330b93ea72b233f', log_level='error', server='demo')
pair = 'EUR/USD'

data = con.get_candles(pair, period='m5', number=250)



#%%
