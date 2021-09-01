class Author:


    def __init__(self, name):
        self.name = name
        # from video
        self.books = []

    def __str__(self):
        book_list = ', '.join(self.books) or 'No books'
        # from video
        #if self.books:
       
        # else:
        #     book_list = 'No books' 
        return f'author: {self.name}, books: {book_list}'
    
    
    def publish(self,title):
        if title in self.books:
            print(f'{title} already in list')
        else:
            self.books.append(title)
        
    

def main():
    tom = Author('Tom')
    tom.publish('xyz')
    tom.publish('xyz')
    tom.publish('abc')
    
    jerry = Author('Jerry')
    jerry.publish('vuy')
    jerry.publish('nuy')
    print(tom)
    print(jerry)
    max = Author('Max')
    print(max)

main()