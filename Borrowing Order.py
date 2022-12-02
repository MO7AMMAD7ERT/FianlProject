from datetime import datetime

import Parent


class Borrowing_Order(Parent):

    def __init__(self, date, client_id, book_id, status):
        super(Parent, self).__init__(id=id)
        self.date = date
        self.client_id = client_id
        self.book_id = book_id
        self.status = status

    def set_date(self, date: datetime):
        self.date = date

    def set_client_id(self, client_id: str):
        self.client_id = client_id

    def set_book_id(self, book_id: str):
        self.book_id = book_id

    def set_status(self, status: str):
        self.status = status

    def get_date(self):
        return self.date

    def get_client_id(self):
        return self.client_id

    def get_book_id(self):
        return self.book_id

    def get_status(self):
        return self.status
