# Create class for student and course
class student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob
    def print_student(self):
        print(f"{self.id}\n{self.name}\n{self.dob}")
        
class course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name
    def print_course(self):
        print(f"{self.course_id}\n{self.course_name}")
            
# Input number of students in a class
def input_number_of_students():
    return int(input("Enter number of students: "))
    
# Input student information: id, name, DoB
def input_student_information():
    return {'id': str(input(f"Enter student id: ")),
            'name': str(input(f"Enter student name: ")),
            'dob': str(input(f"Enter student date of birth: "))}

# Input number of courses
def input_number_of_courses():
    return int(input("Enter number of courses: "))

# Input course information: id, name
def input_course_information():
    return {'id': str(input("Enter course id: ")),
            'name': str(input("Enter course name: "))}

# Select a course, input marks for student in this course
def update_marks_of_course(course):
    print(f"Enter marks for the course {course['name']}: ")
    course['marks'] = []

    for student in students:
        course['marks'].append((student, input(f"Enter mark for student {student['name']}: ")))

# List courses
def list_courses():
    print('Listing available courses: ')

    for course in courses:
        print(f"- [{course['id']}] {course['name']}", end='')
        print(' (mark available)' if 'marks' in course else '')

# List students
def list_students():
    print('Listing students: ')
    print(f'{"ID":^10}{"DATE OF BIRTH":^15}{"NAME":^20}')

    for student in students:
        print(f"{student['id']:^10}{student['dob']:^15}{student['name']:>20}")
    
    print()

# Show student marks for a given course
def show_marks_of_course(course):
    if 'marks' in course:
        print(f"Show marks of the course {course['name']}: ")

        print(f'{"NAME":^20}{"MARK":^5}')
        for student, mark in course['marks']:
            print(f"{student['name']:<20}{mark:>5}")
    else:
        print('This course has no marks.')

def select_course_prompt(intro_message):
    list_courses()
    print(intro_message)
    return input('Choose a course (Enter nothing to skip): ')

def search(List, keyword):
    for item in List:
        if keyword in item.values():
            return item
    empty_item = List[0].copy()
    empty_item.clear()
    return empty_item

def action_loop(msg=None, callback=None):
    while True:
        keyword = select_course_prompt(f'-> {msg}')
        if not keyword:
            print()
            break
        callback(search(courses, keyword))
        print()

if __name__ == '__main__':
    students = []
    courses = []
    for _ in range(input_number_of_students()):
        students.append(input_student_information())
    
    for _ in range(input_number_of_courses()):
        courses.append(input_course_information())
    
    list_students()
    action_loop(msg='Marking course...', callback=update_marks_of_course)
    action_loop(msg='Select a course...', callback=show_marks_of_course)

    print("Goodbye")
