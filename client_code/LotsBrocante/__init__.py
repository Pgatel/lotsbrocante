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
    b_pair = self.pair_impair.selected_value == 'Pair'
    lots = anvil.server.call("get_lots", b_pair, self.zone.selected_value)
    self.lot.items = lots
    if not self.populate.visible:
      #Read the database to obtain the info related to the number of 'lot'
      d_lot = anvil.server.call("get_lot", self.lot.selected_value)
      self.update_lot(d_lot)
    self.i_lot = 0
    self.back.enabled = False

  def update_lot(self, lot):
    self.nom.text = f" {lot['Nom']:32s} "
    self.prenom.text = f" {lot['Prénom']:28s} "
    self.rue.text = f" {lot['Rue']:50s} "
    self.numero.text = f" {lot['Numero']:13s} "
    self.code_postal.text = f" {lot['CodePostal']:18s} "
    self.localite.text = f" {lot['Localité']:42s} "
    self.facade.text = f" {lot['Facade']:4.1f}m "
    self.profondeur.text = f"{lot['Profondeur']:4.1f}m "
    self.surface.text = f" {lot['Surface']:5.1f}m² "
    self.lots_samedi.text = f"S:{lot['LotsSamedi']} "
    self.lots_dimanche.text = f"D:{lot['LotsDimanche']} "
    
  def lot_change(self, **event_args):
    """Search in datatable this number"""
    s_lot = self.lot.selected_value
    d_lot = anvil.server.call("get_lot", s_lot)
    self.i_lot = self.lot.items.index(s_lot)
    if self.i_lot == 0:
      self.back.enabled = False
    else:
      self.back.enabled = True
    if self.i_lot == len(self.lot.items) - 1:
      self.forward.enabled = False
    else:
      self.forward.enabled = True

    self.update_lot(d_lot)

  def populate_click(self, **event_args):
    anvil.server.call("update_lots_brocante")

  def zone_change(self, **event_args):
    """This method is called when an item is selected"""
    b_pair = self.pair_impair.selected_value == 'Pair'
    lots = anvil.server.call("get_lots", b_pair, self.zone.selected_value)
    self.lot.items = lots
    d_lot = anvil.server.call("get_lot", self.lot.selected_value)
    self.i_lot = 0
    self.back.enabled = False
    self.update_lot(d_lot)

  def pair_impair_change(self, **event_args):
    """This method is called when this checkbox is checked or unchecked"""
    b_pair = self.pair_impair.selected_value == 'Pair'
    lots = anvil.server.call("get_lots", b_pair, self.zone.selected_value)
    self.lot.items = lots
    self.i_lot = 0
    self.back.enabled = False
    d_lot = anvil.server.call("get_lot", self.lot.selected_value)
    self.update_lot(d_lot)

  def back_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.i_lot > 0:
      self.i_lot -= 1
      s_lot = self.lot.items[self.i_lot]
      self.lot.selected_value = s_lot
      self.lot_change()

  def forward_click(self, **event_args):
    """This method is called when the button is clicked"""
    if self.i_lot < len(self.lot.items) - 1:
      self.i_lot += 1
      s_lot = self.lot.items[self.i_lot]
      self.lot.selected_value = s_lot
      self.lot_change()
