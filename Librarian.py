import Parent


class Librarian(Parent):

    def __init__(self, full_name, age, id_no, employment_type):
        super(Parent, self).__init__(id=id)
        self.full_name = full_name
        self.age = age
        self.id_no = id_no
        self.employment_type = employment_type

    def set_full_name(self, full_name: str):
        self.full_name = full_name

    def set_age(self, age: int):
        self.age = age

    def set_id_no(self, id_no: str):
        self.id_no = id_no

    def set_employment_type(self, employment_type: bool):
        self.employment_type = employment_type

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.age

    def get_id_no(self):
        return self.id_no

    def get_employment_type(self):
        return self.employment_type
