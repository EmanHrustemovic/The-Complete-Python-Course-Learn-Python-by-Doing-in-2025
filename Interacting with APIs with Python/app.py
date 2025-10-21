from libs.openexchange import OpenExchangeClient

APP_ID = "5e32d55c26f0400296f850b66cd69aeb"

#ENDPOINT = "https://openexchangerates.org/api/latest.json"

client = OpenExchangeClient(APP_ID)


usd_amount = 1000
gbp_amount = client.convert(usd_amount,"USD","GBP")

print(f"USD {usd_amount} is GBP {gbp_amount}")