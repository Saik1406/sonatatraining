from employee import Employee
from address import Address
address1=Address("banglore")
address2=Address("hyderabad")

emp1=Employee("sai","kiran","narasaraopet")
emp2=Employee("sai","kiran",[address1,address2])
print(address1.display_address())
print(address2.display_address())
print(emp1.display())
print(emp2.display())