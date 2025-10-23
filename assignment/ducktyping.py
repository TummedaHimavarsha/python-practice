class Duck:
    def walk(self):
        print("ducks walk")
class Person(Duck):
    def walk(self):
        print("some people usaully walk in sleep")
def make_it_walk(obj):
    obj.walk()
a=Duck()
make_it_walk(a)
b=Person()
make_it_walk(b)


class MP3:
    def play(self):
        print("mp3 allows to download the songs")
class Video(MP3):
    def play(self):
        print("videos are played using autocontrols")
def start_media(obj):
    obj.play()
a=MP3()
start_media(a)
b=Video()
start_media(b)


from abc import ABC,abstractmethod
class bankaccount(ABC):
    @abstractmethod
    def withdraw(self,amount):
        pass
class savings(bankaccount):
    def withdraw(self, amount,balance):
        if balance>500:
            return amount-balance
class currentaccount(bankaccount):
    def withdraw(self):
        print("no minimu balance check")
a=savings()
print(a.withdraw(10000,900))
b=currentaccount()
b.withdraw()