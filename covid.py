import pandas as pd  
from datetime import datetime as dt  

df_eda = pd.read_csv(
    "https://raw.githubusercontent.com/JJTorresDS/ds-data-sources/main/covid_data_raw.csv"
)

df_eda["Date_reported"] = pd.to_datetime(
    df_eda["Date_reported"]
)
df_eda["FIRST_VACCINE_DATE"] = pd.to_datetime(
    df_eda["FIRST_VACCINE_DATE"]
)

df_eda["days_since_vaccine"] = (
    df_eda["Date_reported"] - df_eda["FIRST_VACCINE_DATE"]
).dt.days

df_eda["vaccination_started"] = df_eda["days_since_vaccine"].apply(
    lambda x: "Yes" if x >= 0 else "No"
)

print(df_eda.head())