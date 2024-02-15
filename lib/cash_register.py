#!/usr/bin/env python3

class CashRegister:

  def __init__(self, discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.transactions = []

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

  # def last_item(last):
  #   print(last[-1])

  def add_item(self, title, price, quantity=0):
      if quantity > 0:
        x = range(quantity)
        for q in x:
          self.items.append(title)
          self.transactions.append(price * quantity)
        self.total += (price * quantity)
        return self.total
      else:
        self.items.append(title)
        self.transactions.append(price)
        self.total += price
        return self.total
      
      return self.items

  def apply_discount(self):
    self.total = int(self.total - (self.discount * 10))
    if self.discount > 0:
      print(f'After the discount, the total comes to ${self.total}.')
      return self.total
    else:
      print('There is no discount to apply.')

  def void_last_transaction(self):
    # self.total = self.total - self.transactions[-1]
    # return self.total
    self.total = self.total - self.transactions.pop(-1)
    return self.total

    
    
    