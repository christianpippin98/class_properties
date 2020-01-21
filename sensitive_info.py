class Patient:
    
    def __init__(self, ssn, dob, hin, first_name, last_name, address):
        self.__ssn = ssn
        self.__dob = dob
        self.__hin = hin
        self.__first_name = first_name
        self.__last_name = last_name
        self.__address = address


    @property
    def ssn(self):
        return self.__ssn


    @property
    def dob(self):
        return self.__dob


    @property
    def dob(self):
        return self.__hin


    @property
    def address(self):
        return self.__address


    @property
    def full_name(self):
        return f"{self.__first_name} {self.__last_name}"

    @address.setter
    def address(self, new_address):
        if type(new_address) is str:
            self.__address = new_address
        else:
            raise TypeError('Please provide a string for the address.')


cashew = Patient(
    "097-23-1003", "08/13/92", "7001294103",
    "Daniela", "Agnoletti", "500 Infinity Way"
)

# This should not change the state of the object
# cashew.ssn = "838-31-2256"

# Neither should this
# cashew.dob = "01-30-90"

# But printing either of them should work
print(cashew.ssn)   # "097-23-1003"

# These two statements should output nothing
# print(cashew.first_name)
# print(cashew.last_name)

# But this should output the full name
print(cashew.full_name)   # "Daniela Agnoletti"