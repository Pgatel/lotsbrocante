from ._anvil_designer import LotsBrocanteTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LotsBrocante(LotsBrocanteTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def Lot_change(self, **event_args):
    """Search in datatable this number"""
    pass
