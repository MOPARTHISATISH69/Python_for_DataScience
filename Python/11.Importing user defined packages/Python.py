class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return "student name is :" + str(self.name)+ ' '+str(self.age)+ " years old"
    def firstName(self):
        return self.name.split(' ')[0]
    def lastName(self):
        return self.name.split(' ')[1]