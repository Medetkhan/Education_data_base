print('Module organizations is successfully imported')
#import users
import csv

class School():
    def __init__(self, school_name = None,
                       school_adr = None,
                       school_tel = None,
                       school_email = None,
                       students_num = None,
                       teachers_num = None):
        self.__school_name = school_name
        self.__school_adr = school_adr
        self.__school_tel = school_tel
        self.__school_email = school_email
        self.__students_num = students_num
        self.__teachers_num = teachers_num
        self.students = []
        self.teachers = []
        
        self.thisdict_school = dict(name = self.__school_name, school_address = self.__school_adr,
                        school_phone_num = self.__school_tel, school_email = self.__school_email,
                        students_number = self.__students_num, teachers_number = self.__teachers_num)

    def set_name(self, school_name = None):
        self.__school_name = school_name
    def set_address(self, school_adr = None):
        self.__school_adr = school_adr
    def set_phone(self, school_tel = None):
        self.__school_tel = school_tel
    def set_email(self, school_email = None):
        self.__school_email = school_email
    def set_num_stud(self, students_num = None):
        self.__students_num = students_num
    def set_num_teachers(self, teachers_num = None):
        self.__teachers_num = teachers_num
    
    def add_student(self, student):
        self.students.append(student)
        
    def add_teacher(self, teacher):
        self.teachers.append(teacher)
    

    def get_info(self):
        student_info = [s.get_info() for s in self.students]
        teacher_info = [t.get_info() for t in self.teachers]
        thisdict_school = dict(name = self.__school_name, school_address = self.__school_adr,
                        school_phone_num = self.__school_tel, school_email = self.__school_email,
                        students_number = self.__students_num, teachers_number = self.__teachers_num)
        return thisdict_school, student_info, teacher_info

    def get_report(self):
        
        # Write the school info to the CSV file
        with open('school_info.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(self.thisdict_school.keys())
            writer.writerow(self.thisdict_school.values())

        # Write the student info to the CSV file
        with open('school_info.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([])
            writer.writerow(['Teachers Information'])
            writer.writerow(['name', 'familyname', 'age', 'gender', 'nationality', 'school', 'teaching_sbj'])
            for prepod in self.teachers:
                writer.writerow([prepod._Human__name, prepod._Human__familyname, prepod._Human__age, prepod._Human__gender, 
                                 prepod._Human__nationality, prepod._Teacher__school_uni_name, prepod._Teacher__teaching_sbj_lst])
            
            writer.writerow([])  # add an empty row for clarity
            writer.writerow(['Student Information'])
            writer.writerow(['Name', 'Family Name', 'Age', 'Gender', 'Nationality', 'School', 'List of Subjects'])
            for stud in self.students:
                writer.writerow([stud._Human__name, stud._Human__familyname, stud._Human__age, stud._Human__gender,
                                 stud._Human__nationality, stud._Student__school, stud._Student__list_of_subjects])

if __name__ == "__main__":
    
    print('This module organizations: Class School; its methods: set_name, set_address, set_phone, set_email, set_num_students, set_num_teachers\n')
    


