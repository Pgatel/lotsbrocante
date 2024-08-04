from ._anvil_designer import LotsBrocanteTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import pandas as pd

class LotsBrocante(LotsBrocanteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def read_lots(self, path_lots):
    df_list = pd.read_excel(path_lots)
    return df_list

  def Lot_change(self, **event_args):
    """Search in datatable this number"""
    pass

  def Populate_click(self, **event_args):
    path_lot = r'C:\Brocante\Liste des Lots réservés.xlsx'
    lots = self.read_lots(path_lot)
    print(lots)
