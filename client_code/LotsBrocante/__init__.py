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

  def lot_change(self, **event_args):
    """Search in datatable this number"""
    pass

  def populate_click(self, **event_args):
    anvil.server.call("update_lots_brocante")

  def zone_change(self, **event_args):
    """This method is called when an item is selected"""
    pass

  def pair_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    pass
