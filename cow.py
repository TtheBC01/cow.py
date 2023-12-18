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
    # What are the per-block energy requirements of the Bitcoin network
    transactions_per_block = 1800 # txs per block default value
    btc_tx_per_block_request = await pyfetch(url="https://blockchain.info/q/avgtxnumber", method="GET")
    if btc_tx_per_block_request.status == 200:
        print("Successfully got BTC tx per block")
        transactions_per_block = await btc_tx_per_block_request.json()
    else:
        print("Failed to fetch current btc tx per block")

    energy_per_transaction = 1780 # kWh/tx
    setElement("#kwhpertx",energy_per_transaction)
    setElement("#txperblock",transactions_per_block)
    mWh_per_block = energy_per_transaction*transactions_per_block/1000 # kWh/tx*tx/block*mWh/kWw = mWh/block
    setElement("#mwhperblock", mWh_per_block)
    print(f'Bitcoin MW per block: {mWh_per_block} BTC/MWh')

    print("Fetching price from CoinGecko")
    CoinGeckoBTCPrice = await pyfetch(url="https://api.coingecko.com/api/v3/simple/price?ids=binance-bitcoin&vs_currencies=usd", method="GET")
    btc_price = 1
    if CoinGeckoBTCPrice.status == 200:
        print("Successfully got BTC price from CoinGecko")
        priceJSON = await CoinGeckoBTCPrice.json()
        btc_price = priceJSON['binance-bitcoin']['usd']
        setElement("#btcspotprice", btc_price)
    else:
        print("Failed to fetch current BTC price from CoinGecko")
    
    # What are the unit economics of the Bitcoin network
    block_reward = 6.25 # default BTC/block
    btc_block_reward_request = await pyfetch(url="https://blockchain.info/q/bcperblock", method="GET")
    if btc_block_reward_request.status == 200:
        print("Successfully got BTC block reward")
        block_reward = await btc_block_reward_request.json()
    else:
        print("Failed to fetch current btc block reward")

    dollars_per_block = block_reward*btc_price # btc/block*$/btc = $/block
    dollars_per_Wh = dollars_per_block/(mWh_per_block*1000000) # $/block*block/mWh = $/mWh*Wh/mWh
    setElement("#blockreward", block_reward)
    setElement("#dollarsperblock", dollars_per_block) 
    setElement("#dollarsperwatt", dollars_per_Wh)
    print(f'$ per Wh: {dollars_per_Wh} $/Wh')
    
    # What can a cow expect to earn from RNG based electricity production from Bitcoin mining
    min_profit_per_cow_per_month = dollars_per_Wh*min_cow_watts*number_of_hours_in_a_month
    max_profit_per_cow_per_month = dollars_per_Wh*max_cow_watts*number_of_hours_in_a_month
    min_conservative_profit_per_cow_per_month = min_profit_per_cow_per_month*(1-parasitic_loss)*(1-downtime_loss)
    max_conservative_profit_per_cow_per_month = max_profit_per_cow_per_month*(1-parasitic_loss)*(1-downtime_loss)
    setElement("#mincowmonthlyearnings",min_profit_per_cow_per_month)
    setElement("#maxcowmonthlyearnings",max_profit_per_cow_per_month)
    setElement("#minconservativemonthlyearnings",min_conservative_profit_per_cow_per_month)
    setElement("#maxconservativemonthlyearnings",max_conservative_profit_per_cow_per_month)
    print(f'Min Cow earnings per month: ${min_profit_per_cow_per_month}')
    print(f'Max Cow earnings per month: ${max_profit_per_cow_per_month}')
    print(f'Min Conservative earnings per month: ${min_conservative_profit_per_cow_per_month}')
    print(f'Max Conservative earnings per month: ${max_conservative_profit_per_cow_per_month}')
    print(f'Min Cow earnings per year: ${min_profit_per_cow_per_month*12}')
    print(f'Max Cow earnings per year: ${max_profit_per_cow_per_month*12}')
    print(f'Min Conservative earnings per year: ${min_conservative_profit_per_cow_per_month*12}')
    print(f'Max Conservative earnings per year: ${max_conservative_profit_per_cow_per_month*12}')


# Constants and conversion factors
parasitic_loss = 0.3 # parasitic loss assumption in RNG capture and electrical conversion
downtime_loss = 0.2 # loss due to unexpected downtime and network outages
methane_density_stp = 0.0007168 # kg/L at standard temperature and pressure
joules_per_kg_of_methane = 50000000 # J/kg
methane_generator_efficiency = 0.36 # percent
number_of_seconds_in_a_day = 60*60*24 # seconds
number_of_hours_in_a_month = 24*30 # hours
min_methane_yield_per_kg = 160 # L/kg
max_methane_yield_per_kg = 216 # L/kg
min_lbs_of_waste_per_day = 85 # lbs/day
max_lbs_of_waste_per_day = 133 # lbs/day
min_kg_of_waste_per_day = min_lbs_of_waste_per_day*0.453592 # kg/day
max_kg_of_waste_per_day = max_lbs_of_waste_per_day*0.453592 # kg/day

setElement("#parasiticloss",parasitic_loss*100)
setElement("#downtimeloss", downtime_loss*100)

setElement("#minkgwaste1", min_lbs_of_waste_per_day)
setElement("#minkgwaste2", min_lbs_of_waste_per_day)
print(f'Min KG Waste: {min_kg_of_waste_per_day}')

setElement("#maxkgwaste1", max_lbs_of_waste_per_day)
setElement("#maxkgwaste2", max_lbs_of_waste_per_day)
print(f'Max KG Waste: {max_kg_of_waste_per_day}')

# What is the methane production rate of a cow per day
setElement("#minmethaneyield", min_methane_yield_per_kg)
setElement("#maxmethaneyield", max_methane_yield_per_kg)
print(f'Min KG of methane per day: {min_methane_yield_per_kg} kg/day')
print(f'Max KG of methane per day: {max_methane_yield_per_kg} kg/day')

min_methane_volume_per_cow_per_day = min_kg_of_waste_per_day*min_methane_yield_per_kg; # kg/day*L/kg = L/day
min_methane_kg_per_cow_per_day = min_methane_volume_per_cow_per_day*methane_density_stp # L/day*kg/L = kg/day
setElement("#minkgproduction", min_methane_kg_per_cow_per_day)
print(f'Min L/Day Methane per Cow: {min_methane_volume_per_cow_per_day}')

max_methane_volume_per_cow_per_day = max_kg_of_waste_per_day*max_methane_yield_per_kg;
max_methane_kg_per_cow_per_day = max_methane_volume_per_cow_per_day*methane_density_stp
setElement("#maxkgproduction", max_methane_kg_per_cow_per_day)
print(f'Max L/Day Methane per Cow: {max_methane_volume_per_cow_per_day}')

setElement("#methanedensitystp", methane_density_stp*1000) # g/L
setElement("#generatorefficiency", methane_generator_efficiency*100) 

# What is the power output of a cow from RNG
# kg/(cow-day)*j/kg*day/s=j/(cow-s)
min_cow_energy_per_day = min_methane_kg_per_cow_per_day*joules_per_kg_of_methane*methane_generator_efficiency # kg/day*J/kg = J/day
max_cow_energy_per_day = max_methane_kg_per_cow_per_day*joules_per_kg_of_methane*methane_generator_efficiency # kg/day*J/kg = J/day
min_cow_mj_per_month = min_cow_energy_per_day*30/1000000
max_cow_mj_per_month = max_cow_energy_per_day*30/1000000
setElement("#mincowmegajoulesperday",min_cow_energy_per_day/1000000)
setElement("#maxcowmegajoulesperday",max_cow_energy_per_day/1000000)
min_cow_watts = (min_cow_energy_per_day)/number_of_seconds_in_a_day #J/day*day/sec = J/sec
max_cow_watts = (max_cow_energy_per_day)/number_of_seconds_in_a_day
setElement("#mincowjoulespersecond", min_cow_watts) 
setElement("#maxcowjoulesjpersecond", max_cow_watts)
print(f'Min MJ of energy per day: {min_cow_energy_per_day/1000000} MJ/day')
print(f'Max MJ of energy per day: {max_cow_energy_per_day/1000000} MJ/day')
print(f'Min Cow Watts: {min_cow_watts} W/cow')
print(f'Max Cow Watts: {max_cow_watts} W/cow')

# get the price of BTC now from CoinGecko
loop = asyncio.get_event_loop()
loop.run_until_complete(getBTCPrice())