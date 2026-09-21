import sys

'''This function provides the capacity, size and space left in the list.
We can invoke it to get the details of the lsit.'''

def list_details(lst):
    print("Capacity:", (sys.getsizeof(lst)-36)//4)

    print("Size:", len(lst))

    print("Space left:", ((sys.getsizeof(lst)-36) - len(lst*4))//4)

marias_lst=[]
print("Empty list created!!!")
print("List details:")
list_details(marias_lst)


marias_lst.append("Sugar")
print("Maria's list after adding Sugar:")
print(marias_lst)
print("List details:")
list_details(marias_lst)
