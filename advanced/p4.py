"""
Problem 4
Try to implement django models.Model using some alternative way than
metaclasses

Custom classes should ineheret from a base class that implements some sort of
persistancy using save, delete.
The important part is to hide the detail of persistancy implementation and
make custom classes easy to create

Usage:
A user defined class class should provide access for the following 
persistancy  methods.
+------------+
|   Model    |
+------------+
| - state    |
| + objects  |
+------------+
| + save()   |
| + delete() |
-------------+
also, the base class should provide access to an objects attribute, a proxy
object that handle the mutation of the entries

"""

import unittest

class Field(object):
    pass

class CharField(Field):
    def __init__(self, max_length, value):
        self.max_length = max_length
        self.value = value

class DateField(Field):
    def __init__(self, max_length, value):
        self.max_length = max_length
        self.value = value

class ModelState(object):
    def __init__(self, *args, **kwargs):
        pass
    db = None # for now

class QuerySet(object):
    def __init__(self, *args, **kwargs):
        self._its_vals = []
    def all(self):
        print 'its objects'
    def get(self, *args, **kwargs):
        for key, value in kwarts.iteritems():
            if key == pk:
                pass
    def count(self):
        return len(self._its_vals)

def model(klass):
    """
    A decorator that bolts on functionality: save, delete, mutators
    """
    state = ModelState(klass)
    objects = QuerySet(klass)

    for key, value in klass.__dict__.iteritems():
        if isinstance(key, Field):
            print "\n{} is {}".format(key, value)

    def model_init(self, *args, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def model_save(self):
        pass

    def model_delete(self):
        pass

    def model_id(self):
        return id(self)

    klass.__init__ = model_init
    klass.save = model_save
    klass.delete = model_delete
    klass.id = model_id
    klass._state = state
    klass.objects = objects
    return klass

@model
class Book(object):
    title = CharField(max_length = 80, value = 'Default Title')
    author = CharField(max_length = 40, value = 'Default Author')
    def __str__(self):
        return self.title

class BookBaseTest(unittest.TestCase):
    def setUp(self):
        self.title = 'A Christmas Carol'
        self.author = 'Dickens, Charles'
        self.book = Book(title = self.title, 
                         author = self.author)
    
    def test_init(self):
        self.assertEquals(self.title, self.book.title)
        self.assertEquals(self.author, self.book.author)

class BookSaveTest(BookBaseTest):
    def test_emtpy(self):
        self.assertEquals(0, Book.objects.count())

    def test_save(self):
        self.book.save()
        self.assertEquals(1, Book.objects.count())
        self.assertEquals(self.book, Book.objects.get(pk = self.book.id))

class BookModifyTest(BookBaseTest):
    def test_modify(self):
        new_title = 'The red and the black'
        new_author = 'Stendhal'
        self.book.author = new_author
        self.book.title = new_title
        self.book.save()
        self.assertEquals(self.book, Book.objects.get(pk = self.book.id))

if __name__ == '__main__':
    unittest.main()
