import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
from pandas import DataFrame

@anvil.server.callable
def get_zone():
  l_zone = [row['zone'] for row in app_tables.zones.search()]
  print(l_zone)
  return l_zone

@anvil.server.callable
def get_lots(pair, zone):
  print(f'Pair:{pair}; zone:{zone}')
  filtered = app_tables.lotsbrocante.search(Zone=zone)
  print(filtered)
  return ['A024', 'A026']

@anvil.server.callable
def update_lots_brocante():
  path_lot = data_files['Liste des Lots réservés.xlsx']
  print(f"Updating the data table 'LotsBrocante' from {path_lot}")
  lots = pd.read_excel(path_lot)

  app_tables.lotsbrocante.delete_all_rows()
  for t_lot in lots.iterrows():
    lot = t_lot[1]
    if pd.isna(lot['Prénom']):
      lot['Prénom'] = ''
    if pd.isna(lot['Numero']):
      lot['Numero'] = ''
    if pd.isna(lot['Rue']):
      lot['Rue'] = ''
    if pd.isna(lot['Localité']):
      lot['Localité'] = ''
    if pd.isna(lot['Code Postal']):
      lot['Code Postal'] = ''
    print(lot)
    app_tables.lotsbrocante.add_row(Nom=lot['Nom'], Prénom=lot['Prénom'], NumeroLot=lot['No Lot'],
                                   Rue=lot['Rue'], Numero=lot['Numero'], Code_Postal=lot['Code Postal'],
                                   Localité=lot['Localité'], Zone=lot['Zone'], Facade=lot['Facade'],
                                   Profondeur=lot['Profondeur'], Surface=lot['Surface'])
  
  zones = lots[['Zone']].groupby('Zone').first().index
  df_zones = DataFrame(zones)
  zones_pair = df_zones[df_zones['Zone'].str.contains(' pair')].values.tolist()
  s_zone_pair = [str(z[0])[:2].strip() for z in zones_pair]
  
  app_tables.zones.delete_all_rows()
  for zone in s_zone_pair:
    app_tables.zones.add_row(zone=zone)
