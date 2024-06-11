import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as font

# Main window
class Main(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x400')
        self.resizable(0, 0)
        self.title('Login Page')

        frame = tk.Frame(self, bg='#333333')
        frame.place(relwidth=1, relheight=1)

        login_label = tk.Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
        username_label = tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.username_entry = tk.Entry(frame, font=("Arial", 16))
        password_label = tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
        login_button = tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=self.validate_login)

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
        username_label.grid(row=1, column=0)
        self.username_entry.grid(row=1, column=1, pady=20)
        password_label.grid(row=2, column=0)
        self.password_entry.grid(row=2, column=1, pady=20)
        login_button.grid(row=3, column=0, columnspan=2, pady=30)

        self.mainloop()

    def open_start_window(self):
        start_window = tk.Toplevel(self)
        start_window.title('Start Window')
        start_window.geometry('400x300')
        start_window.resizable(0, 0)

        def exit_window():
            start_window.destroy()

        current_value = tk.IntVar()

        def slider_changed(event):
            proper_value = current_value.get()
            value_entry.config(state='normal')
            value_entry.delete(0, tk.END)
            value_entry.insert(0, proper_value)
            value_entry.config(state='readonly')

        slider_label = ttk.Label(start_window, text='HOW MUCH WEIGHT CAN YOU BENCH !!!:')
        slider_label.pack(pady=10)

        value_entry = ttk.Entry(start_window, font=("Arial", 20), justify='center', state='readonly')
        value_entry.pack(pady=10)

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

        exit_button = tk.Button(start_window, text='Exit', command=exit_window)
        exit_button.place(x=160, y=240)

    def validate_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username.isalpha():
            messagebox.showwarning("Error", "Please enter a valid username (alphabetic characters only).")
        elif len(password) < 7:  # Example password criteria
            messagebox.showwarning("Error", "Password must be at least 7 characters long.")
        else:
            self.open_start_window()

if __name__ == "__main__":
    app = Main()
