🎓 Student Marks Manager (Day 4 Project)<br><br>
📌 Overview
<br><br>
     This is my Day 4 Python Project: a simple Student Marks Manager.<br><br>
The program stores students’ marks in a dictionary, calculates their average marks, and allows adding new students dynamically.<br>

It’s a beginner-friendly project that demonstrates:<br>

Dictionaries (for storing data)<br>

Functions (for modular code)<br>

Loops (for iterating over student data)<br>

User Input (for adding new students)<br><br>

🛠️ Features
<br><br>
✅ Store marks of multiple students<br>
✅ Calculate each student’s average marks<br>
✅ Add a new student with their marks<br>
✅ Display updated results<br>

📂 Project Structure<br><br>

Student-Marks-Manager/
│
├── student_manager.py   # Main Python code
├── README.md            # Project Documentation<br>

🚀 How It Works<br>

1. The program starts with a dictionary of students and their marks:<br>
Students = {
    "Itizaz": [93, 93, 89, 91, 95, 90],
    "Ahmad": [93, 95, 87, 90, 89, 86],
    "Qasim": [92, 84, 93, 91, 79, 92]
}
<br>
2. It calculates the average marks of each student using a function:<br>
def calculate_average(marks):
    return sum(marks) / len(marks)<br>
3. It prints all student averages.<br>

4. The user can add a new student and their marks.<br>

5. The program then displays the updated list with averages.<br><br>

▶️ Example Output
<br><br>
--- Student Averages ---
Itizaz average marks are:  91.83
Ahmad average marks are:  90.00
Qasim average marks are:  88.50
<br>
Enter new student's name: Ali<br>
Enter marks of Ali separated by spaces: 95 90 92 88 91<br>

Student 'Ali' has been added successfully!<br>

--- Student Averages ---
Itizaz average marks are:  91.83
Ahmad average marks are:  90.00
Qasim average marks are:  88.50
Ali average marks are:  91.20
<br>
📖 What I Learned<br><br>

How to use dictionaries for storing structured data<br>

Writing functions for reusability<br>

Iterating with for loops<br>

Taking and processing user input<br>

This project improved my problem-solving and code organization skills in Python.<br>
<br><br>
🔮 Future Improvements
<br><br>
Here are some ideas to make the project more advanced in the future:
<br>
📊 Store data in CSV or JSON files so that student records persist even after the program closes.<br>

📝 Add student editing and deletion options (not just adding new ones).<br>

📈 Show highest, lowest, and overall class average for better insights.<br>

💻 Add a simple GUI (Graphical User Interface) using Tkinter or PyQt.<br>

🌐 Convert it into a web app using Flask/Django for online student management.<br>

🔐 Add authentication so only teachers/admins can modify student data.<br>

✨ Day 4 complete! Onwards to Day 5 🚀
