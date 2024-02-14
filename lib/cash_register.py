#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      # self.quantity = quantity

  # @property
  # def discount(self):
  #     return self._discount
  
  # @discount.setter
  # def discount(self, discount):
  #     self._discount = discount
  
  # @property
  # def total(self):
  #     return self._total
  
  # @total.setter
  # def total(self, total):
  #     self._total = total  

  # @property
  # def items(self):
  #     return self._items
  
  # @items.setter
  # def items(self, items):
  #     self._items = items

  # @property
  # def quantity(self):
  #     return self._quantity
  
  # @quantity.setter
  # def quantity(self, quantity):
  #     self._quantity = quantity

  def add_item(self, title, price, quantity=0):
      # breakpoint()
      # self.items.append(title)
      if quantity > 0:
        x = range(quantity)
        breakpoint()
        for q in x:
          self.items.append(title)
        self.total += (price * quantity)
        return self.total
      else:
        self.items.append(title)
        self.total += price
        return self.total
      return self.items
      
  def apply_discount(self):
    # breakpoint()
    self.total = int(self.total - (self.discount * 10))
    # print('There is not discount to apply.')
    if self.discount > 0:
      print(f'After the discount, the total comes to ${self.total}.')
      return self.total
    else:
      print('There is no discount to apply.')
