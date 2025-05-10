from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import ast

root = Tk()
root.title('Login System')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False, False)

def signin():
    username = user.get()
    password = code.get()

    try:
        with open('datasheet.txt', 'r') as file:
            data = file.read()
            users = ast.literal_eval(data)
    except:
        users = {}

    if username in users and password == users[username]:
        open_loan_form()
    else:
        messagebox.showerror('Invalid', 'Invalid username or password')

def signup_command():
    def signup():
        username = user.get()
        password = code.get()
        confirm_password = confirm_code.get()

        if password == confirm_password and username and username != "Username":
            try:
                with open('datasheet.txt', 'r') as file:
                    data = file.read()
                    users = ast.literal_eval(data)
            except:
                users = {}

            users[username] = password
            with open('datasheet.txt', 'w') as file:
                file.write(str(users))

            messagebox.showinfo('Sign up', 'Successfully signed up')
            window.destroy()
        else:
            messagebox.showerror('Error', 'Passwords do not match or invalid username')

    def switch_to_signin():
        window.destroy()

    window = Toplevel(root)
    window.title('Sign Up')
    window.geometry('925x500+300+200')
    window.configure(bg="#fff")
    window.resizable(False, False)

    try:
        img = PhotoImage(file='login2.png')
        Label(window, image=img, border=0, bg='white').place(x=50, y=90)
    except Exception:
        # If image file not found, ignore
        pass

    frame = Frame(window, width=350, height=390, bg="#fff")
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    def on_enter(e): user.delete(0, 'end')
    def on_leave(e): user.insert(0, 'Username') if user.get() == '' else None

    user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, 'Username')
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

    def on_enter(e): code.delete(0, 'end')
    def on_leave(e): code.insert(0, 'Password') if code.get() == '' else None

    code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11), )
    code.place(x=30, y=150)
    code.insert(0, 'Password')
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

    def on_enter(e): confirm_code.delete(0, 'end')
    def on_leave(e): confirm_code.insert(0, 'Confirm Password') if confirm_code.get() == '' else None

    confirm_code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11), )
    confirm_code.place(x=30, y=220)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind('<FocusIn>', on_enter)
    confirm_code.bind('<FocusOut>', on_leave)
    Frame(frame, width=295, height=2, bg="black").place(x=25, y=247)

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)

    label = Label(frame, text="I have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
    label.place(x=90, y=340)

    signin_btn = Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=switch_to_signin)
    signin_btn.place(x=200, y=340)

    window.mainloop()

def open_summary_page():
    summary_window = Toplevel(root)
    summary_window.title('Application Summary')
    summary_window.geometry('600x400+300+200')
    summary_window.configure(bg="#fff")
    summary_window.resizable(False, False)

    frame = Frame(summary_window, bg="white")
    frame.pack(pady=20, padx=10, fill=BOTH, expand=True)

    heading = Label(frame, text='Loan Application Summary', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.pack(pady=10)

    # Create a Text widget to display the summary with vertical scrollbar
    scrollbar = Scrollbar(frame)
    scrollbar.pack(side=RIGHT, fill=Y)

    summary_text = Text(frame, width=70, height=15, bg="lightgrey", fg="black", font=('Microsoft YaHei UI Light', 11), yscrollcommand=scrollbar.set)
    summary_text.pack(pady=10, fill=BOTH, expand=True)
    scrollbar.config(command=summary_text.yview)

    # Read the loan applications from the file
    try:
        with open("loan_applications.txt", "r") as f:
            applications = f.read()
            if applications.strip():
                summary_text.insert(END, applications)
            else:
                summary_text.insert(END, "No applications found.")
    except FileNotFoundError:
        summary_text.insert(END, "No applications found.")

    # Disable editing of summary text
    summary_text.config(state=DISABLED)

    # Add a button to close the summary window
    close_button = Button(frame, text='Close', command=summary_window.destroy, bg='#57a1f8', fg='white')
    close_button.pack(pady=10)

def open_loan_form():
    screen = Toplevel(root)
    screen.title('Loan Application')
    screen.geometry('925x600+300+200')
    screen.configure(bg="#fff")
    screen.resizable(False, False)

    try:
        img = PhotoImage(file='login.png')
        Label(screen, image=img, bg='white').place(x=50, y=100)
    except Exception:
        pass

    frame = Frame(screen, width=350, height=500, bg="white")
    frame.place(x=480, y=70)

    heading = Label(frame, text='Loan Application Form', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=10, y=3)

    def make_entry(y, text):
        def on_enter(e): entry.delete(0, 'end')
        def on_leave(e): entry.insert(0, text) if entry.get() == '' else None

        entry = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        entry.place(x=30, y=y)
        entry.insert(0, text)
        entry.bind('<FocusIn>', on_enter)
        entry.bind('<FocusOut>', on_leave)
        Frame(frame, width=295, height=2, bg="black").place(x=25, y=y+27)
        return entry

    name_entry = make_entry(80, 'Applicant Name')
    age_entry = make_entry(150, 'Age')
    income_entry = make_entry(220, 'Monthly Income')
    loan_amount_entry = make_entry(290, 'Loan Amount')

    combo = Combobox(screen, width=45)
    combo['values'] = ("Home Loan", "Car Loan", "Personal Loan", "Education Loan")
    combo.place(x=510, y=420)

    def submit_application():
        name = name_entry.get()
        age_str = age_entry.get()
        income_str = income_entry.get()
        loan_amount_str = loan_amount_entry.get()
        loan_type = combo.get()

        errors = []

        try:
            age = int(age_str)
            if not (18 <= age <= 65):
                errors.append("Age must be between 18 and 65.")
        except ValueError:
            errors.append("Invalid age entered.")

        try:
            income = float(income_str)
            if income <= 0:
                errors.append("Income must be a positive number.")
        except ValueError:
            errors.append("Invalid income entered.")

        try:
            loan_amount = float(loan_amount_str)
            if loan_amount <= 0:
                errors.append("Loan amount must be positive.")
        except ValueError:
            errors.append("Invalid loan amount entered.")

        if not name or name == "Applicant Name":
            errors.append("Please enter applicant name.")
        if not loan_type:
            errors.append("Please select a loan type.")

        if not errors:
            min_income_map = {
                "Home Loan": 3000,
                "Car Loan": 2000,
                "Personal Loan": 1500,
                "Education Loan": 1000,
            }
            if income < min_income_map[loan_type]:
                errors.append(f"Minimum income for {loan_type} is ${min_income_map[loan_type]}.")

            if loan_amount > income * 20:
                errors.append(f"Loan amount exceeds allowed maximum (${income*20:.2f}).")

        if errors:
            messagebox.showerror("Validation Error", "\n".join(errors))
        else:
            with open("loan_applications.txt", "a") as f:
                f.write(f"Name: {name}\n")
                f.write(f"Age: {age}\n")
                f.write(f"Monthly Income: ${income:.2f}\n")
                f.write(f"Loan Amount: ${loan_amount:.2f}\n")
                f.write(f"Loan Type: {loan_type}\n")
                f.write("-" * 40 + "\n")
            messagebox.showinfo("Success", "Application Submitted and Saved Successfully!")

    Button(frame, width=39, pady=7, text='Submit', bg='#57a1f8', relief="raised", fg='white', border=0, command=submit_application).place(x=35, y=420)

    # New button to open summary page
    Button(frame, width=39, pady=7, text='View Applications', bg='#57a1f8', relief="raised", fg='white', border=0, command=open_summary_page).place(x=35, y=460)

    screen.mainloop()

# Main login window UI setup
try:
    img = PhotoImage(file='login.png')
    Label(root, image=img, bg='white').place(x=50, y=50)
except Exception:
    pass

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Sign in', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
heading.place(x=100, y=5)

def on_enter(e): user.delete(0, 'end')
def on_leave(e): user.insert(0, 'Username') if user.get() == '' else None

user = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

def on_enter(e): code.delete(0, 'end')
def on_leave(e): code.insert(0, 'Password') if code.get() == '' else None

code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11), )
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=75, y=270)

sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=signup_command)
sign_up.place(x=215, y=270)

root.mainloop()
