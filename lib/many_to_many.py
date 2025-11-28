class Author:
    all = []
    def __init__(self, name):
   

        self.name = name
        Author.all.append(self)

    def contracts(self):
        
        return [contract for contract in Contract.all if contract.author is self]

    def books(self):
        
        return [contract.book for contract in self.contracts()]

    def sign_contract(self, book, date, royalties):
      
        if not isinstance(book, Book):
            raise Exception("book must be instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        # create and return new contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
       
        return sum(contract.royalties for contract in self.contracts())

    


class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        
        return [contract for contract in Contract.all if contract.book is self]
    
    def authors(self):
        return [contract.author for contract in Contract.all if contract.book is self]

   
  


class Contract:
    all = []
    def __init__(self, author, book, date, royalties):
        
        if not isinstance(author, Author):
           raise Exception("author must be instance of Author")
        
        if not isinstance(book, Book):
            raise Exception("book must be instance of a Book")
        
        if not isinstance(date, str):
            raise Exception("date must be a string")
        
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_author(cls, date):
        return [contract for contract in cls.all if contract.date == date]
    
    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls.all if contract.date == date]
        
       
   