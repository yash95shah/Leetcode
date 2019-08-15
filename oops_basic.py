class Employee:
    'Common base class for all employees'
    empCount = 0
 
    def __init__(self):
        #self.empCount = 0
        Employee.empCount += 1
    
    def displayCount(self):
      print ("Total Employee : {}" .format( Employee.empCount))
 
    def displayEmployee(self):
       print ("Name : {}" .format(self.name),  ", Salary: {}" .format(self.salary))

    def __repr__(self):
       return "Name : {}" .format(self.name) +  ", Salary: {}" .format(self.salary)


class Engineer(Employee):
    def __init__(self, name, salary):
        #self.empCount = 0
        self.name = name
        self.salary = salary
        self.benefits =list()
        #self.has_been_given_bonus = False
        Employee.empCount +=1
    def give_bonus(self, bonus):
        #self.has_been_given_bonus =True
        self.salary += bonus
        return 
    def give_benefits(self, l_of_benefits):

        if l_of_benefits not in ["Medical", "Vision","Dentistry","401K"]:
            print("Error! You haven't entered a correct benefit")
        else:
            if "Medical" in self.benefits:
                self.benefits.append(l_of_benefits)
                self.give_bonus(bonus= 0.18* self.salary)
                
            else:
                self.benefits.append(l_of_benefits)
        return




if __name__ is '__main__':
    # a = (3,5)
    # print (type(a))
   em_1 = Engineer(name= "Yash", salary=75000)
   #em_1.displayCount()
   em_1.give_bonus(bonus=5000)
   #bonus1 ="Medical"
   bonus2 = "401K"
   #em_1.give_benefits(l_of_benefits=bonus1)
   em_1.give_benefits(l_of_benefits=bonus2)
  # print (em_1.benefits)
   print (em_1)
   


