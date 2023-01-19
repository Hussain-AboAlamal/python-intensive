"""
Refactor the following classes to follow SOLID Principles. Add every principle to it's own file
"""

# SRP

accounts_list = []

class BankAccount:
   
   def __init__(self, account_no: str):
       self.account_no = account_no
   
   def get_account_number(self):
       return self.account_no
   
   def save(self) -> None:
     accounts_list.append(self)
     print("Success, saved to DB")
     
     
# open/closed

class Discount:
   def __init__(self, customer, price):
       self.customer = customer
       self.price = price
   
   def give_discount(self) -> float:
       if self.customer == 'silver':
           return self.price * 0.2
       elif self.customer == 'gold':
           return self.price * 0.3
       elif self.customer == 'vip':
           return self.price * 0.4
       
# Liskov

class Vehicle:

   def engine(self) -> None:
       pass

   def start_engine(self) -> None:
       self.engine()


class Car(Vehicle):
   """A demo Car Vehicle class"""
   def start_engine(self) -> None:
       print("Let's go")


class Bicycle(Vehicle):
   """A demo Bicycle Vehicle class"""
   def start_engine(self) -> None:
       print("I don't have an engine")
       
# Interface segregation

class Worker:
    def build_construction(self) -> None:
        pass
    
    def serve_the_table(self) -> None:
        pass
    
    def check_hometask(self) -> None:
        pass
    
class Builder(Worker):
    def build_construction(self) -> None:
        print("No! I have a dinner!")
    
    def serve_the_table(self) -> None:
        pass
    
    def check_hometask(self) -> None:
        pass
    
class Waiter(Worker):
    def build_construction(self) -> None:
        pass
    
    def serve_the_table(self) -> None:
        print("Going to table")
    
    def check_hometask(self) -> None:
        pass
    
class Teacher(Worker):
    def build_construction(self) -> None:
        pass
    
    def serve_the_table(self) -> None:
        pass
    
    def check_hometask(self) -> None:
        print("Students are so talented!")
        
        
# Dependency Inversion

class Reporter:
    
    @staticmethod
    def publish(news: str) -> None:
        print(NewsPaper().publish(news=news))

class NewsPaper:
    
    @staticmethod
    def publish(news: str) -> None:
        print(f"{news} published today")

reporter = Reporter()
print(reporter.publish("News Paper"))
