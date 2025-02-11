from tkinter import *
from db import DataBase

db = DataBase("store.db ")


class Root(Tk):
    def __init__(self):
        super().__init__()
        self.title("Book Store Application")
        self.geometry("600x350")
        self.create_widgets()
        self.populate_list()

    
    def create_widgets(self):
        #title
        self.title_label = Label(self,text = "Title")
        self.title_label.grid(row=0 , column=0, pady=20)
        self.title_text = StringVar()
        self.title_entry = Entry(self, textvariable=self.title_text)
        self.title_entry.grid(row=0 , column=1)

        #author
        self.author_label = Label(self,text = "Author")
        self.author_label.grid(row=0 , column=2)
        self.author_text = StringVar()
        self.author_entry = Entry(self, textvariable=self.author_text)
        self.author_entry.grid(row=0 , column=3 ) 
        
        #year
        self.year_label = Label(self,text = "Year")
        self.year_label.grid(row=1 , column=0)
        self.year_text = StringVar()
        self.year_entry = Entry(self, textvariable=self.year_text)
        self.year_entry.grid(row=1 , column=1)

        #isbn
        self.isbn_label = Label(self,text = "ISBN")
        self.isbn_label.grid(row=1 , column=2)
        self.isbn_text = StringVar()
        self.isbn_entry = Entry(self, textvariable=self.isbn_text)
        self.title_entry.grid(row=1 , column=3)

        #Book List
        self.books_list = Listbox(self, height=8, width=50 , border=0)
        self.books_list.grid(row=3, column=0, rowspan=6, columnspan=3, padx=20, pady=20)

        #bind listbox
        self.books_list.bind("<<ListboxSelect>>", self.select_box)


        #scroll bar
        self.scrollbar = Scrollbar(self)
        self.scrollbar.grid(row = 3, column=3, rowspan=6, sticky=NS, pady = 20)

        #connect listbox and scrollbar together
        self.books_list.configure(yscrollcommand= self.scrollbar.set)
        self.scrollbar.configure(command=self.books_list.yview)

        #Buttons
        self.add_btn = Button(self, text = "Add Book" , command=self.add_book)
        self.add_btn.grid(row=2 , column=0, pady=20)

        self.remove_btn = Button(self, text = "Remove Book" , command=self.remove_book)
        self.remove_btn.grid(row=2 , column=1)

        self.update_btn = Button(self, text = "Update Book" , command=self.update_book)
        self.update_btn.grid(row=2 , column=2)

        self.search_btn = Button(self, text = "Search Book" , command=self.search_book)
        self.search_btn.grid(row=2 , column=3)




    def populate_list(self, rows = None):
        self.books_list.delete(0,END)
        if rows == None: 
            rows = db.fetch()
        for row in rows:
            self.books_list.insert(END, row)







    def add_book(self):
        if self.title_text.get() == '' or self.author_text.get() == '' or self.year_text.get() == '' or self.year_text.get() == '':
            return
        

        db.insert(self.title_text.get() , self.author_text.get() , self.year_text.get() , self. isbn_text.get())
        #clear list, populate listbox
        self.clear_fields()
        self.books_list.delete(0,END)
        self.populate_list()

    def select_box(self , event):
        widget = event.widget
        self.selected_item = widget.get(ANCHOR)

        #add test to entries
        self.clear_fields()
        self.title_entry.insert(END, self.selected_item[1])
        self.author_entry.insert(END, self.selected_item[2])
        self.year_entry.insert(END, self.selected_item[3])
        self.isbn_entry.insert(END, self.selected_item[4])


    def remove_book(self):
        db.remove(self.selected_item[0])
        self.clear_fields()
        self.populate_list()

    def update_book(self):
        db.update(self.selected_item[0], self.title_text.get(), self.author_text.get() , self.year_text.get(), self.isbn_text.get())
        self.populate_list() 


    def search_book(self):
        rows = db.search(self.title_text.get(), self.author_text.get(), self.year_text.get(),self.isbn_text.get())
        self.populate_list(rows)

    def clear_fields(self):
        self.title_entry.delete(0, END)
        self.author_entry.delete(0, END)
        self.year_entry.delete(0, END)
        self.isbn_entry.delete(0, END)



root = Root()
root.mainloop()
