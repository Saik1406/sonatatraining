from leave import Leave
from basketleave import BasketOfLeave
from restrictedleave import RestrictedLeave
r1=RestrictedLeave(22790,"sai",20,"2001-06-14")
print(r1.display_dob())
b1=BasketOfLeave(22790,"sai",20,"health")
print(b1.displayleave())
l1=Leave(22790,"sai kiran",20)
print(l1.display())
