class BoardGame: 

    def __init__(self, name, description, quantity, buying_cost, selling_price, manufacturer, id=None):
        self.name = name
        self.description = description
        self.quantity = quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.manufacturer = manufacturer
        self.id = id