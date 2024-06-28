class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        is_false = hasattr(self,"name")
        if isinstance(name, str) and 3 <= len(name) and is_false == False:
            self._name = name
        else:
            raise Exception("not properly inputted")

        
    def orders(self):
        order_list = []
        all_orders = Order.all
        for order in all_orders:
            if order.coffee == self:
                order_list.append(order)
        return order_list
    
    def customers(self):
        customer_list = []
        unique_order = self.orders()
        for order in unique_order:
            if order.coffee == self and order.customer not in customer_list:
                customer_list.append(order.customer)
        return customer_list
    
    def num_orders(self):
        return len(self.orders())
    
    def average_price(self):
        count = 0 
        orders = self.orders()
        for order in orders:
            count += order.price
        return count/self.num_orders()

class Customer:
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,name):
        if isinstance(name, str) and 1 <= len(name) <=15 :
            self._name = name
        else:
            raise Exception("not properly inputted")
        
    def orders(self):
        customer_orders = []
        all_orders = Order.all 
        for order in all_orders:
                if order.customer == self:
                    customer_orders.append(order)
        return customer_orders

    def coffees(self):
        unique_list = []
        unique_coffees = self.orders()
        for order in unique_coffees:
            if order.customer == self and order.coffee not in unique_list:
                unique_list.append(order.coffee)
        return unique_list

    def create_order(self, coffee, price):
        return Order(self,coffee,price)
    
class Order:
    all = []
    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        self.all.append(self)

    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,price):
        is_false = hasattr(self,"price")
        if isinstance(price, float) and 1.0 <= price <= 10.0 and is_false == False:
            self._price = price
        else:
            raise Exception("not properly inputted")
        
    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self,customer):
        is_false = hasattr(self,"customer")
        if isinstance(customer, Customer) and is_false == False:
            self._customer = customer
        else:
             raise Exception("not properly inputted")
        
    @property
    def coffee(self):
        return self._coffee 
    
    @coffee.setter
    def coffee(self,coffee):
        is_false = hasattr(self,"coffee")
        if isinstance(coffee, Coffee) and is_false == False:
            self._coffee = coffee
        else:
            raise Exception("not the same values")