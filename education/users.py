
print('Module users is successfully imported')

class Human:
    def __init__(self, name = None, familyname = None, age = None, gender = None, nationality = None):
        self.__name = name
        self.__familyname = familyname
        self.__age = age
        self.__gender = gender
        self.__nationality = nationality

    def set_name(self, name =None):
        self.__name = name

    def set_family(self, familyname = None):
        self.__familyname = familyname

    def set_age(self, age = None):
        self.__age = age

    def set_gender(self, gender = None):
        self.__gender = gender

    def set_nationality(self, nationality = None):
        self.__nationality = nationality

    #@staticmethod
    def get_info(self):
        #thisdict = dict(name = {self.__name}, familyname = {self.__familyname}, age = {self.__age}, gender = {self.__gender}, nationality = {self.__nationality}) 
        thisdict = dict(name = self._Human__name, familyname = self._Human__familyname, 
                        age = self._Human__age, gender = self._Human__gender, nationality = self._Human__nationality) 

        return thisdict

class Student(Human):

    def __init__(self, name, familyname, age, gender, nationality, school = None, list_of_subjects = None):
        super().__init__(name, familyname, age, gender, nationality)
        
        self.__school = school
        self.__list_of_subjects = []
        #self.__list_of_subjects += list_of_subjects
        self.__list_of_subjects = [] if list_of_subjects is None else list_of_subjects
        thisdict_student = dict(name = self._Human__name, familyname = self._Human__familyname, age = self._Human__age, 
                        gender = self._Human__gender, nationality = self._Human__nationality, 
                        school = self.__school, list_of_subjects = self.__list_of_subjects)

        #self.__list_of_subjects.append(list_of_subjects)

    def set_school(self, school = None):
        self.__school = school

    def set_list_of_sbj(self, list_of_sbj = None):
        self.__list_of_subjects = list_of_sbj
        
    def add_subject(self, teaching_sbj):
        self.__teaching_sbj_lst.append(teaching_sbj)

    #@staticmethod
    def get_info(self):
        #dict(name = self.__name, familyname = self.__familyname, age = self.__age, gender = self.__gender, nationality = self.__nationality, school = self.__school_uni_name, list_of_subjects = self.__list_of_subjects) 
        thisdict = dict(name = self._Human__name, familyname = self._Human__familyname, age = self._Human__age, 
                        gender = self._Human__gender, nationality = self._Human__nationality, 
                        school = self.__school, list_of_subjects = self.__list_of_subjects) 
        
        return thisdict

class Teacher(Human):
    def __init__(self, name, familyname, age, gender, nationality, school, teaching_sbj):
        super().__init__(name = name, familyname = familyname, age = age, gender = gender, nationality = nationality)
        self.__school_uni_name = school
        self.__teaching_sbj_lst = []
        self.__teaching_sbj_lst.append(teaching_sbj)

    def set_school(self, school = None):
        self.__school_uni_name = school

    def set_teaching_sbj(self, teaching_sbj = None):
        self.__teaching_sbj = teaching_sbj

    def add_subject(self, teaching_sbj):
        self.__teaching_sbj_lst.append(teaching_sbj)

    #@staticmethod
    def get_info(self):
        #thisdict = dict(name = self.__name, familyname = self.__familyname, age = self.__age, gender = self.__gender, nationality = self.__nationality, school = self.__school_uni_name, teaching_subjects = self.__teaching_sbj) 
        thisdict = dict(name = self._Human__name, familyname = self._Human__familyname, age = self._Human__age, 
                        gender = self._Human__gender, nationality = self._Human__nationality, 
                        school = self.__school_uni_name, teaching_subjects = self.__teaching_sbj_lst) 

        return thisdict



if __name__ == "__main__":
    print('This module Users: Class Human; its methods: set_name, set_familyname, set_age, set_gender, set_nationality\n')
    print('Module Users: Class Student; methods: set_school and set_list_of_sbj\n')
    print('Module Users: Class Teacher; methods: set_school, set_teaching_sbj, add_subject\n')
