import anvil.files
from anvil.files import data_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import pandas as pd

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
@anvil.server.callable
def update_lots_brocante():
   path_lot = 'Liste des Lots réservés.xlsx'
   print(f"Updating the data table 'LotsBrocante' from {path_lot}")
   df_list = pd.read_excel(data_files[path_lot])
   print(df_list)
