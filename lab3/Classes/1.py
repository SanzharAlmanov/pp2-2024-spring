class Student():
    def __init__(self, name_param='', ID_param='A'):
        self.name = name_param
        self.ID = ID_param
    
    def print_inf(self):
        print(self.name, self.ID)
    
    def get_inp(self):
        self.name = input()   
        self.ID = int(input()) 
        
stud = Student()
stud.get_inp()
stud.print_inf()