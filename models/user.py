from models.base_model import BaseModel


class User(BaseModel):

    email = ""  # initializing email attribute
    password = ""  # initializing password attribute to an empty string
    first_name = ""  # initializing first_name attribute
    last_name = ""  # initialize last_name attribute to an empty string
