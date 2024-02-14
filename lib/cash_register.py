#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0, total=0, items=[]):
      self.discount = discount
      self.total = total
      self.items = items

  @property
  def discount(self):
      return self._discount
  
  @discount.setter
  def discount(self, discount):
      self._discount = discount
  
  @property
  def total(self):
      return self._total
  
  @total.setter
  def total(self, total):
      self._total = total  

  @property
  def items(self):
      return self._items
  
  @items.setter
  def items(self, items):
      self._items = items

