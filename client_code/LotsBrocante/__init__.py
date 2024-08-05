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
    # Read the 'Zones' table to update the field 'zone'
    zones = anvil.server.call("get_zone")
    self.zone.items = zones
    # Read the 'LotsBrocante' table to update the field 'lot'
    lots = anvil.server.call("get_lots", self.pair.checked, self.zone.selected_value)
    self.lot.items = lots
    #Read the database to obtain the info related to the number of 'lot'
    d_lot = anvil.server.call("get_lot", self.lot.selected_value)
    self.update_lot(d_lot)

  def update_lot(self, lot):
    self.nom.text = f"{lot['Nom']:40s}"
    self.prenom.text = f"{lot['Prénom']:40s}"
    self.rue.text = f"{lot['Rue']:40s}"
    self.numero.text = f"{lot['Numero']:10s}"
    self.code_postal.text = f"{lot['CodePostal']:10s}"
    self.localite.text = f"{lot['Localité']:40s}"
    
  def lot_change(self, **event_args):
    """Search in datatable this number"""
    d_lot = anvil.server.call("get_lot", self.lot.selected_value)
    self.update_lot(d_lot)

  def populate_click(self, **event_args):
    anvil.server.call("update_lots_brocante")

  def zone_change(self, **event_args):
    """This method is called when an item is selected"""
    lots = anvil.server.call("get_lots", self.pair.checked, self.zone.selected_value)
    self.lot.items = lots
    d_lot = anvil.server.call("get_lot", self.lot.selected_value)
    self.update_lot(d_lot)

  def pair_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    lots = anvil.server.call("get_lots", self.pair.checked, self.zone.selected_value)
    self.lot.items = lots
    d_lot = anvil.server.call("get_lot", self.lot.selected_value)
    self.update_lot(d_lot)
