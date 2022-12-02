import Parent

class Book(Parent):

    def __init__(self, title, description, author, status):
        super(Parent, self).__init__(id=id)
        self.title = title
        self.description = description
        self.author = author
        self.status = status



    def set_title(self, title: str):
        self.title = title

    def set_description(self, description: str):
        self.description = description

    def set_author(self, author: str):
        self.author = author

    def set_status(self, status: int):
        self.status = status



    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_author(self):
        return self.author

    def get_status(self):
        return self.status
