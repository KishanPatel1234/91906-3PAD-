'''
Name: Kishan Patel
Program: Bench Press Game V4.py
Date: 2/09/2024
AS91906
game is to help students improve their maths skills using a bench press game
'''
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import random
import os

GIF_START_FRAME = 0 # First Gif Frame. 
GIF_END_FRAME = 26 # Last Gif Frame
SCORE_FILE = "scores.txt"  # File to store scores.
'''This class opens the main menu'''
class MainApp(tk.Tk): 

    def __init__(self):
        ''' Loads the user name login and password '''
        super().__init__()
        self.geometry('400x400') # Window size.
        self.resizable(0, 0) # Stops the window size being changed.
        self.title('IKRAAMS BENCH SIMULATOR') # Window title.

        self.current_frame = 0 
        self.scores = self.load_scores()  # Load scores from the file.
        
        frame = tk.Frame(self, bg='#333333') # Background colour for window.
        frame.place(relwidth=1, relheight=1) # Position of frame. 
        login_label = tk.Label(frame, text="Login", bg='#333333', fg="#E85D04", font=("Elephant", 30)) # Creates login label.
        username_label = tk.Label(frame, text="Username", bg='#333333', fg="#E85D04", font=("Arial", 16)) # Creates a username label.
        self.username_entry = tk.Entry(frame, font=("Arial", 16)) # User is able to enter their username.
        password_label = tk.Label(frame, text="Password", bg='#333333', fg="#E85D04", font=("Arial", 16)) # Creates a password label.
        self.password_entry = tk.Entry(frame, show="*", font=("Arial", 16)) # User is able to enter their password.
        login_button = tk.Button(frame, text="Login", bg="#E85D04", fg="#FFFFFF", font=("Arial", 16), command=self.validate_login) # User clicks login button to create next window and start game.

        login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40) # Position of login label.
        username_label.grid(row=1, column=0) # Position of username label.
        self.username_entry.grid(row=1, column=1, pady=20) # Position of username entry box.
        password_label.grid(row=2, column=0) # Position of password label.
        self.password_entry.grid(row=2, column=1, pady=20) # Position of password entry box.
        login_button.grid(row=3, column=0, columnspan=2, pady=30) # Position of login button.
        
    def load_scores(self): 
        ''' Load scores from a file.'''
        if not os.path.exists(SCORE_FILE): # Makes sure file exists
            return []
        with open(SCORE_FILE, "r") as file: # Opens the score file.
            scores = [line.strip().split(",") for line in file.readlines()] # Writes the users score.
            return [(user, int(score)) for user, score in scores] 

    def save_scores(self):
        ''' Save scores to a file.'''
        with open(SCORE_FILE, "w") as file: # Opens the score file
            for user, score in self.scores:
                file.write(f"{user},{score}\n") # Writes users score into file.

    def open_start_window(self):
        ''' starts the login page '''
        start_window = tk.Toplevel() 
        start_window.config(bg="#333333") # Background colour for window.
        start_window.title('Start Window') # Window title.
        start_window.geometry('400x300') # Window size.
        start_window.resizable(0, 0) # Stops the window size being changed.

        def exit_window():
            ''' Destroys window once logged in. '''
            start_window.destroy() # Destroys start window to move into the weight selection window

        current_value = tk.IntVar() 
        text_value = tk.StringVar()
        text_value.set("20") # Weight goes up in 20kgs

        def slider_changed(event):
            ''' Creates a slider to select weights'''
            proper_value = current_value.get() 
            value_entry.config(state='normal') 
            text_value.set(str(proper_value)) 
            value_entry.config(state='readonly') # Value entry is only read only.

        slider_label = ttk.Label(start_window, text='HOW MUCH WEIGHT CAN YOU BENCH !!!', font=("Arial", 15), background="#333333", foreground="#E85D04") # How much can you bench label.
        slider_label.pack(pady=10) # Position of label

        value_entry = ttk.Entry(start_window, font=("Arial", 20), justify='center', state='readonly', textvariable=text_value, foreground="#333333") # Weight Value.
        value_entry.pack(pady=10) # Position of weight value.

        slider_label = ttk.Label(start_window, text='KG', font=("Arial", 15)) # KG label.
        slider_label.place(x=225, y=65) # Position of label.

        slider = tk.Scale( 
            start_window, 
            from_=20, # Start of slider 20kg.
            to=120, # End of slider 120kg
            showvalue=False,
            orient='horizontal', # Slider orientation.
            command=slider_changed,
            variable=current_value, 
            background="#d90429", # Colour of slider
            resolution=20 # Resolution of slider.
        )
        slider.pack(pady=10) # Position of slider.

        select_game_button = tk.Button(start_window, text='SELECT', bg="#E85D04", fg="#FFFFFF", font=("Arial", 10), command=lambda: self.open_game_window(current_value.get())) # Select weight button created.
        select_game_button.place(x=100, y=240) # Postion of select button.

        exit_button = tk.Button(start_window, text='Exit', bg="#E85D04", fg="#FFFFFF", font=("Arial", 10), command=exit_window) # Exit button created.
        exit_button.place(x=240, y=240) # Placement of exit button.

    def open_game_window(self, weight):
        ''' Opens game window.'''
        game_window = tk.Toplevel() 
        game_window.config(bg="#333333") # Backround colour for game window.
        game_window.title('Bench Press Game') # Game window title.
        game_window.geometry('400x300') # Size of game window.
        game_window.resizable(0, 0) # Stops the window size being changed.

        self.main_canvas = tk.Canvas(game_window, width=400, height=300, bg="#333333", borderwidth=0, highlightthickness=0) # Creates a canavs
        self.main_canvas.place(y=0, x=0) # Position of canvas

        question_label = tk.Label(game_window, bg='#333333', fg='#FFFFFF', font=("Arial", 18)) # Creates question label.
        question_label.place(y=0) # Position of question label. 

        feedback_label = tk.Label(game_window, bg='#333333', fg='#FFFFFF', font=("Arial", 14)) # Creates feedback label.

        self.frame_image = tk.PhotoImage(file="bench.gif", format="gif -index 1") # Creates my gif onto game.
        self.main_canvas.create_image(10,10, anchor="nw", image=self.frame_image) # Position of gif.
        
        
        self.timer_label = tk.Label(game_window, text="Time Left: 30", font=("Arial", 14), bg='#333333', fg='#FFFFFF') # 30 second time label.
        self.timer_label.place(relx=0.7, rely=0.0) # Position of time label.
        
        self.time_left = 30 # Ammount of time to answer questions.
        self.score = 0 # Starting score.

        box1 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3) # 1st box with an answer.
        box1.place(relx=0.0, rely=0.632) # Position of first box.

        box2 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3) # 2nd box with an answer
        box2.place(relx=0.29, rely=0.632, anchor='nw') # Position of second box.

        box3 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3) # 3rd box with an answer.
        box3.place(relx=0.0, rely=0.82) # Position of third box.

        box4 = tk.Button(game_window, bg='#E85D04', fg='white', width=15, height=3) # 4th box with an answer.
        box4.place(relx=0.29, rely=0.82, anchor='nw') # Position of fourth box.

        buttons = [box1, box2, box3, box4] 

        def generate_question():
            ''' Generate questions.'''
            if weight == 20: # Selection of weight is 20kg.
                number_1 = random.randint(1, 10) # First number between 1 - 10. 
                number_2 = random.randint(1, 10) # Second number between 1 - 10.
                Maths_operation = '+' # Only addition questions.
                answer = number_1 + number_2 # Correct answer both numbers added.
            elif weight == 40: # Selection of weight is 40kg.
                number_1 = random.randint(1, 20) # First number between 1 - 20.
                number_2 = random.randint(1, 20) # Second number between 1 - 20.
                Maths_operation = random.choice(['+', '-']) # Addition and subtraction questions.
                answer = number_1 + number_2 if Maths_operation == '+' else number_1 - number_2 # Correct answer both numbers added or subtracted.
            elif weight == 60: # Selection of weight is 60kg.
                number_1 = random.randint(1, 30) # First number between 1 - 30.
                number_2 = random.randint(1, 30) # Second number between 1 - 30.
                Maths_operation = random.choice(['+', '-', '*']) # Addition, subtraction and multiplication questions.
                answer = number_1 + number_2 if Maths_operation == '+' else (number_1 - number_2 if Maths_operation == '-' else number_1 * number_2) # Correct answer both numbers added, subtracted or multiplied.
            elif weight == 80: # Selection of weight is 80kg.
                number_1 = random.randint(1, 50) # First number between 1 - 50.
                number_2 = random.randint(1, 50) # Second number between 1 - 50.
                Maths_operation = random.choice(['+', '-', '*']) # Addition, subtraction and multiplication questions.
                answer = number_1 + number_2 if Maths_operation == '+' else (number_1 - number_2 if Maths_operation == '-' else number_1 * number_2) # Correct answer both numbers added, subtracted or multiplied.
            elif weight == 100: # Selection of weight is 100kg.
                number_1 = random.randint(1, 100) # First number between 1 - 100.
                number_2 = random.randint(1, 10)  # second number between 1 - 10.
                Maths_operation = random.choice(['+', '-', '*', '//']) # Addition, subtraction, multiplication and division questions.
                answer = number_1 + number_2 if Maths_operation == '+' else (number_1 - number_2 if Maths_operation == '-' else (number_1 * number_2 if Maths_operation == '*' else number_1 // number_2))  # Correct answer both numbers added,subtracted,multiplied or divided.
            elif weight == 120: # Selection of weight is 120kg.
                number_1 = random.randint(50, 150) # First number between 1 - 150.
                number_2 = random.randint(1, 20) # second number between 1 - 20.
                Maths_operation = random.choice(['+', '-', '*', '//']) # Addition, subtraction, multiplication and division questions.
                answer = number_1 + number_2 if Maths_operation == '+' else (number_1 - number_2 if Maths_operation == '-' else (number_1 * number_2 if Maths_operation == '*' else number_1 // number_2)) # Correct answer both numbers added,subtracted,multiplied or divided.
            
            answers = [answer, answer + random.randint(1, 10), answer - random.randint(1, 10), answer + random.randint(11, 20)] # 1 answer in one of the boxes.
            random.shuffle(answers) # Puts random answers onto the 4 boxes.

            question_label.config(text=f'What is {number_1} {Maths_operation} {number_2}?') # Generates the question.

            for i, btn in enumerate(buttons):
                btn.config(text=f'{answers[i]}', command=lambda ans=answers[i]: check_answer(ans, answer)) # makes sure the answer selected is the correct answer.

        def check_answer(selected_answer, answer):
            ''' checks the answer the user has selected '''
            if selected_answer == answer: # if user has selected the correct answer.
                feedback_label.config(text="Correct!", fg="#00FF00") # User gets it correct.
                feedback_label.place(relx=0.57, rely=0.75, anchor='nw') # Position of correct text.
                self.handle_gif()
                self.score += 10  # Increase score for correct answer
            else:
                feedback_label.config(text="Incorrect. Try again!", fg="#FF0000") # User gets it incorrect.
                feedback_label.place(relx=0.57, rely=0.75, anchor='nw') # Position of incorrect text.
                self.score -= 5  # Decrease score for incorrect answer
            generate_question()

        def countdown():
            ''' Creates a 30 second timer.'''
            if self.time_left > 0: # user keeps answering questions above 0 seconds.
                self.time_left -= 1 
                self.timer_label.config(text=f"Time Left: {self.time_left}") # Timer label.
                self.after(1000, countdown) 
            else:
                game_window.destroy() # Destroy window once time is up
                self.end_game() # Ends the game once time is up

        countdown()
        generate_question()

    def handle_gif(self):
        ''' handling the animation of gif.'''
        if self.current_frame > GIF_END_FRAME: 
            self.current_frame = 0
            return
        
        self.frame_image = tk.PhotoImage(file="bench.gif", format=f"gif -index {self.current_frame}") # Cretaes my gif in my program.
        self.main_canvas.create_image(10,10, anchor="nw", image=self.frame_image) # Position of gif.
        self.current_frame += 1 # animation every frame.
        self.after(10, self.handle_gif) 

    def end_game(self):
        ''' shows my leaderboard system.'''
        username = self.username_entry.get() # Username shows on the leaderboard.
        self.scores.append((username, self.score))# Username and score is shown on leaderbord
        self.scores.sort(key=lambda x: x[1], reverse=True)
        self.save_scores()  # Save the scores to file
        self.open_leaderboard()

    def open_leaderboard(self):
        ''' creates a window for leaderboard'''
        leaderboard_window = tk.Toplevel() 
        leaderboard_window.config(bg="#333333") # Background of leaderboard
        leaderboard_window.title('Leaderboard') # Window title
        leaderboard_window.geometry('400x300')  # Size of window.
        leaderboard_window.resizable(0, 0) # Makes sure the window is in a fixed position.

        leaderboard_label = tk.Label(leaderboard_window, text="Leaderboard", font=("Arial", 20), bg='#333333', fg='#FFFFFF') # Leaderboard label.
        leaderboard_label.pack(pady=10) # Position of leaderboard text.

        for i, (user, score) in enumerate(self.scores): 
            score_label = tk.Label(leaderboard_window, text=f"{i+1}. {user} - {score}", font=("Arial", 14), bg='#333333', fg='#FFFFFF') # Creates score label
            score_label.pack()

    def validate_login(self):
        ''' Validates my login '''
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username.isalpha(): # makes sure username is only chracters.
            messagebox.showwarning("Error", "Please enter a valid username (alphabetic characters only).") # Error message informing user.
        elif len(password) < 7: # makes sure password is more than 7 characters.
            messagebox.showwarning("Error", "Password must be at least 7 characters long.") # Error message informing user.
        else:
            self.open_start_window() # all is correct starts the next window.
            self.withdraw()

if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
