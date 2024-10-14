class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def to_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'isbn': self.isbn
        }

class Member:
    def __init__(self, name, email, membership_id):
        self.name = name
        self.email = email
        self.membership_id = membership_id

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'membership_id': self.membership_id
        }
