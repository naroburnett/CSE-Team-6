


class Property():
    def __init__(self):
        self.id = None
        self.name = None
        self.color = None
        self.cost = None
        self.rent = None
        self.houses = [None,None,None,None,None] #[0] = 1st house, [1] = 2nd house...
        self.mortgage = None
        self.is_mortgage = 0
        self.no_of_houses = 0
        self.owner = None

    def set_id(self,id):
        """Updates property id to the given one.
        
        Args:
            String(xxx): The property id.
        """
        self.id = id
    
    def set_name(self,name):
        """Updates the property name to the given one.
        
        Args:
            String(name): The given name.
        """
        self.name = name
    
    def set_color(self,color):
        """Updates the property color to the given one.
        
        Args:
            Color: The given property color.
        """
        self.color = color
    
    def set_cost(self, cost):
        """Updates the property cost to the given one.
        
        Args:
            Number (cost): The given property cost.
        """
        self.cost = cost
    
    def set_rent(self, rent):
        """Updates the property rent to the given one.
        
        Args:
            number(rent): The given property rent.
        """
        self.rent = rent

    def set_houses(self,rent,index):
        """Updates the property house rents to the given ones.
        
        Args:
            rent (cost): The given house property rent.
            index (house): the house rent to be chnaged in list. 
        """
        self.houses[index] = rent
    
    def set_mortgage(self, mortgage):
        """Updates the property mortgage cost to the given one.
        
        Args:
            Number (mortgage) : The given property mortage amount.
        """
        self.mortgage = mortgage
    
    def set_is_mortgage(self, logic):
        """Updates if the property has be mortgaged.
        
        Args:
            Logic : True or False statment.
        """
        self.is_mortgage = logic
    
    def set_no_of_houses(self, no_of_houses):
        """Updates the properties current amount of houses to the given one.
        
        Args:
            no_of_houses : The given amount on property.
        """
        self.no_of_houses = no_of_houses
    
    def set_owner(self, owner):
        """Updates the property owner to the given one.
        
        Args:
            owner: The given property owner.
        """
        self.owner = owner

    def get_id(self):
        """Gets property id.
        
        Returns:
            String: The property id.
        """
        return self.id 
    
    def get_name(self):
        """Gets property name.
        
        Returns:
            String: The property name.
        """
        return self.name
    
    def get_color(self):
        """Gets property color.
        
        Returns:
            Color: The property color.
        """
        return self.color
    
    def get_cost(self):
        """Gets property cost.
        
        Returns:
            Number: The property cost.
        """
        return self.cost
    
    def get_rent(self):
        """Gets property initial rent cost.
        
        Returns:
            Number: The property inital rent cost.
        """
        return self.rent

    def get_houses(self,index):
        """Gets updated rent cost with house amount.
        
        Returns:
            number: The property updated rent with house amount.
        """
        return self.houses[index]
    
    def get_mortgage(self):
        """Gets property mortgage.
        
        Returns:
            Point: The property mortgage.
        """
        return self.mortgage

    def get_is_mortgage(self):
        """Gets if the property has been mortgage.
        
        Returns:
            Boolean: True or False.
        """
        return self.is_mortgage

    def get_no_of_houses(self):
        """Gets current amount of houses on property.
        
        Returns:
            Number: The amount of house currently placed.
        """
        return self.no_of_houses
    
    def get_owner(self):
        """Gets property owner.
        
        Returns:
            name: The property owner.
        """
        return self.owner