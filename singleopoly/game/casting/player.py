class Player():
    def __init__(self):
        self.name = None
        self.bank = 1500
        self.properties_owned = [] #list of properties
        self.location = None
        self.color = None
    

    def set_name(self, name):
        """Updates player name to the given one.
        
        Args:
            name(string): The player name.
        """
        self.name = name

    def set_bank(self, amount):
        """Updates player current amount of cash in bank to the given one.
        
        Args:
            Amount(Total): The player bank amount.
        """

        self.bank = amount
    
    def set_properties_owned(self, list):
        """Updates player properties list to the given one.
        
        Args:
            list (list of properties): The player owned properties
        """
        self.properties_owned = list
    
    def set_location(self, point):
        """Updates player location to the given one.
        
        Args:
            Point (location): The players current location
        """
        self.location = point
    
    def set_color(self, color):
        """Updates player color to the given one.
        
        Args:
            color : The player color
        """
        self.color = color

    def get_name(self):
        """Gets player name.
        
        Returns:
            String: The player name.
        """
        return self.name

    def get_bank(self):
        """Gets player curent bank holdings.
        
        Returns:
            number: The current bank amount.
        """

        self.bank
    
    def get_properties_owned(self):
        """Gets player properties owned.
        
        Returns:
            List: a list of owned properties.
        """
        return self.properties_owned
    
    def get_location(self):
        """Gets player location.
        
        Returns:
            String: The players loaction.
        """
        return self.location
    
    def get_color(self):
        """Gets player color.
        
        Returns:
            String: The players color.
        """
        return self.color
    