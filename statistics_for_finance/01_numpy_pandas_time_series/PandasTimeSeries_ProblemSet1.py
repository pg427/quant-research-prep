import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

SP_read = pd.read_csv("GSPC.csv", sep=",", parse_dates=True, index_col='Date', header=0)
SP_close = SP_read['Close']
print(SP_close.head())
# SP_returns_log = 100 * np.log(SP_close/SP_close.shift())
# print(SP_returns_log.head())

''' S&P 500 NET RETURNS'''
SP_returns_net = 100 * ((SP_close - SP_close.shift())/SP_close.shift())
print(SP_returns_net.head())
# SP_returns_net.plot()
# plt.show()

''' S&P 500 - 1990s, 2000s, 2008 NET RETURNS'''
SP_close_1990s = SP_close["1990-01-01":"1999-12-31"]
SP_close_2000s = SP_close["2000-01-01":"2007-12-31"]
SP_close_2008 = SP_close["2008-01-01":"2008-12-31"]

SP_returns_net_1990s = 100 * ((SP_close_1990s - SP_close_1990s.shift())/SP_close_1990s.shift())
SP_returns_net_2000s = 100 * ((SP_close_2000s - SP_close_2000s.shift())/SP_close_2000s.shift())
SP_returns_net_2008 = 100 * ((SP_close_2008 - SP_close_2008.shift())/SP_close_2008.shift())

fig, axes = plt.subplots(3, 1, figsize=(12, 9), sharey=True)
axes[0].plot(SP_returns_net_1990s.dropna())
axes[0].set_title("1990s S&P 500 Net Returns")

axes[1].plot(SP_returns_net_2000s.dropna())
axes[1].set_title("2000s S&P 500 Net Returns")

axes[2].plot(SP_returns_net_2008.dropna())
axes[2].set_title("2008 S&P 500 Net Returns")

plt.tight_layout()
plt.show()