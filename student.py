class Student:

    def __init__(self, first_name, last_name, age, cohort_number):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__cohort_number = cohort_number


    @property
    def first_name(self):
        try:
            return self.__first_name
        except AttributeError:
            return "Jon"

    @property
    def last_name(self):
        try:
            return self.__last_name
        except AttributeError:
            return "Deux"

    @property
    def age(self):
        try:
            return self.__age
        except AttributeError:
            return 0

    @property
    def cohort_number(self):
        try:
            return self.__cohort_number
        except AttributeError:
            return 0

    @property
    def full_name(self):
        try:
            return f"{self.first_name} {self.last_name}"
        except AttributeError:
            return "Jon Deux"

    @first_name.setter
    def first_name(self, new_first_name):
        if type(new_first_name) is str:
            self.__first_name = new_first_name
        else:
            raise TypeError('Please provide a string for the first name.')

    @last_name.setter
    def last_name(self, new_last_name):
        if type(new_last_name) is str:
            self.__last_name = new_last_name
        else:
            raise TypeError('Please provide a string for the last name.')

    @age.setter
    def age(self, new_age):
        if type(new_age) is int:
            self.__age = new_age
        else:
            raise TypeError('Please provide an integer for the age.')

    @cohort_number.setter
    def cohort_number(self, new_cohort_number):
        if type(new_cohort_number) is int:
            self.__cohort_number = new_cohort_number
        else:
            raise TypeError('Please provide an integer for the cohort number.')

christian = Student("Christian", "Pippen", 21, 36)

christian.last_name = "Pippin"

print(christian.full_name)