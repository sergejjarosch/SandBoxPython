import pandas as pd


berlin = pd.read_csv('open-meteo-berlin.csv', parse_dates=['time'])

anomalien = berlin[(berlin['time'].dt.month >= 9) | (berlin['time'].dt.month <= 4)]
anomalien = anomalien[anomalien['temperature'] > 36]

max_temp_anomalien = anomalien.groupby(anomalien['time'].dt.strftime('%Y-%m'))['temperature'].max().reset_index()
max_temp_anomalien.to_csv('anomalien.csv', index=False)

for index, row in anomalien.iterrows():
    prev_row = berlin.loc[index - 1]
    berlin.loc[(berlin['time'] == row['time']), 'temperature'] = prev_row['temperature']

berlin.to_csv('open-meteo-berlin.csv', index=False)

warme_zeiten = berlin[berlin['temperature'] > 30]
warme_zeiten.to_csv('warme-zeiten.csv', index=False)
warme_monate = warme_zeiten['time'].dt.month.unique()

print(f"Die Temperatur war über 15 Grad in den folgenden Monaten: {warme_monate}")