from auth import *

def C_Y(forms):

    total_number = len(forms)
    
    question_values = {}
    for form in forms.values():
        for key in form.keys():
            if key.startswith("Q") and key != "Q008":
                question_values[key] = question_values.get(key, []) + [form[key]]


    question_values = {key:count_values(val) for key, val in question_values.items()}
        

    # print("Total number ", total_number)
    # for qv in question_values:
    #     print(qv, question_values[qv])

    return question_values

        
def recent_feedbacks(forms, count=None):
    sorted_forms = sorted([v for k,v in forms.items()], key=lambda x:x['date'], reverse=True)
    if count is None:
        count = len(sorted_forms)
    return sorted_forms[:count]

def count_values(question_value):
    dt = {}
    for i in question_value:
        if i in dt:
            dt[i] += 1
        else:
            dt[i] = 1

    return dt
    

if __name__ == "__main__":
    _T = {'Form 1': {'Section': 'E1', 'Class': 'Python', 'Name': 'bc', 'Q001': 'Yes', 'Q002': 'Yes', 'Q003': 'No', 'Q004': 'No', 'Q005': 'Somewhat Relevant', 'Q006': 'No Change', 'Q007': 'Extremely Interested', 'Q008': 'yoo', 'form_id': 'Form 1', 'date': '2024-09-19 11:01:45'}, 'Form 2': {'Section': 'E1', 'Class': 'Python', 'Name': 'r', 'Q001': 'No', 'Q002': 'No', 'Q003': 'Yes', 'Q004': 'No', 'Q005': 'Not relevant', 'Q006': 'No Change', 'Q007': 'Extremely Interested', 'Q008': 'Okay', 'form_id': 'Form 2', 'date': '2024-09-19 11:02:26'}, 'Form 3': {'Section': 'E1', 'Class': 'Python', 'Name': 'Book', 'Q001': 'Yes', 'Q002': 'No', 'Q003': 'Yes', 'Q004': 'Yes', 'Q005': 'Somewhat Relevant', 'Q006': 'Somewhat Changed', 'Q007': 'Not Interested', 'Q008': "I don't know", 'form_id': 'Form 3', 'date': '2024-09-19 11:03:07'}, 'Form 4': {'Section': 'E1', 'Class': 'Python', 'Name': '', 'Q001': 'Yes', 'Q002': 'Yes', 'Q003': 'Yes', 'Q004': 'Yes', 'Q005': 'Not relevant', 'Q006': 'No Change', 'Q007': 'Not Interested', 'Q008': 'Yes, I really recommend Ethronics-IRAS to others', 'form_id': 'Form 4', 'date': '2024-09-19 11:09:18'}}
    print(C_Y(_T))
    print(recent_feedbacks(_T, 2))
    