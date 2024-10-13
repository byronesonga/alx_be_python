class Book:
    
    # define instance attribute
    
    def __init__(self,title:str,author:str,year:int):

        self.title = title
        self.author = author
        self.year = year

    # define a repr formate (more official)
    def __repr__(self):
        
        return f"Book('{self.title}', '{self.author}', {self.year})"

    # defien a string message to show info about the object
    def __str__(self):
        
        return f"{self.title} by {self.author}, published in {self.year}"

    # define the message before deleting the object directly
    def __del__(self):
        print(f"Deleting {self.title}")