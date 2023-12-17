from pyscript import document
from datetime import date
from pyodide.http import pyfetch
import asyncio

date_element = document.querySelector("#date")
today = date.today()
date_element.innerText = today.__str__();
print(f'Date: {today}')

def setElement(elemID, value):
    my_element = document.querySelector(elemID)
    my_element.innerText = value

async def getBTCPrice():
    print("Fetching price from CoinGecko")
    CoinGeckoBTCPrice = await pyfetch(url="https://api.coingecko.com/api/v3/simple/price?ids=binance-bitcoin&vs_currencies=usd", method="GET")
    print(CoinGeckoBTCPrice)
    btc_price = 1
    if CoinGeckoBTCPrice.status == 200:
        print("Successfully got BTC price from CoinGecko")
        priceJSON = await CoinGeckoBTCPrice.json()
        btc_price = priceJSON['binance-bitcoin']['usd']
        setElement("#btcspotprice", btc_price)
    else:
        print("Failed to get BTC price from CoinGecko")
    
    # What are the unit economics of the Bitcoin network
    blockreward = 6.25 # BTC/block
    dollarsperblock = blockreward*btc_price # USD/block
    dollarsperWh = dollarsperblock/(mWhperblock*1000000)
    setElement("#dollarsperblock", blockreward*btc_price)
    setElement("#dollarsperwatt", dollarsperblock/(mWhperblock*1000000))
    print(f'$ per Wh: {dollarsperWh} $/Wh')
    
    # What can a cow expect to earn from RNG based electricity production from Bitcoin mining
    profitpercowpermonth = dollarsperWh*cowwatts*numberofhoursinamonth
    print(f'Cow earnings per month: ${profitpercowpermonth}')
    print(f'Conservative earnings per month: ${profitpercowpermonth*0.8*0.8}')
    print(f'Cow earnings per year: ${profitpercowpermonth*12}')
    print(f'Conservative earnings per year: ${profitpercowpermonth*12*0.8*0.8}')


# Constants and conversion factors
methanedensitystp = 0.0007168 # kg/L at standard temperature and pressure
joulesperkgofmethan = 50000000 # J/kg
methanegeneratorefficiency = 0.36 # percent
numberofsecondsinaday = 60*60*24 # seconds
numberofhoursinamonth = 24*30 # hours
mathaneyieldperkg = 216 # 160 to 216 L/kg
min_methane_yield_per_kg = 160 # 160 to 216 L/kg
max_methane_yield_per_kg = 216 # 160 to 216 L/kg
min_kg_of_waste_per_day = 85 # 85 to 133 kg/day
max_kg_of_waste_per_day = 133 # 85 to 133 kg/day
kgofwasteperday = 133*0.453592 # 85 to 133 kg/day

setElement("#minkgwaste1", min_kg_of_waste_per_day)
setElement("#minkgwaste2", min_kg_of_waste_per_day)
print(f'Min KG Waste: {min_kg_of_waste_per_day}')

setElement("#maxkgwaste1", max_kg_of_waste_per_day)
setElement("#maxkgwaste2", max_kg_of_waste_per_day)
print(f'Max KG Waste: {max_kg_of_waste_per_day}')

# What is the methane production rate of a cow per day
setElement("#minmethaneyield", min_methane_yield_per_kg)
setElement("#maxmethaneyield", max_methane_yield_per_kg)
print(f'Min KG of methane per day: {min_methane_yield_per_kg} kg/day')
print(f'Max KG of methane per day: {max_methane_yield_per_kg} kg/day')

min_methane_volume_per_cow_per_day = min_kg_of_waste_per_day*min_methane_yield_per_kg;
min_methane_kg_per_cow_per_day = min_methane_volume_per_cow_per_day*methanedensitystp
setElement("#minkgproduction", min_methane_kg_per_cow_per_day)

max_methane_volume_per_cow_per_day = max_kg_of_waste_per_day*max_methane_yield_per_kg;
max_methane_kg_per_cow_per_day = max_methane_volume_per_cow_per_day*methanedensitystp
setElement("#maxkgproduction", max_methane_kg_per_cow_per_day)

setElement("#methanedensitystp", methanedensitystp*1000) # g/L
setElement("#generatorefficiency", methanegeneratorefficiency*100) 
methanvolumepercowperday = kgofwasteperday*mathaneyieldperkg # L/(cow-day)
kgofmethanepercowday = methanvolumepercowperday*methanedensitystp # kg/(cow-day)

# What is the power output of a cow from RNG
setElement("#mincowjoules", min_methane_kg_per_cow_per_day*joulesperkgofmethan*methanegeneratorefficiency/numberofsecondsinaday) #j/day
setElement("#maxcowjoules", max_methane_kg_per_cow_per_day*joulesperkgofmethan*methanegeneratorefficiency/numberofsecondsinaday) #j/day
cowenergyperday = kgofmethanepercowday*joulesperkgofmethan*methanegeneratorefficiency # J/day
cowwatts = (cowenergyperday)/numberofsecondsinaday
print(f'MJ of energy per day: {cowenergyperday/1000000} MJ/day')
print(f'Cow Watts: {cowwatts} W/cow')

# What are the per-block energy requirements of the Bitcoin network
energypertransaction = 1720 # kWh/tx
transactionsperblock = 1800 # txs
mWhperblock = energypertransaction*transactionsperblock/1000 # mWh
print(f'Bitcoin MW per block: {mWhperblock} BTC/MWh')

# get the price of BTC now from CoinGecko
loop = asyncio.get_event_loop()
thing = loop.run_until_complete(getBTCPrice())