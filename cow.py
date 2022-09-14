methanedensitystp = 0.0007168 # kg/L
kgmethanepercowpermonth = 0.453592*10 # kg/(cow*month)
joulesperkgofmethan = 50000000 # J/kg
methanegeneratorefficiency = 0.36 # percent
numberofsecondsinaday = 60*60*24 # seconds
numberofhoursinamonth = 24*30 # hours
numberofsecondsinamonth = 60*60*numberofhoursinamonth # seconds
mathaneyieldperkg = 160 # - 216 L/kg
kgofwasteperday = 85*0.453592 # kg/day

methanvolumepercowperday = kgofwasteperday*mathaneyieldperkg # L/(cow-day)
kgofmethanepercowday = methanvolumepercowperday*methanedensitystp # kg/(cow-day)
print("kg of methane per day:", kgofmethanepercowday)

cowenergyperday = kgofmethanepercowday*joulesperkgofmethan*methanegeneratorefficiency # J/day
cowwatts = (cowenergyperday)/numberofsecondsinaday

print("MJ of energy per day:", cowenergyperday/1000000)
print("Cow Watts:", cowwatts)

energypertransaction = 1720 # kWh/tx
transactionsperblock = 1800 # txs
mWhperblock = energypertransaction*transactionsperblock/1000 # mWh

print("Bitcoin MW per block:", mWhperblock)

blockreward = 6.25 # BTC/block
priceperbitcoin = 20000 # USD
dollarsperblock = blockreward*priceperbitcoin # USD/block

dollarsperWh = dollarsperblock/(mWhperblock*1000000)
print("$ per Wh:", dollarsperWh)

profitpercowpermonth = dollarsperWh*cowwatts*numberofhoursinamonth
print("Cow earnings per month:", profitpercowpermonth)