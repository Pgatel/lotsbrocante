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
  return l_zone

# Read the 'LotsBrocante' table and return the lots corresponding to the 'zone' + 'Pair/impair'
# Used to update the comboBox 'lot'
@anvil.server.callable
def get_lots(pair, zone):
  if pair:
    filter = f'{zone} pair'
  else:
    filter = f'{zone} impair'
  filtered = app_tables.lotsbrocante.search(Zone=filter)
  l_lots = [row['NumeroLot'] for row in filtered]
  return l_lots

# Read the 'LotsBrocante' table and return the lot corresponding to 'numero'
@anvil.server.callable
def get_lot(numero_lot):
  f_lot = app_tables.lotsbrocante.search(NumeroLot=numero_lot)[0]
  d_return = {'Nom': f_lot['Nom'], 'Prénom': f_lot['Prénom'], 'Rue': f_lot['Rue'],
              'Numero': f_lot['Numero'], 'CodePostal': f_lot['Code_Postal'], 'Localité': f_lot['Localité'],
              'Facade': f_lot['Facade'], 'Profondeur': f_lot['Profondeur'], 'Surface': f_lot['Surface'],
              'LotsSamedi': f_lot['LotsSamedi'], 'LotsDimanche': f_lot['LotsDimanche']}
  return d_return

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
    if pd.isna(lot['ListeLotSamedi']):
      lot['ListeLotSamedi'] = ''
    if pd.isna(lot['ListeLotDimanche']):
      lot['ListeLotDimanche'] = ''

    app_tables.lotsbrocante.add_row(Nom=lot['Nom'], Prénom=lot['Prénom'], NumeroLot=lot['No Lot'],
                                    Rue=lot['Rue'], Numero=lot['Numero'], Code_Postal=lot['Code Postal'],
                                    Localité=lot['Localité'], Zone=lot['Zone'], Facade=lot['Facade'],
                                    Profondeur=lot['Profondeur'], Surface=lot['Surface'],
                                    LotsSamedi=lot['ListeLotSamedi'], LotsDimanche=lot['ListeLotDimanche'])
  
  zones = lots[['Zone']].groupby('Zone').first().index
  df_zones = DataFrame(zones)
  zones_pair = df_zones[df_zones['Zone'].str.contains(' pair')].values.tolist()
  s_zone_pair = [str(z[0])[:2].strip() for z in zones_pair]
  
  app_tables.zones.delete_all_rows()
  for zone in s_zone_pair:
    app_tables.zones.add_row(zone=zone)
