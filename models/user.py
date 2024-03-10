from models.base_model import BaseModel

class User(BaseModel):
    
    def __init__(self, *args, **kwargs):
        """initialize user instance"""
        super().__init__(*args, **kwargs)
        self.email = "" #initializing email attribute
        self.password = "" #initializing password attribute to an empty string
        self.first_name = "" #initializing first_name attribute
        self.last_name = "" #initialize last_name attribute to an empty string
        