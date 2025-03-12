#!/usr/bin/env python3

class Book:
    def __init__(book, title, page_count):
        book.title = title
        book.page_count = page_count

    @property
    def page_count(book):
        return book._page_count 

    @page_count.setter
    def page_count(book, value):
        if not isinstance(value, int):  
            print("page_count must be an integer")
        book._page_count = value

    def turn_page(self):
        print ("Flipping the page...wow, you read fast!")