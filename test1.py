




from ctypes import addressof
from re import A


def run_test():
    print ("Test 1 - dictionaries")

    me = {
        "first": "Chris",
        "last": "Reinhart",
        "age": 28,
        "hobbies": [],
        "address": {
            "city": "San Francisco",
            "country": "US",
            "state": "CA",
            "zip": "94107",
            "street": "Arrow Rd",
        }
    }

    
    print(me["first"])
    print(me["first"] + " " + me["last"])

    ### read about f strings

    me["age"] = me["age"] + 1
    
    me["preferred_color"] = "yellow"

    

    if "middle_name" in me:
        print(me["middle_name"])

    address = me["address"]
    print(address)
    print(type(address)) 

    print(f"{address['street']}, {address['city']}, {address['country']}, {address['zip']}, {address['state']}")
    







run_test()