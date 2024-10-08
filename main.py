import time
from Calc import C_Y
import datetime
import tkinter as tk
import customtkinter as ctk
from PIL import Image
from auth import *
import os

# Constants
WINDOW_SIZE = 1080, 800
Factor = 0.3, 0.45
Pages_factor = 0.2


# Image and Path
imgs_path = 'imgs/'
ethronics_img = Image.open(os.path.join(imgs_path, 'ethronics.jpg'))
ethronics_icon = os.path.join(imgs_path, 'ethronics.ico')


# Default theme
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")


class FrontPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title('Ethronics - Feedback Form')

        self.iconbitmap(ethronics_icon)

        # Set window size
        self.after(0, lambda:self.state('zoomed'))
        # self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')

        # Load the Ethronics image
        self.ethronics_image = ctk.CTkImage(ethronics_img, size=(WINDOW_SIZE[0]*Factor[0], WINDOW_SIZE[0]*Factor[0]))

        # Create an image label
        self.image_label = ctk.CTkLabel(self, text="", image=self.ethronics_image)
        self.image_label.pack(pady=20)

        # Create the title label
        self.title_label = ctk.CTkLabel(self, text='Ethronics - Feedback Form', font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Create theme option
        self.theme_var = tk.StringVar(value="Light")
        self.theme_menu = ctk.CTkOptionMenu(self, values=["Light", "Dark"], variable=self.theme_var, command=self.change_theme)
        self.theme_menu.pack(pady=10)
        # Button to fill a feedback form (will lead to another page later)
        self.form_button = ctk.CTkButton(self, text="Fill Feedback Form", command=self.go_to_form)
        self.form_button.pack(pady=10)

        # Button to log in as teacher (will lead to login page)
        self.login_button = ctk.CTkButton(self, text="Teacher Login", command=self.go_to_login)
        self.login_button.pack(pady=10)

    def change_theme(self, new_theme):
        # Update the theme based on selection
        if new_theme == "Dark":
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def go_to_form(self):
        self.destroy()
        feedback_form = FeedbackForm()
        feedback_form.mainloop()

    def go_to_login(self):
        self.destroy()
        login_page = LoginPage()
        login_page.mainloop()



class LoginPage(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title('Ethronics - Teacher Login')

        # Set window size
        self.after(0, lambda:self.state('zoomed'))
        # self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')

        # Load the Ethronics image
        self.ethronics_image = ctk.CTkImage(ethronics_img, size=(WINDOW_SIZE[0]*Factor[0]*Pages_factor, WINDOW_SIZE[0]*Factor[0]*Pages_factor))

        # Create an image label
        self.image_label = ctk.CTkLabel(self, text="", image=self.ethronics_image)
        self.image_label.pack(pady=20)

        # Create the title label
        self.title_label = ctk.CTkLabel(self, text='Ethronics - Teacher Login', font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Create the teacher ID entry
        self.teacher_id_label = ctk.CTkLabel(self, text="Teacher ID")
        self.teacher_id_label.pack(pady=10)
        self.teacher_id_entry = ctk.CTkEntry(self)
        self.teacher_id_entry.pack(pady=10)

        # Create the password entry
        self.password_label = ctk.CTkLabel(self, text="Password")
        self.password_label.pack(pady=10)
        self.password_entry = ctk.CTkEntry(self, show="*")
        self.password_entry.pack(pady=10)

        # Button to log in
        self.login_button = ctk.CTkButton(self, text="Login", command=self.login)
        self.login_button.pack(pady=10)

        # Button to go back to front page
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.pack(pady=10)

    def login(self):
        teacher_id = self.teacher_id_entry.get()
        password = self.password_entry.get()

        teacher = get_teacher(teacher_id, password)
        if teacher:
            self.destroy()
            teacher_page = TeacherPage(teacher_id)
            teacher_page.mainloop()
        else:
            if getattr(self, 'login_popup', None):
                self.login_popup.destroy()
            self.login_popup = ctk.CTkToplevel(self, width=WINDOW_SIZE[0]*.5, height=WINDOW_SIZE[1]*.5)
            width, height = WINDOW_SIZE[0]*.3, WINDOW_SIZE[1]*.3
            self.login_popup.geometry("%dx%d+%d+%d" % (width, height, self.winfo_x() + width/4, self.winfo_y() + height/4))

            frm = ctk.CTkFrame(self.login_popup)
            frm.pack(fill='both', expand=False)
            label = ctk.CTkLabel(frm, text="Invalid credentials")
            label.pack(padx=4, pady=4)
            btnNo = ctk.CTkButton(frm, text='Ok', command=self.No)
            btnNo.pack()
            self.login_popup.after(100, self.login_popup.lift)
            self.login_popup.focus_force()

    def No(self):
        self.login_popup.destroy()

    def go_back(self):
        self.destroy()
        front_page = FrontPage()
        front_page.mainloop()
        

class TeacherPage(ctk.CTk):
    def __init__(self, teacher_id):
        super().__init__()
        self.teacher_id = teacher_id

        # Set the window title
        self.title('Ethronics - Teacher Page')

        # Set window size
        self.after(0, lambda:self.state('zoomed'))
        # self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')

        # Load the Ethronics image
        self.ethronics_image = ctk.CTkImage(ethronics_img, size=(WINDOW_SIZE[0]*Factor[0]*Pages_factor, WINDOW_SIZE[1]*Factor[1]*Pages_factor))

        # Create an image label
        self.image_label = ctk.CTkLabel(self, text="", image=self.ethronics_image, width=50)
        self.image_label.pack(pady=20)

        # Create the title label
        self.title_label = ctk.CTkLabel(self, text='Ethronics - Teacher Page', font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Button to view FeedBack
        self.view_feedback_button = ctk.CTkButton(self, text="View Feedback", command=lambda:[self.view_feedback(), self.Destroy_Btn()])
        self.view_feedback_button.pack(pady=10)

        # Button to log out
        self.logout_button = ctk.CTkButton(self, text="Logout", command=self.logout)
        self.logout_button.pack(pady=10)

    def Destroy_Btn(self):
        self.view_feedback_button.destroy()

    def view_feedback(self):
        # Placeholder function for viewing courses
        feedbacks = get_feedbacks(self.teacher_id)
        sections = [i['section_id'] for i in get_sections()]
        self.categorized = {section:{} for section in sections}
        for feedback in feedbacks:
            section = feedback['Section']
            self.categorized[section][feedback['form_id']] = feedback

        # Create a buttons for each section
        for section in sections:
            self.section_button = ctk.CTkButton(self, text=section, command=lambda section=section: self.view_feedback_section(section, self.categorized[section]))
            self.section_button.pack(pady=10)



    def view_feedback_section(self, section, feedbacks):
        self.destroy()
        
        feedback_page = FeedbackPage(section, feedbacks, self.teacher_id)
        
        feedback_page.mainloop()

    def logout(self):
        self.destroy()
        front_page = FrontPage()
        front_page.mainloop()


class FeedbackPage(ctk.CTk):
    def __init__(self, section, feedbacks, teacher_id):
        self.feedbacks = feedbacks
        C_Y(feedbacks)
        super().__init__()

        # Set the window title
        self.title('Ethronics - Feedback Page')
        self.teacher_id = teacher_id

        # Set window size
        self.after(0, lambda:self.state('zoomed'))
        # self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')

        # Button to go back to view analysis
        self.back_button = ctk.CTkButton(self, text="View Analysis", command=self.go_back, height=20, width=20)
        self.back_button.pack(side=ctk.TOP, anchor=ctk.W)

        # Button to go back to teacher page
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back, height=20, width=20)
        self.back_button.pack(side=ctk.RIGHT, anchor=ctk.N)

        # Load the Ethronics image
        self.ethronics_image = ctk.CTkImage(ethronics_img, size=(WINDOW_SIZE[0]*Factor[0]*Pages_factor, WINDOW_SIZE[1]*Factor[1]*Pages_factor))

        # Create an image label
        self.image_label = ctk.CTkLabel(self, text="", image=self.ethronics_image)
        self.image_label.pack(pady=20)

        # Create the title label
        self.title_label = ctk.CTkLabel(self, text=f'Ethronics - Feedback Page - {section}', font=("Arial", 20))
        self.title_label.pack(pady=10)

        self.FFOUTPUTS = ctk.CTkFrame(self, width=1000, height=450)
        self.FFOUTPUTS.pack()

        self.feedback_keys = list(feedbacks.keys())
        if len(self.feedback_keys):
            self.current_feedback_id = 0
            self.display_form(self.current_feedback_id)
        else:
            pass


    def display_form(self, f_id):
        self.current_feedback_id = f_id
        # Display the feedback form
        self.FFOUTPUTS.destroy()
        self.FFOUTPUTS = ctk.CTkFrame(self, width=1000, height=450)
        self.FFOUTPUTS.pack()
        questions_list = get_questions()
        self.questions_dict = {question['question_id']:question['question'] for question in questions_list}
        feedback = self.feedbacks[self.feedback_keys[f_id]]
        self.feedback_label = ctk.CTkLabel(self.FFOUTPUTS, text=f"Feedback from {feedback['Name'] or 'Anonymous'}")
        self.feedback_label.pack(pady=10)
        for key, value in feedback.items():
            if key in self.questions_dict:
                self.question_label = ctk.CTkLabel(self.FFOUTPUTS, text=f"{self.questions_dict[key]}: {value}")
                self.question_label.pack(pady=10)
        if self.current_feedback_id > 0:
            goBackButton = ctk.CTkButton(self, text='<', font=('bold', 50), text_color='Black', width=10, fg_color='transparent', hover_color='Light Gray', bg_color='transparent', command=lambda : self.display_form(f_id-1))
            goBackButton.place(x=300, y=300)

        if self.current_feedback_id < len(self.feedback_keys) - 1:
            nextButton = ctk.CTkButton(self, text='>', font=('bold', 50), text_color='Black', width=10, fg_color='transparent', hover_color='Light Gray', bg_color='transparent', command=lambda : self.display_form(f_id+1))
            nextButton.place(x=925, y=300)


    def go_back(self):
        self.destroy()
        teacher_page = TeacherPage(self.teacher_id)
        teacher_page.mainloop()


class FeedbackForm(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Set the window title
        self.title('Ethronics - Feedback Form')

        # Set window size
        self.after(0, lambda:self.state('zoomed'))
        # self.geometry(f'{WINDOW_SIZE[0]}x{WINDOW_SIZE[1]}')

        # Load the Ethronics image
        self.ethronics_image = ctk.CTkImage(ethronics_img, size=(WINDOW_SIZE[0]*Factor[0]*Pages_factor, WINDOW_SIZE[1]*Factor[1]*Pages_factor))

        # Create an image label
        self.image_label = ctk.CTkLabel(self, text="", image=self.ethronics_image)
        self.image_label.place(y=0, x=0)

        # Create the title label
        self.title_label = ctk.CTkLabel(self, text='Ethronics - Feedback Form', font=("Arial", 20))
        self.title_label.pack(pady=10)

        # Create the headers of the feeback
        HEADER_Y_POS = WINDOW_SIZE[0]*.05
        self.sections = get_sections() 
        section_names = [section['section_id'] for section in self.sections]
        self.selected_section = tk.StringVar(value="Choose section")
        self.section_name = ctk.CTkOptionMenu(self, values=section_names, variable=self.selected_section)
        self.section_name.place(y=HEADER_Y_POS, x=WINDOW_SIZE[1]*.15) 

        self.courses = get_courses() 
        course_names = [course['course_name'] for course in self.courses]
        self.selected_course = tk.StringVar(value="Choose course")
        self.class_name = ctk.CTkOptionMenu(self, values=course_names, variable=self.selected_course)
        self.class_name.place(y=HEADER_Y_POS, x=WINDOW_SIZE[1]*.4)


        self.name_label = ctk.CTkLabel(self, text="Enter your name(optional): ")
        self.name_label.place(y=HEADER_Y_POS, x=WINDOW_SIZE[1]*.65)
        self.name_entry = ctk.CTkEntry(self)
        self.name_entry.place(y=HEADER_Y_POS, x=WINDOW_SIZE[1]*.9)


        # Create the feedback form
        self.questions_list = get_questions()
        initialx, initialy = WINDOW_SIZE[0]*.1, WINDOW_SIZE[1]*.05
        increment_factor = 50
        x_increment_factor = 100
        x_increment_factor_rate = 175
        initialy_options = 550
        self.questions_response = {}
        for idx, question in enumerate(self.questions_list):
            question_text = f"{idx+1}. {question['question']}"
            question_type = question['type']
            question_id = question['question_id'],
            self.questions_response[question_id] = None
            if question_type == 'tickbox':
                options = question['options']
                question_label = ctk.CTkLabel(self, text=question_text)
                question_label.place(y=initialx+increment_factor*idx, x=initialy)
                radio_var = tk.StringVar(value='')
                for idx2, option in enumerate(options):
                    rb = ctk.CTkRadioButton(master=self, text=option, variable=radio_var, value=option)
                    rb.place(y=initialx+increment_factor*idx, x=initialy_options+x_increment_factor*idx2)
                self.questions_response[question_id] = radio_var
            elif question_type == 'rate':
                options = question['options']
                question_label = ctk.CTkLabel(self, text=question_text)
                question_label.place(y=initialx+increment_factor*idx, x=initialy)
                radio_var = tk.StringVar(value='')
                for idx2, option in enumerate(options):
                    rb = ctk.CTkRadioButton(master=self, text=option, variable=radio_var, value=option)
                    rb.place(y=initialx+increment_factor*idx, x=initialy_options+x_increment_factor_rate*idx2)
                self.questions_response[question_id] = radio_var
            else:
                question_label = ctk.CTkLabel(self, text=question_text)
                question_label.place(y=initialx+increment_factor*idx, x=initialy)
                question_entry = ctk.CTkEntry(self, width=400)
                question_entry.place(y=initialx+increment_factor*idx, x=initialy_options+initialy)
                self.questions_response[question_id] = question_entry

        # Button to submit feedback
        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.place(y=initialx+increment_factor*(idx+2), x=WINDOW_SIZE[1]*.8)

        # Button to go back to teacher page
        self.back_button = ctk.CTkButton(self, text="Back", command=self.go_back)
        self.back_button.place(y=initialx+increment_factor*(idx+3), x=WINDOW_SIZE[1]*.8)

    def submit(self):
        response_dict = {
            "Section": self.selected_section.get(),
            "Class": self.selected_course.get(),
            "Name": self.name_entry.get(),
        }
        response_dict.update({key[0]:value.get() for key, value in self.questions_response.items()})
        optionals = ["Name"]
        flag = any(response_dict[key]=="" for key in response_dict if key not in optionals)
        flag = flag or response_dict["Section"] == "Choose section" or response_dict["Class"] == "Choose course"

        if flag:
            if getattr(self, 'submit_popup', None):
                self.submit_popup.destroy()
            self.submit_popup = ctk.CTkToplevel(self, takefocus=True)
            width, height = WINDOW_SIZE[0]*.3, WINDOW_SIZE[1]*.3
            self.submit_popup.geometry("%dx%d+%d+%d" % (width, height, self.winfo_x() + width/4, self.winfo_y() + height/4))
            self.submit_popup.title("Error")
            self.submit_popup.resizable(False, False)
            self.submit_popup.attributes('-topmost', True)

            frm = ctk.CTkFrame(self.submit_popup)
            frm.pack(fill='both', expand=False)
            label = ctk.CTkLabel(frm, text="Missing data! Please Check")
            label.pack(padx=4, pady=4)
            btnNo = ctk.CTkButton(frm, text='Ok', command=self.No)
            btnNo.pack()
            self.submit_popup.after(100, self.submit_popup.lift)
            self.submit_popup.focus_force()
            self.submit_popup.mainloop()

        else:
            if getattr(self, 'submit_popup', None):
                self.submit_popup.destroy()
            self.submit_popup = ctk.CTkToplevel(self,  takefocus=True)
            width, height = WINDOW_SIZE[0]*.3, WINDOW_SIZE[1]*.3
            self.submit_popup.geometry("%dx%d+%d+%d" % (width, height, self.winfo_x() + width/4, self.winfo_y() + height/4))
            self.submit_popup.title("Confirm")
            self.submit_popup.resizable(False, False)
            self.submit_popup.attributes('-topmost', True)

            frm = ctk.CTkFrame(self.submit_popup)
            frm.pack(fill='both', expand=False)
            label = ctk.CTkLabel(frm, text="Are you sure?")
            label.pack(padx=4, pady=4)
            btnYes = ctk.CTkButton(frm, text='Yes', command=lambda : self.Yes(response_dict))
            btnYes.pack()
            btnNo = ctk.CTkButton(frm, text='No', command=self.No)
            btnNo.pack()
            self.submit_popup.after(100, self.submit_popup.lift)
            self.submit_popup.focus_force()
            self.submit_popup.mainloop()

    def Yes(self, response_dict):
        add_form(response_dict)

        self.submit_popup.destroy()
        self.submit_popup = ctk.CTkToplevel(self,  takefocus=True)
        width, height = WINDOW_SIZE[0]*.3, WINDOW_SIZE[1]*.3
        self.submit_popup.geometry("%dx%d+%d+%d" % (width, height, self.winfo_x() + width/4, self.winfo_y() + height/4))
        self.submit_popup.title("Success")
        frm = ctk.CTkFrame(self.submit_popup)
        frm.pack(fill='both', expand=False)
        label = ctk.CTkLabel(frm, text="Feedback submitted successfully")
        label.pack(padx=4, pady=4)
        

        self.submit_popup.resizable(False, False)
        self.submit_popup.attributes('-topmost', True)
        self.submit_popup.after(100, self.submit_popup.lift)
        self.submit_popup.focus_force()

        time.sleep(1)
        self.submit_popup.destroy()
        self.destroy()
        front_page = FrontPage()
        front_page.mainloop()

    def No(self):
        self.submit_popup.destroy()

    def go_back(self):
        self.destroy()
        front_page = FrontPage()
        front_page.after(0, lambda:front_page.state('zoomed'))
        front_page.mainloop()

def main():
    app = FrontPage()
    global WINDOW_SIZE
    WINDOW_SIZE = app.winfo_screenwidth(), app.winfo_screenheight()
    print(WINDOW_SIZE)
    app.mainloop()
    print()

if __name__ == '__main__':
    main()