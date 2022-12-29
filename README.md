# Economics of Mining Bitcoin with Cow Manure

The prospect of mining cryptocurrency with renewable energy is an intriguing  idea, particularly if the renewable energy is free of monetary cost. 
Consider mining Bitcoin via renewable natural gas (RNG), i.e. methane from cow manure. 

According to the [Agricultural Waste Management Field Handbook](https://directives.sc.egov.usda.gov/viewerFS.aspx?hid=21430), a cow can produce between
[`85` and `133` pounds of waste per day](https://directives.sc.egov.usda.gov/OpenNonWebContent.aspx?content=31475.wba) based on a normalized *animal unit* of `1000` lbs (i.e. every `1000` lbs of bovine live stock produces between `85` and `133` lbs of manure per day). Furthermore, research suggests that cow manure 
outgases between [`160` and `216` L of methane per kg of manure](https://www.researchgate.net/publication/324976649_Biogas_Production_from_Different_Types_of_Cow_Manure#:~:text=The%20methane%20yield%20was%20found,%2Fkg%20VS). This equates to `4.4` to `6.9` kg of methane gas production per day assuming the density of methane at [standard temperature and pressure is `0.72` g/L](https://www.engineeringtoolbox.com/methane-d_1420.html). A kilogram of methane gas contains approximately
[`50`MJ of energy](https://world-nuclear.org/information-library/facts-and-figures/heat-values-of-various-fuels.aspx). Modern methane-based electric generators
can operate at a thermodynamic  efficiency in the [range of `36%`](https://www.yanmar.com/global/about/technology/technical_review/2016/0727_1.html#:~:text=The%20BP%2DG%20power%20generation,23.3MJ%2FNm3). Assuming `86400` seconds in a day, a cow produces approximately `921` to `1441` Watts (J/s) of usable
electric power from RNG. 

A Bitcoin transaction is estimated to require [approximately `1720` kWh](https://www.coindesk.com/business/2021/08/18/how-much-energy-does-bitcoin-use/) of energy to confirm. Based on current network activity, there are typically [`1800` transactions per block](https://www.blockchain.com/charts/n-transactions-per-block) mined in the Bitcoin network.  Therefore, a block requires, on average, `3096` MWh of energy to mine. 

The current block reward in the Bitcoin network is [`6.25` BTC per block](https://www.investopedia.com/bitcoin-halving-4843769#:~:text=As%20of%202022%2C%20Bitcoin%20miners,the%20block%20reward%20approaches%20zero.). As of 9/14/2022, the price of BTC is around
[`$20,000` USD](https://www.coindesk.com/price/bitcoin/). So, a new block is worth at least `$125,000` USD plus transaction fees associated with the 
mined transactions which are currently negligible in comparison to the block reward. This is equivalent to saying the Bitcoin network
pays ~`$0.00004037` per Watt-hour to secure the network. 

If a cow produces ~`80` to `124` MJ of usable (i.e. accounting for generator efficiency) energy per day in the form of RNG, and said cow is paid fair market rate from the Bitcoin network for its RNG-based electric output, the cow should earn about `$25` to`$55` per month. If you assume a `20` percent reduction in output due to 
various parasitic losses in RNG capture and conversion to electricity as well an additional `20` percent reduction due to unplanned outages, downtime due to 
upgrades, etc., then the cow's conservative earning potential is in the ballpark of `$17` to `$25` per month. See [cow.py](/cow.py) for calculations. 
