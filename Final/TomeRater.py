class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.books = {}
    self.bookcount = 0
	
  def get_email(self):
    print(self.name + "'s email address is currently " + self.email)
	
  def change_email(self, address):
    self.email = address
    print(self.name + "'s email address has been changed to " + address)
	
  def __repr__(self):
    return "User: " + self.name + ", Email: " + self.email + ", Books Read: " + str(self.bookcount)
	
  def __eq__(self, other_user):
    if self.name == other_user.name and self.email == other_user.email:
          return True
    else:
          return False
	  
  def read_book(self, book, rating=0):
    self.books[book.title] = rating
    self.bookcount += 1
	
  def get_average_rating(self):
    cnt = 0
    lst = []
    for rate in self.books.values():
      lst.append(rate)
      cnt += 1
    return cnt / len(lst)

  def get_high_rating(self):
    rat = 0
    for rate in self.books.values():
      if rate > rat:
        rat = rate
    return rat
	
  def __hash__(self):
    return hash((self.title, self.isbn))
	
##-----------
class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []
	
  def get_title(self):
    return self.title
	
  def get_isbn(self):
    print(self.isbn)
    return self.isbn
	
  def add_rating(self, rating):
    self.ratings.append(rating)
	
  def __eq__(self, other_book):
    if self.title == other_book.title:
      return True
    else:
      return False
	  
  def __repr__(self):
    return "Title: " + self.title + ", Isbn: " + str(self.isbn)

##------------
class Fiction(Book):
  def __init__(self, title, author, isbn):
   # super().__init__(title, isbn)
    self.title = title
    self.author = author
    self.ratings = []
	
  def get_author(self):
    return self.author

  def set_isbn(self, isbn):
    self.isbn = isbn
	
  def __repr__(self):
    return self.title + " by " + self.author
	
##--------------
class Non_Fiction(Book):
  def __init__(self, title, subject, level, isbn):
    self.title = title
    self.subject = subject
    self.level = level
    self.ratings = []
	
  def get_subject(self):
    return self.subject
	
  def get_level(self):
    return self.level
	
  def __repr__(self):
    return self.title + ", a " + self.level + " manual on " + self.subject
	
##----------------
class TomeRater(object):
  def __init__(self):
    self.users = {}
    self.books = {}
  
  def create_book(self, title, isbn):
    return Book(title, isbn)
	
  def create_novel(self, title, author, isbn):
    return Fiction(title, author, isbn)
	
  def create_non_fiction(self, title, subject, level, isbn):
    return Non_Fiction(title, subject, level, isbn)
	
  def add_user(self, name, email, books=None):
    if email not in self.users:
      self.users[email] = User(name, email)
      if books is not None:
        for book in books:
          self.add_book_to_user(book, email)
    else:
      print("This User already Exists")
	  
  def add_book_to_user(self, book, email, rating=None):
    user = self.users.get(email, "No User with Email: {email}".format(email=email))
    if user:
      user.read_book(book, rating)
      book.add_rating(rating)
      self.books[book] = self.books.get(book, 0) + 1
		
  def print_catalog(self):
    for ke in self.books.keys():
      print(ke)
	  
  def print_users(self):
    for val in self.users.values():
      print(val)
	  
  def get_most_read_book(self):
    bk = 0
    for val in self.users.values():
      if val > bk:
        bk = val
    return bk
	  
  def highest_rated_book(self):
     rat = 0
     for val in self.books.values():
       if val > rat:
         rat = val
     return rat

  def most_positive_user(self):
    val = 0
    val2 = 0
    for ke in self.users.values():
      val = ke.get_average_rating()
      if val2 < val:
        val2 = val
    return val2
