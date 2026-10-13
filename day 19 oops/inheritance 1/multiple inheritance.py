# multiple inheritance

class Phone:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
        
    def make_call(self,number):
        return f"{self.brand} {self.model} is calling {number}"
    
    def send_msg(self,number,message):
        return f"{self.brand} {self.model} sent messageto {number} : {message}"

class Camera:
    def __init__(self,resolution):
        self.resolution = resolution

    def take_photo(self):
        return f"Taking photo with {self.resolution} MP camera"
    
    def record_video(self):
        return f"Recording video with {self.resolution} MP camera"


class Smartphone(Phone,Camera):
    def __init__(self, brand, model,resolution):
        Phone.__init__(self,brand, model)
        Camera.__init__(self,resolution)
               
        
s = Smartphone("Iphone","16 Pro Max","48")
print(s.make_call(7447596811))
print(s.send_msg(7447596811,"shivam"))
print(s.take_photo())
print(s.record_video())


'''ASSIGNMENT'''

class Person:
    def getname(self,name):
        self.name = name
    def showperson(self):
        return f"Name of person is : {self.name}"
    
class Doctor(Person):
    def getdoctor(self,specialization):
        self.specialization = specialization
    def showdoctor(self):
        return f"specialization of doctor is : {self.specialization}"

class Surgeon(Doctor):
    def getsurgeon(self,surgerytype):
        self.surgerytype = surgerytype
    def showsurgeon(self):
        return f"surgerytype : {self.surgerytype}"

s1 = Surgeon()
s1.getdoctor("MBBS")
s1.getname('shivam')
s1.getsurgeon('hello')
print(s1.showsurgeon())
print(s1.showdoctor())
print(s1.showperson())
