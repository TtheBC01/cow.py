# Constants and conversion factors
methanedensitystp = 0.0007168 # kg/L at standard temperature and pressure
joulesperkgofmethan = 50000000 # J/kg
methanegeneratorefficiency = 0.36 # percent
numberofsecondsinaday = 60*60*24 # seconds
numberofhoursinamonth = 24*30 # hours
mathaneyieldperkg = 216 # 160 to 216 L/kg
kgofwasteperday = 133*0.453592 # 85 to 133 kg/day

# What is the methane production rate of a cow per day
methanvolumepercowperday = kgofwasteperday*mathaneyieldperkg # L/(cow-day)
kgofmethanepercowday = methanvolumepercowperday*methanedensitystp # kg/(cow-day)
print(f'kg of methane per day: {kgofmethanepercowday} kg/day')

# What is the power output of a cow from RNG
cowenergyperday = kgofmethanepercowday*joulesperkgofmethan*methanegeneratorefficiency # J/day
cowwatts = (cowenergyperday)/numberofsecondsinaday
print(f'MJ of energy per day: {cowenergyperday/1000000} MJ/day')
print(f'Cow Watts: {cowwatts} W/cow')

# What are the per-block energy requiremnets of the Bitcoin network
energypertransaction = 1720 # kWh/tx
transactionsperblock = 1800 # txs
mWhperblock = energypertransaction*transactionsperblock/1000 # mWh
print(f'Bitcoin MW per block: {mWhperblock} BTC/MWh')

# What are the unit economics of the Bitcoin network
blockreward = 6.25 # BTC/block
priceperbitcoin = 20000 # USD
dollarsperblock = blockreward*priceperbitcoin # USD/block
dollarsperWh = dollarsperblock/(mWhperblock*1000000)
print(f'$ per Wh: {dollarsperWh} $/Wh')

# What can a cow expect to earn from RNG based electricity production from Bitcoin mining
profitpercowpermonth = dollarsperWh*cowwatts*numberofhoursinamonth
print(f'Cow earnings per month: ${profitpercowpermonth}')
print(f'Conservative earnings per month: ${profitpercowpermonth*0.8*0.8}')
print(f'Cow earnings per year: ${profitpercowpermonth*12}')
print(f'Conservative earnings per year: ${profitpercowpermonth*12*0.8*0.8}')