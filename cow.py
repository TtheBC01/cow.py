kgmethanepercowpermonth = 0.453592*10 # kg/(cow*month)
joulesperkgofmethan = 50000000 # J/kg
methanegeneratorefficiency = 0.36 # percent
numberofsecondsinamonth = 60*60*24*30 # seconds
numberofcows = 100 # cows

cowenergypermonth = kgmethanepercowpermonth*joulesperkgofmethan*methanegeneratorefficiency # J/Month
cowwatts = (cowenergypermonth)/numberofsecondsinamonth

print(cowenergypermonth/1000000)
print(cowwatts)

energypertransaction = 1720 # kWh/tx
transactionsperblock = 1800 # txs
mWhperblock = energypertransaction*transactionsperblock/1000 # mWh

print(mWhperblock)

blockreward = 6.25 # BTC/block
priceperbitcoin = 20000 # USD
dollarsperblock = blockreward*priceperbitcoin # USD/block

dollarsperWh = dollarsperblock/(mWhperblock*1000000)
print(dollarsperWh)

profitpercowpermonth = dollarsperWh*cowwatts*numberofsecondsinamonth
print(profitpercowpermonth)