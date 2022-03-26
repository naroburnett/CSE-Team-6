class Utility():
    def __init__(self):
        self.id = None
        self.name = None
        self.cost = None
        self.rent = None
        self.owned = [None, None]
        self.mortgage = None
        self.is_mortgage = 0
        self.no_owned = 0
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

    def set_owned(self,rent,index):
        """Updates the property utility rents to the given ones.
        
        Args:
            rent (cost): The given utility property rent.
            index (utility): the utility rent to be changed in list. 
        """
        self.owned[index] = rent

    def set_mortgage(self, mortgage):
        """Updates the property mortgage cost to the given one.
        
        Args:
            Number (mortgage) : The given property mortage amount.
        """
        self.mortgage = mortgage
    
    def set_is_mortgage(self, logic):
        """Updates if the property has been mortgaged.
        
        Args:
            Logic : True or False statment.
        """
        self.is_mortgage = logic

    def set_no_owned(self, no_owned):
        """Updates the amount of utilities owned to the given one.
        
        Args:
            no_owned : The given amount of utilities owned.
        """
        self.no_owned = no_owned
    
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

    def get_owned(self,index):
        """Gets updated rent cost with amount of utilities owned.
        
        Returns:
            number: The property updated rent with amount of utilities owned.
        """
        return self.owned[index]
    
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

    def get_no_owned(self):
        """Gets current amount of utilities owned.
        
        Returns:
            Number: The amount of utilities currently owned.
        """
        return self.no_owned
    
    def get_owner(self):
        """Gets property owner.
        
        Returns:
            name: The property owner.
        """
        return self.owner