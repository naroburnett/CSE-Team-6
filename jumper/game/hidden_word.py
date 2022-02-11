import random


class Hidden_Word:
    def __init__(self):
        word_catalog = ["Abuse","Adult","Agent","Anger","Apple","Award","Basis"
        ,"Beach","Birth","Block","Blood","Board","Brain","Brain","Bread"
        ,"Break","Break","Brown","Buyer","Cause","Chain","Chair","Chest"
        ,"Cheif","Child","Dream","Dress"," Depth","Drive","Drink","Event"
        ,"Final","Force","Floor","Focus","Frame","Guide","Heart","Henry"
        ,"Hotel","House","Image","Index","Input","Judge","Knife","Lunch"
        ,"Limit","Model","Motor","Mouth","Month","Money","Music","Night"
        "Noise","North","Novel","Nurse","Offer","Order","Phase","Peace"
        ,"Pilot","Pitch","Place","Plane","Plate","Point","Pound"]
        
        self._word = random.choice(word_catalog)
    
    def get_word(self):
        return self._word

    def is_found(self):
        return True












