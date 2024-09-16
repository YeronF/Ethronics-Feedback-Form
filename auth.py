import json
import os

data_path = "data"

def reload_data():
    global Teachers, Courses, Questions

    Teachers = json.load(open(os.path.join(data_path, 'teachers.json')))
    Courses = json.load(open(os.path.join(data_path, 'courses.json')))
    Questions = json.load(open(os.path.join(data_path, 'questions.json')))
    Forms = json.load(open(os.path.join(data_path, 'forms.json')))
    Sections = json.load(open(os.path.join(data_path, 'sections.json')))

Teachers = json.load(open(os.path.join(data_path, 'teachers.json')))
Courses = json.load(open(os.path.join(data_path, 'courses.json')))
Questions = json.load(open(os.path.join(data_path, 'questions.json')))
Forms = json.load(open(os.path.join(data_path, 'forms.json')))
Sections = json.load(open(os.path.join(data_path, 'sections.json')))


def get_teacher(teacher_id, password):
    for teacher in Teachers:
        if teacher['teacher_id'] == teacher_id and teacher['password'] == password:
            return teacher
        
def add_teacher(teacher_id, password, name):
    try:
        Teachers.append({
            'teacher_id': teacher_id,
            'password': password,
            'name': name
        })
        json.dump(Teachers, open(os.path.join(data_path, 'teachers.json'), 'w'))
    except:
        return False


def get_course(course_id):
    for course in Courses:
        if course['course_id'] == course_id:
            return course
        
    return None

def add_course(course_id, name, teacher_id):
    Courses.append({
        'course_id': course_id,
        'name': name,
        'teacher_id': teacher_id
    })
    json.dump(Courses, open(os.path.join(data_path, 'courses.json'), 'w'))

def get_teacher_courses(teacher_id):
    return [course for course in Courses if course['teacher_id'] == teacher_id]

def get_questions():
    return Questions

def get_courses():
    return Courses

def get_sections():
    return Sections

def add_form(form):
    form_id = "Form "+ str(len(Forms) + 1)
    form['form_id'] = form_id
    Forms.append(form)
    json.dump(Forms, open(os.path.join(data_path, 'forms.json'), 'w'))

def get_feedbacks(teacher_id):
    feedback_course = None
    for course in Courses:
        if course['taught_by'] == teacher_id:
            feedback_course = course
            break
    else:
        return "None found"
    
    result = []
    for form in Forms:
        if form['Class'] == feedback_course['course_name']:
            result.append(form)


    return result