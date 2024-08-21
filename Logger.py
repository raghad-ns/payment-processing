# Logger class, using singleton design pattern
class Logger:
    def __new__(self):
        if not hasattr(self, 'instance'):
            self.instance = super(Logger, self).__new__(self)
        return self.instance
    
    def log(self, message):
        print(message)
