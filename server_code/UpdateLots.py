import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd
from pandas import DataFrame

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
for zone in app_tables.zones:
  print(Zone)
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def update_lots_brocante():
  path_lot = data_files['Liste des Lots réservés.xlsx']
  print(f"Updating the data table 'LotsBrocante' from {path_lot}")
  lots = pd.read_excel(path_lot)
  zones = lots[['Zone']].groupby('Zone').first().index
  df_zones = DataFrame(zones)
  zones_pair = df_zones[df_zones['Zone'].str.contains(' pair')].values.tolist()
  s_zone_pair = [str(z[0])[:2].strip() for z in zones_pair]
  app_tables.zones.delete_all_rows()
  for zone in s_zone_pair:
    print(zone)
    app_tables.zones.add_row(Zone=zone)
