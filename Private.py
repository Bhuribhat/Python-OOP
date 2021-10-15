# Private Class -> "_" to remind programmers NOT to use it.
class _Private:
    def __init__(self, name):
        self.name = name

# Public Class
class NotPrivate:
    def __init__(self, name):
        self,name = name
        self.priv = _Private(name)
    
    # Private Method -> We can still use them normally.
    def _display(self):
        print("Hello")

    # Public Method
    def display(self):
        print("Hi")