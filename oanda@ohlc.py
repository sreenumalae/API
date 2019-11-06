import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import pandas as pd

access_token = "7eef1883be46e194de1f66c57d5ccbdb-75f84221ab7ea27e7067a4f462d4eeaa"

client = oandapyV20.API(access_token=access_token)

params ={"count": 5000,"granularity": "M5"}
r = instruments.InstrumentsCandles(instrument="DE30_EUR",params=params)
client.request(r)

out=[]
out=pd.DataFrame(r.response['candles'])
df=pd.DataFrame(out)
print(df['mid'])

objs = [df['mid'], pd.DataFrame(df['mid'].tolist()).iloc[:, :4]]
df2 = pd.concat(objs, axis=1).drop('mid', axis=1)
df2['time'] = df['time']
df2['volume'] = df['volume']
df2.columns=['Open','High','Low','Close','Timestamp','volume']
print(df2)
