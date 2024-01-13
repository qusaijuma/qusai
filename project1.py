import tkinter
import tkinter as tk
from tkinter import ttk, messagebox


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))


def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    myfile = open("users.txt", "r")
    alldata = myfile.readlines()

    for x in alldata:
        linedata = x.split(",")
        if username == linedata[1] and password == linedata[2]:
            open_goal_window()
            break
        else:
            messagebox.showinfo("Login Failed", "Invalid username or password")
            break


def signup_complete(email_entry, username_entry, password_entry, phone_entry):
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    phone = phone_entry.get()

    myfile = open("users.txt", "r")
    alldata = myfile.readlines()

    if email == "" or username == "" or password == "" or phone == "":
        messagebox.showinfo("Sign Up Failed", "Please fill in all required fields.")
        open_signup_window()
    elif len(phone) != 10:
        messagebox.showinfo("Sign Up Failed", "Please enter a 10-digit phone number.")
        open_signup_window()
    elif not phone.isdigit():
        messagebox.showinfo("Sign Up Failed", "Please enter a valid phone number.")
        open_signup_window()
    else:
        for x in alldata:
            linedata = x.split(",")
            if linedata[0] == email:
                messagebox.showinfo("Sign Up Failed", "Please use another email.")
                open_signup_window()
            elif linedata[1] == username:
                messagebox.showinfo("Sign Up Failed", "Please use another username.")
                open_signup_window()
            elif linedata[3] == phone:
                messagebox.showinfo("Sign Up Failed", "Please use another phone number.")
                open_signup_window()
            else:
                myfile = open("users.txt", "a")
                str1 = "\n" + email + "," + username + "," + password + "," + phone + ",end"
                myfile.write(str1)
                messagebox.showinfo("Sign Up Complete", "Sign Up Successful!")
                open_additional_info_window()
            break


def open_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")
    fram2 = tkinter.Frame(signup_window, bg="#333333")

    signup_window.geometry("340x440")
    signup_window.configure(bg="#333333")
    center_window(signup_window)

    signup_label = tk.Label(fram2, text="Sign Up", bg="#333333", fg="#3BEDDF", font=("Arial", 30))
    signup_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=30)

    email_label = tk.Label(fram2, text="Email:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    email_label.grid(row=1, column=0, pady=18)

    email_entry = tk.Entry(fram2)
    email_entry.grid(row=1, column=1)

    username_label2 = tk.Label(fram2, text="Username:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    username_label2.grid(row=2, column=0, pady=18)

    username_entry = tk.Entry(fram2)
    username_entry.grid(row=2, column=1)

    password_label = tk.Label(fram2, text="Password:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    password_label.grid(row=3, column=0, pady=18)

    password_entry = tk.Entry(fram2, show="*")
    password_entry.grid(row=3, column=1)

    phone_label = tk.Label(fram2, text="Phone Number:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    phone_label.grid(row=4, column=0, pady=18)

    phone_entry = tk.Entry(fram2)
    phone_entry.grid(row=4, column=1)

    signup_button2 = tk.Button(fram2, text="       Sign Up       ", command=lambda: signup_complete(email_entry, username_entry, password_entry, phone_entry), bg="#3BEDDF", fg="black", font=("Arial", 12))
    signup_button2.grid(row=5, column=0, columnspan=2, pady=30)

    fram2.pack()


def additional_info_complete(gender_var, weight_entry, height_entry, age_entry, goal_var):
    gender = gender_var.get()
    weight = weight_entry.get()
    height = height_entry.get()
    age = age_entry.get()
    goal = goal_var.get()

    myfile = open("usersInfo.txt", "a")
    str1 = "\n" + gender + "," + weight + "," + height + "," + age + "," + goal + ",end"
    myfile.write(str1)

    messagebox.showinfo("Information Submitted", "Additional Information Submitted Successfully!")
    open_goal_window()


def open_additional_info_window():
    additional_info_window = tk.Toplevel(root)
    additional_info_window.title("Additional Information")
    additional_info_window.geometry("350x500")
    fram3 = tkinter.Frame(additional_info_window, bg="#333333")

    additional_info_window.configure(bg="#333333")
    center_window(additional_info_window)

    info_label = tk.Label(fram3, text="Data entry", bg="#333333", fg="#3BEDDF", font=("Arial", 30))
    info_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

    gender_label = tk.Label(fram3, text="Select Gender:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    gender_label.grid(row=1, column=0, pady=20)

    gender_var = tk.StringVar()
    gender_var.set("                           ")  # Default value
    gender_options = ["         Male         ", "       Female       "]
    gender_menu = tk.OptionMenu(fram3, gender_var, *gender_options)
    gender_menu.grid(row=1, column=1, pady=20)

    weight_label = tk.Label(fram3, text="Weight (kg):", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    weight_label.grid(row=2, column=0, pady=20)

    weight_entry = tk.Entry(fram3)
    weight_entry.grid(row=2, column=1, pady=20)

    height_label = tk.Label(fram3, text="Height (cm):", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    height_label.grid(row=3, column=0, pady=20)

    height_entry = tk.Entry(fram3)
    height_entry.grid(row=3, column=1, pady=20)

    age_label = tk.Label(fram3, text="Age:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    age_label.grid(row=4, column=0, pady=20)

    age_entry = tk.Entry(fram3)
    age_entry.grid(row=4, column=1, pady=20)

    goal_label = tk.Label(fram3, text="Select Goal:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
    goal_label.grid(row=5, column=0, pady=20)

    goal_var = tk.StringVar()
    goal_var.set("                          ")  # Default value
    goal_options = ["  Lose Weight  ", "Maintain Weight", " Build Muscle "]
    goal_menu = tk.OptionMenu(fram3, goal_var, *goal_options)
    goal_menu.grid(row=5, column=1, pady=20)

    submit_button = tk.Button(fram3, text="        Submit      ", command=lambda: additional_info_complete(gender_var, weight_entry, height_entry, age_entry, goal_var), bg="#3BEDDF", fg="black", font=("Arial", 12))
    submit_button.grid(row=6, column=1, columnspan=2, pady=20)

    fram3.pack()


def open_goal_window():
    goal_window = tk.Toplevel(root)
    goal_window.title("Goal Options")
    fram3 = tk.Frame(goal_window, bg="#333333")

    goal_window.geometry("350x500")
    goal_window.configure(bg="#333333")
    center_window(goal_window)

    goal_label = tk.Label(fram3, text="Goal Options", bg="#333333", fg="#3BEDDF", font=("Arial", 35))
    goal_label.grid(row=0, column=0, columnspan=3, sticky="news", pady=40)

    lose_weight_button = tk.Button(fram3, text="     Lose Weight      ", command=open_lose_weight_window, bg="#3BEDDF", fg="black", font=("Arial", 20))
    lose_weight_button.grid(row=1, column=1, pady=25)

    build_muscle_button = tk.Button(fram3, text="     Build Muscle      ", command=open_build_muscle_window, bg="#3BEDDF", fg="black", font=("Arial", 20))
    build_muscle_button.grid(row=2, column=1, pady=25)

    maintain_weight_button = tk.Button(fram3, text="   Maintain Weight   ", command=open_maintain_weight_window, bg="#3BEDDF", fg="black", font=("Arial", 20))
    maintain_weight_button.grid(row=3, column=1, pady=25)

    fram3.pack()


def open_lose_weight_window():
    lose_weight_window = tk.Toplevel(root)
    lose_weight_window.title("Lose weight workouts Schedule")

    fram5 = tk.Frame(lose_weight_window, bg="#333333")

    lose_weight_window.configure(bg="#333333")
    lose_weight_window.geometry("450x350")
    center_window(lose_weight_window)

    schedule_label = tk.Label(fram5, text="Training workouts Schedule", bg="#333333", fg="#3BEDDF", font=("Arial", 20))
    schedule_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    workout_plan = [
        "Power walking for 45 minutes",
        "Strength training for upper body",
        "Yoga for 45 minutes",
        "Strength training for lower body",
        "Power walking for 45 minutes",
        "Rest day",
        "Jogging for 30 minutes"
    ]

    tree = ttk.Treeview(fram5, columns=("Day", "Workout Plan"), show="headings", height=7)
    tree.heading("Day", text="Day")
    tree.heading("Workout Plan", text="Workout Plan")

    for day, plan in zip(days, workout_plan):
        tree.insert("", "end", values=(day, plan))

    tree.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    food_button = tk.Button(fram5, text="                     Press here for Food Schedule                       ", command=lambda: open_food_schedule1_window(), bg="#3BEDDF", fg="black", font=("Arial", 12))
    food_button.grid(row=2, column=0, columnspan=2, pady=10)

    fram5.pack()


def open_food_schedule1_window():
    food_schedule1_window = tk.Toplevel(root)
    food_schedule1_window.title("Food Schedule")

    fram6 = tk.Frame(food_schedule1_window, bg="#333333")

    food_schedule1_window.configure(bg="#333333")
    food_schedule1_window.geometry("1350x350")
    center_window(food_schedule1_window)

    schedule_label = tk.Label(fram6, text="Food Schedule for losing weight", bg="#333333", fg="#3BEDDF", font=("Arial", 20))
    schedule_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    breakfast = [
        "Oatmeal with blueberries, milk, and seeds",
        "Scrambled eggs with spinach and tomato",
        "Mashed avocado and a fried egg on a slice of rye toast",
        "Smoothie made with protein powder, berries, and oat milk",
        "Buckwheat pancakes with raspberries and Greek yogurt",
        "Breakfast muffin with eggs and vegetables",
        "Cheat Day"
    ]
    lunch = [
        "Grilled chicken salad with balsamic vinaigrette",
        "Tuna salad with lettuce, cucumber, and tomato",
        "Broccoli quinoa and toasted almonds",
        "Chicken salad with lettuce and corn",
        "Vegetable soup with two oatcakes",
        "Minted pea and feta omelet",
        "Cheat Day"
    ]
    dinner = [
        "Grilled salmon with roasted vegetables",
        "Bean chili with cauliflower rice",
        "Chicken stir fry and soba noodles",
        "Roasted Mediterranean vegetables, puy lentils, and tahini dressing",
        "Fish tacos with slaw",
        "Baked sweet potato, chicken breast, greens",
        "Cheat Day"
    ]
    snacks = [
        "Apple slices with peanut butter",
        "Tangerine and cashew nuts",
        "Blueberries and coconut yogurt",
        "Whole grain rice cake with nut butter",
        "Carrot sticks and hummus",
        "Apple slices with peanut butter",
        "Cheat Day"
    ]

    tree = ttk.Treeview(fram6, columns=("Day", "Breakfast", "Lunch", "Dinner", "Snacks"), show="headings", height=7)
    tree.heading("Day", text="Day")
    tree.heading("Breakfast", text="Breakfast")
    tree.heading("Lunch", text="Lunch")
    tree.heading("Dinner", text="Dinner")
    tree.heading("Snacks", text="Snacks")

    tree.column("Day", width=80, stretch=False)
    tree.column("Breakfast", width=340, stretch=True)
    tree.column("Lunch", width=270, stretch=True)
    tree.column("Dinner", width=360, stretch=True)
    tree.column("Snacks", width=220, stretch=True)

    for day, Breakfast, Lunch, Dinner, Snacks in zip(days, breakfast, lunch, dinner, snacks):
        tree.insert("", "end", values=(day, Breakfast, Lunch, Dinner, Snacks))

    tree.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
    fram6.pack()


def open_build_muscle_window():
    build_muscle_window = tk.Toplevel(root)
    build_muscle_window.title("Building muscle workouts Schedule")

    fram7 = tk.Frame(build_muscle_window, bg="#333333")

    build_muscle_window.configure(bg="#333333")
    build_muscle_window.geometry("450x350")
    center_window(build_muscle_window)

    schedule_label = tk.Label(fram7, text="Training workouts Schedule", bg="#333333", fg="#3BEDDF", font=("Arial", 20))
    schedule_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    workout_plan = [
        "Chest day  4x12",
        "Back day  2xfailure",
        "Shoulders day low weights high reps",
        "Leg day high reps rir",
        "Arm day go for failure",
        "Rest day",
        "Rest day"
    ]

    tree = ttk.Treeview(fram7, columns=("Day", "Workout Plan"), show="headings", height=7)
    tree.heading("Day", text="Day")
    tree.heading("Workout Plan", text="Workout Plan")

    for day, plan in zip(days, workout_plan):
        tree.insert("", "end", values=(day, plan))

    tree.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    food_button = tk.Button(fram7, text="                      Press here for Food Schedule                       ", command=lambda: open_food_schedule2_window(), bg="#3BEDDF", fg="black", font=("Arial", 12))
    food_button.grid(row=2, column=0, columnspan=2, pady=10)

    fram7.pack()


def open_food_schedule2_window():
    food_schedule2_window = tk.Toplevel(root)
    food_schedule2_window.title("Food Schedule")

    fram8 = tk.Frame(food_schedule2_window, bg="#333333")

    food_schedule2_window.configure(bg="#333333")
    food_schedule2_window.geometry("1350x350")
    center_window(food_schedule2_window)

    schedule_label = tk.Label(fram8, text="Food Schedule for building muscles", bg="#333333", fg="#3BEDDF", font=("Arial", 20))
    schedule_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    breakfast = [
        "Breakfast muffin with eggs and vegetables",
        "Oatmeal with milk, banana, and almonds",
        "Scrambled eggs with spinach and tomato",
        "Mashed avocado and a fried egg on a slice of rye toast",
        "Smoothie made with protein powder, berries, and oat milk",
        "Buckwheat pancakes with raspberries and Greek yogurt",
        "Cheat Day"
    ]
    lunch = [
        "Minted pea and feta omelet",
        "Chicken breast, brown rice, and broccoli",
        "Tuna salad with lettuce, cucumber, and tomato",
        "Broccoli quinoa and toasted almonds",
        "Chicken salad with lettuce and corn",
        "Vegetable soup with two oatcakes",
        "Cheat Day"
    ]
    dinner = [
        "Fish tacos with slaw",
        "Salmon, sweet potato, and salad",
        "Turkey burger, whole wheat bun, and coleslaw",
        "Steak, baked potato, and asparagus",
        "Shrimp, pasta, and broccoli",
        "Chicken stir fry and soba noodles",
        "Cheat Day"
    ]
    snacks = [
        "Protein shake and kiwi",
        "Protein shake and apple",
        "Protein bar and orange",
        "Protein shake and pear",
        "Protein muffin and grapes",
        "Protein shake and banana",
        "Cheat Day"
    ]

    tree = ttk.Treeview(fram8, columns=("Day", "Breakfast", "Lunch", "Dinner", "Snacks"), show="headings", height=7)
    tree.heading("Day", text="Day")
    tree.heading("Breakfast", text="Breakfast")
    tree.heading("Lunch", text="Lunch")
    tree.heading("Dinner", text="Dinner")
    tree.heading("Snacks", text="Snacks")

    tree.column("Day", width=80, stretch=False)
    tree.column("Breakfast", width=340, stretch=True)
    tree.column("Lunch", width=270, stretch=True)
    tree.column("Dinner", width=360, stretch=True)
    tree.column("Snacks", width=220, stretch=True)

    for day, Breakfast, Lunch, Dinner, Snacks in zip(days, breakfast, lunch, dinner, snacks):
        tree.insert("", "end", values=(day, Breakfast, Lunch, Dinner, Snacks))

    tree.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
    fram8.pack()


def open_maintain_weight_window():
    maintain_weight_window = tk.Toplevel(root)
    maintain_weight_window.title("Maintain weight workouts Schedule")

    fram9 = tk.Frame(maintain_weight_window, bg="#333333")

    maintain_weight_window.configure(bg="#333333")
    maintain_weight_window.geometry("550x350")
    center_window(maintain_weight_window)

    schedule_label = tk.Label(fram9, text="         Training workouts Schedule          ", bg="#333333", fg="#3BEDDF", font=("Arial", 20))
    schedule_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    workout_plan = [
        "Bodyweight workouts",
        "Three sets of 10 reps opt for compound movements",
        "Get proper sleep is crucial for muscle recovery",
        "Resistance workouts",
        "20 minutes of strength training two to three time a week",
        "Rest day",
        "Rest day"
    ]

    tree = ttk.Treeview(fram9, columns=("Day", "Workout Plan"), show="headings", height=7)
    tree.heading("Day", text="Day")
    tree.heading("Workout Plan", text="Workout Plan")

    tree.column("Workout Plan", width=310, stretch=True)


    for day, plan in zip(days, workout_plan):
        tree.insert("", "end", values=(day, plan))

    tree.grid(row=1, column=0, columnspan=2, pady=10, padx=10)

    food_button = tk.Button(fram9, text="\t\t Press here for Food Schedule \t\t", command=lambda: open_food_schedule3_window(), bg="#3BEDDF", fg="black", font=("Arial", 12))
    food_button.grid(row=2, column=0, columnspan=2, pady=10)

    fram9.pack()


def open_food_schedule3_window():
    food_schedule2_window = tk.Toplevel(root)
    food_schedule2_window.title("Food Schedule")

    fram10 = tk.Frame(food_schedule2_window, bg="#333333")

    food_schedule2_window.configure(bg="#333333")
    food_schedule2_window.geometry("1350x350")
    center_window(food_schedule2_window)

    schedule_label = tk.Label(fram10, text="Food Schedule for building muscles", bg="#333333", fg="#3BEDDF", font=("Arial", 20))
    schedule_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=20)

    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    breakfast = [
        "French toast with honey and raspberries",
        "Whole wheat toast with peanut butter and banana",
        "Oatmeal with milk, nuts, and dried fruits",
        "Scrambled eggs with spinach and whole wheat toast",
        "Greek yogurt with granola and blueberries",
        "Whole wheat pancakes with maple syrup and strawberries",
        "Cheat Day"
    ]
    lunch = [
        "Vegetable and noodle stir-fry with tofu",
        "Turkey sandwich with lettuce, tomato, and cheese",
        "Vegetable and bean soup with whole wheat pita bread",
        "Chicken salad with lettuce, cucumber, and avocado",
        "Tuna salad with whole wheat crackers and cherry tomatoes",
        "Vegetable and cheese quesadilla with salsa",
        "Cheat Day"
    ]
    dinner = [
        "Roasted turkey with roasted vegetables and quinoa",
        "Salmon with roasted vegetables and brown rice",
        "Chicken and vegetable stir-fry with noodles",
        "Spaghetti with tomato sauce and meatballs",
        "Beef and vegetable stew with mashed potatoes",
        "Roasted chicken with roasted potatoes and green beans",
        "Cheat Day"
    ]
    snacks = [
        "Carrot cake and milk",
        "Carrot sticks and hummus",
        "Low-fat yogurt with berries",
        "Orange and granola bar",
        "Popcorn and dried cranberries",
        "Banana and chocolate milk",
        "Cheat Day"
    ]

    tree = ttk.Treeview(fram10, columns=("Day", "Breakfast", "Lunch", "Dinner", "Snacks"), show="headings", height=7)
    tree.heading("Day", text="Day")
    tree.heading("Breakfast", text="Breakfast")
    tree.heading("Lunch", text="Lunch")
    tree.heading("Dinner", text="Dinner")
    tree.heading("Snacks", text="Snacks")

    tree.column("Day", width=80, stretch=False)
    tree.column("Breakfast", width=340, stretch=True)
    tree.column("Lunch", width=270, stretch=True)
    tree.column("Dinner", width=360, stretch=True)
    tree.column("Snacks", width=220, stretch=True)

    for day, Breakfast, Lunch, Dinner, Snacks in zip(days, breakfast, lunch, dinner, snacks):
        tree.insert("", "end", values=(day, Breakfast, Lunch, Dinner, Snacks))

    tree.grid(row=1, column=0, columnspan=2, pady=20, padx=20)
    fram10.pack()


# login window
root = tk.Tk()
root.title("Login")
Frame = tkinter.Frame(bg="#333333")

root.geometry("340x440")
root.configure(bg="#333333")
center_window(root)

login_label = tk.Label(Frame, text="Login", bg="#333333", fg="#3BEDDF", font=("Arial", 30))
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
# Create and place widgets
username_label = tk.Label(Frame, text="Username:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
username_label.grid(row=1, column=0, pady=20)

username_entry = tk.Entry(Frame)
username_entry.grid(row=1, column=1)

password_label = tk.Label(Frame, text="Password:", bg="#333333", fg="#FFFFFF", font=("Arial", 12))
password_label.grid(row=2, column=0, pady=20)

password_entry = tk.Entry(Frame, show="*")
password_entry.grid(row=2, column=1)

login_button = tk.Button(Frame, text="         Login         ", command=validate_login, bg="#3BEDDF", fg="black", font=("Arial", 12))
login_button.grid(row=3, column=0, columnspan=2, pady=20)

signup_button = tk.Button(Frame, text="       Sign Up       ", command=open_signup_window, bg="#3BEDDF", fg="black", font=("Arial", 12))
signup_button.grid(row=4, column=0, columnspan=2, pady=10)

Frame.pack()
root.mainloop()



