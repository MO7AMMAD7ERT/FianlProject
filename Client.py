
import Parent

class Client(Parent):

    def __init__(self, full_name, age, id_no, phone_number, email):
        super(Parent, self).__init__(id=id)
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.phone_number = phone_number
        self.email = email



    def set_full_name(self, full_name: str):
        self.full_name = full_name

    def set_age(self, age: int):
        self.age = age

    def set_id_no(self, id_no: str):
        self.id_no = id_no

    def set_phone_number(self, phone_number: str):
        self.phone_number = phone_number

    def set_email(self, email: int):
        self.email = email



    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_id_no(self):
        return self.id_no

    def get_phone_number(self):
        return self.phone_number

    def get_email(self):
        return self.email
