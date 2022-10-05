class Person:
  def __init__(self, id,first_name, last_name,age,job) :
    self.id = id
    self.first_name= first_name
    self.last_name = last_name 
    self.age = age 
    self.job = job

def Principal():
    P1 = Person(1,"John","Mitchell",23,"Photographer")
    P2 = Person(2,"Mary","Johnson",16,"Stunt")
    P3 = Person(3,"Steve","Jackson",45,"Director")
    P4 = Person(4,"Julia","Richards",34,"Actor")
    P5 = Person(5,"Richard","Payne",19,"Actor")
    P6 = Person(6,"David","Smith",20,"Actor")
    P7 = Person(7,"Jennifer","Lopez",50,"Singer")
    P8 = Person(8,"Laura","Power",21,"Stunt")

    v=[P1,P2,P3,P4,P5,P6,P7,P8]

    """ for a in range(len(v)):
        v[a] = v[a].first_name.upper()
    """
    v2=[]
    for a in range(len(v)):  
        edad = v[a].age
        if edad%2 != 0:
            v2.append(v[a])
        else:
            pass
        print(v2)
        
Principal()