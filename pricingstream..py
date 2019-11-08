import oandapyV20
import json
from oandapyV20 import API
import oandapyV20.endpoints.pricing as pricing
import pandas as pd
accountID = "101-004-12651949-001"

access_token = "2baa657cc0c681808581c9560bfad0ea-b3a8e6f020f09e5a4d1425ed812c99da"

api = API(access_token= access_token)
params ={
          "instruments": "EUR_USD,EUR_JPY"
        }
r = pricing.PricingStream(accountID=accountID, params=params)
rv = api.request(r)
maxrecs = 100
for ticks in rv:
    print(json.dumps(ticks, indent=4),",")
    if maxrecs == 0:
        r.terminate("maxrecs records received")
