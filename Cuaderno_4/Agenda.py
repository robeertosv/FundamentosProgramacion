def new_agenda() -> list:
    """Creates an empty agenda"""
    return []
    pass

def find_phone(a: list, name: str) -> str:
    """Returns the phone associated to the name.
    if name not in the agenda, returns None.
    """
    uid = None
    for i in range(len(a)):
        if(name in a[i]):
            uid = i
    
    try:
        phone = a[uid][1]
    except TypeError:
        phone = None
        
    return phone
    pass

def add_entry(agenda: list, name: str, phone: str, overwrite: bool = True) -> bool:
    """Adds an entry to the agenda with the pair name, phone
    if overwrite is True and the name was existing, replaces the phone.
    if overwrite is False and the name was existing, returns False.
    if the entry was added or changed, returns True
    """
    name_in_agenda = False
    uid = 0
    for i in range(len(agenda)):
        if(name in agenda[i]):
            uid = i
            name_in_agenda = True
    
    if(overwrite and name_in_agenda):
        agenda[i][1] = phone     
        status = True   
    if(not overwrite and name_in_agenda):
        status = False
    if(not name_in_agenda):
        agenda.append([name, phone])
        status = True
    
    return status
    pass
def delete_entry(a: list, name: str):
    """Deletes an entry from the agenda.
    if the name was not existing, does nothing.
    """
    for i in range(len(a)):
        if(name in a[i]):
            a.pop(i) 
    pass


def contains(a: list, name: str) -> bool:
    """Returns true if the name is in the agenda.
    """
    flag = False
    for i in range(len(a)):
        if(name in a[i]):
            flag = True
    return flag
    pass


def find(a: list, name: str) -> int:
    """Returns the position of the name in the agenda, -1 if not found.
    """
    uid = -1
    for i in range(len(a)):
        if(name in a[i]):
            uid = i
    return uid
    pass


def print_agenda(a: list) -> None:
    """Prints the agenda, an entry per line.
    """
    for i in range(len(a)):
        print(f"Nombre: {a[i][0]}, teléfono: {a[i][1]}")
    pass


# Create and append tests:
a = new_agenda()
add_entry(a, "juan", "91886777")
add_entry(a, "pepe", "91555555")
add_entry(a, "ana", "914444444")

ok = add_entry(a, "ana", "999999", False)

if not ok:
    print("Error adding entry.")

ok = add_entry(a, "ana", "999999", True)
if not ok:
    print("Error adding entry.")

print_agenda(a)
# Contains and find tests:
print(contains(a, "juan"), contains(a, "antonio"))
print(find(a, "ana"), find(a, "antonio"))
print(find_phone(a, "ana"), find_phone(a, "antonio"))

# Delete testing:
delete_entry(a, "ana")
delete_entry(a, "antonio")
print(find_phone(a, "ana"))