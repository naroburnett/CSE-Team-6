class Player():
    def __init__(self):
        self.name = None
        self.bank = None
        self.properties_owned = [] #list of properties
        self.location = None
        self.color = None
    

    def set_name(self, name):
        """Updates player name to the given one.
        
        Args:
            String(xxx): The property id.
        """
