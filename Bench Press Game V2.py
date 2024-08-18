#Project: 3PAD Assignment V2
#Date: 20/06/2024
#Author: Kishan Patel
#Purpose: Make a maths game for a company for kids to learn.
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random

class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400') # Window size.
        self.resizable(0, 0) # Stops the window size being changed.
        self.title('IKRAAMS BENCH SIMULATOR') # Window title.

        frame = tk.Frame(self, bg='#333333') # Background colour for window.
        frame.place(relwidth=1, relheight=1) 
        login_label = tk.Label(frame, text="Login", bg='#333333', fg="#E85D04", font=("Arial", 30)) # Creates login label.
        username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16)) # Creates a username label.
        self.username_entry = tk.Entry(frame, font=("Arial", 16)) # User is able to enter their username.
        password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16)) # Creates a password label.
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 16)) # User is able to enter their password.
        login_button = tk.Button(frame, text="Login", bg="#E85D04", fg="#FFFFFF", font=("Arial", 16), command=self.validate_login) # User clicks login button to create next window and start game.

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) # Position of login label.
        username_label.grid(row=1, column=0) # Position of userneame label.
        self.username_entry.grid(row=1, column=1, pady=20) # Position of username entry box.
        password_label.grid(row=2, column=0) # Position of password label.
        self.password_entry.grid(row=2, column=1, pady=20) # Position of password entry box.
        login_button.grid(row=3, column=0, columnspan=2, pady=30) # Position of login button.

    def open_start_window(self): # Selection of weight window.
        start_window = tk.Toplevel() 
        start_window.config(bg="#333333") # Background colour for window.
        start_window.title('Start Window') # Window title.
        start_window.geometry('400x300') # Window size.
        start_window.resizable(0, 0) # Stops the window size being changed.

        def exit_window():
            start_window.destroy() 

        current_value = tk.IntVar()
        text_value = tk.StringVar()
        text_value.set("20")

        def slider_changed(event):
            proper_value = current_value.get()
            value_entry.config(state='normal')
            text_value.set(str(proper_value))
            value_entry.config(state='readonly')

        slider_label = ttk.Label(start_window, text='HOW MUCH WEIGHT CAN YOU BENCH !!!', font=("Arial", 15), background="#333333", foreground="#E85D04")
        slider_label.pack(pady=10)

        value_entry = ttk.Entry(start_window, font=("Arial", 20), justify='center', state='readonly', textvariable=text_value, foreground="#333333")
        value_entry.pack(pady=10)

        slider_label = ttk.Label(start_window, text='KG', font=("Arial", 15))
        slider_label.place(x=225, y=65)

        slider = tk.Scale(
            start_window,
            from_=20,
            to=120,
            showvalue=False,
            orient='horizontal',
            command=slider_changed,
            variable=current_value,
            resolution=20
        )
        slider.pack(pady=10)

        another_game_button = tk.Button(start_window, text='SELECT', bg="#E85D04", fg="#FFFFFF", font=("Arial", 10), command=lambda: self.open_another_game_window(current_value.get()))
        another_game_button.place(x=100, y=240)

        exit_button = tk.Button(start_window, text='Exit', bg="#E85D04", fg="#FFFFFF", font=("Arial", 10), command=exit_window)
        exit_button.place(x=240, y=240)

    def open_another_game_window(self, weight):
        game_window = tk.Toplevel()
        game_window.config(bg="#333333")
        game_window.title('Bench Press Game')
        game_window.geometry('400x300')
        game_window.resizable(0, 0)

        question_label = tk.Label(game_window, bg='#333333', fg='#E85D04', font=("Arial", 18))
        question_label.pack(pady=20)

        feedback_label = tk.Label(game_window, bg='#333333', fg='#FFFFFF', font=("Arial", 14))
        feedback_label.pack(pady=10)

        box1 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3)
        box1.place(relx=0.0, rely=0.632)

        box2 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3)
        box2.place(relx=0.29, rely=0.632, anchor='nw')

        box3 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3)
        box3.place(relx=0.0, rely=0.82)

        box4 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3)
        box4.place(relx=0.29, rely=0.82, anchor='nw')

        buttons = [box1, box2, box3, box4]

        def generate_question():
            if weight == 20:
                num1 = random.randint(1, 10)
                num2 = random.randint(1, 10)
                operation = '+'
                correct_answer = num1 + num2
            elif weight == 40:
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 20)
                operation = random.choice(['+', '-'])
                correct_answer = num1 + num2 if operation == '+' else num1 - num2
            elif weight == 60:
                num1 = random.randint(1, 30)
                num2 = random.randint(1, 30)
                operation = random.choice(['+', '-', '*'])
                correct_answer = num1 + num2 if operation == '+' else (num1 - num2 if operation == '-' else num1 * num2)
            elif weight == 80:
                num1 = random.randint(1, 50)
                num2 = random.randint(1, 50)
                operation = random.choice(['+', '-', '*'])
                correct_answer = num1 + num2 if operation == '+' else (num1 - num2 if operation == '-' else num1 * num2)
            elif weight == 100:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 10)
                operation = random.choice(['+', '-', '*', '//'])
                correct_answer = num1 + num2 if operation == '+' else (num1 - num2 if operation == '-' else (num1 * num2 if operation == '*' else num1 // num2))
            elif weight == 120:
                num1 = random.randint(50, 150)
                num2 = random.randint(1, 20)
                operation = random.choice(['+', '-', '*', '//'])
                correct_answer = num1 + num2 if operation == '+' else (num1 - num2 if operation == '-' else (num1 * num2 if operation == '*' else num1 // num2))
            
            answers = [correct_answer, correct_answer + random.randint(1, 10), correct_answer - random.randint(1, 10), correct_answer + random.randint(11, 20)]
            random.shuffle(answers)

            question_label.config(text=f'What is {num1} {operation} {num2}?')

            for i, btn in enumerate(buttons):
                btn.config(text=f'{answers[i]}', command=lambda ans=answers[i]: check_answer(ans, correct_answer))

        def check_answer(selected_answer, correct_answer):
            if selected_answer == correct_answer:
                feedback_label.config(text="Correct!", fg="#00FF00")
                feedback_label.place(relx=0.57, rely=0.75, anchor='nw')
            else:
                feedback_label.config(text="Incorrect. Try again!", fg="#FF0000")
                feedback_label.place(relx=0.57, rely=0.75, anchor='nw')
            generate_question()

        generate_question()

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username.isalpha():
            messagebox.showwarning("Error", "Please enter a valid username (alphabetic characters only).")
        elif len(password) < 7:
            messagebox.showwarning("Error", "Password must be at least 7 characters long.")
        else:
            self.open_start_window()
            self.withdraw()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
