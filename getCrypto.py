import pandas_datareader as web
import numpy as np
import pandas as pd
import datetime as dt
from datetime import timedelta


kode_saham="DOGE-USD"
data_api="yahoo"
mulai=dt.datetime(2020,1,1)
if dt.datetime.today().weekday()==5 :
    akhir=dt.datetime.today()- timedelta(days=2)
    prediksi=dt.datetime.today()- timedelta(days=1)
elif dt.datetime.today().weekday()==6 :
    akhir=dt.datetime.today()- timedelta(days=3)
    prediksi=dt.datetime.today()- timedelta(days=2)
else:
    akhir=dt.datetime.today()- timedelta(days=1)
    prediksi=dt.datetime.today()
df=web.DataReader(kode_saham,data_source=data_api,start=mulai,end=akhir)
df.to_csv(f"{kode_saham}.csv")
