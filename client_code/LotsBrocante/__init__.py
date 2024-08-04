from ._anvil_designer import LotsBrocanteTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LotsBrocante(LotsBrocanteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

  def Lot_change(self, **event_args):
    """Search in datatable this number"""
    pass

  def Populate_click(self, **event_args):
    anvil.server.call("update_lots_brocante")
