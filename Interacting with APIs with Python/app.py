import time

from libs.openexchange import OpenExchangeClient

APP_ID = "5e32d55c26f0400296f850b66cd69aeb"

#ENDPOINT = "https://openexchangerates.org/api/latest.json"

client = OpenExchangeClient(APP_ID)


usd_amount = 1000
start_time = time.time()
gbp_amount = client.convert(usd_amount,"USD","GBP")
end_time = time.time()

print(f"Start time is : {start_time}")
print(f"End time is : {end_time}")
print(f"USD {usd_amount} is GBP {gbp_amount}")
print(f"Total time needed : {end_time - start_time}")