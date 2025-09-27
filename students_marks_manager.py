# -------------------------------
# Day 4 Project: Student Marks Manager
# -------------------------------

# ......In this project I will make a Student Marks Manager
# ......It will store student marks, print each student's average marks,
# ......and allow adding a new student.

# ......First make a dictionary.......

Students = {
    "Itizaz": [93, 93, 89, 91, 95, 90],
    "Ahmad": [93, 95, 87, 90, 89, 86],
    "Qasim": [92, 84, 93, 91, 79, 92]
}

# ......Function to calculate average marks......


def calculate_average(marks):
    return sum(marks) / len(marks)


# ......Function to display all students and their averages......

def display_averages():
    print("\n--- Student Averages ---")
    for name, marks in Students.items():
        average = calculate_average(marks)
        print(f"{name} average marks are: {average:.2f}")


# ......Function to add a new student......

def add_student(name, marks):
    Students[name] = marks
    print(f"\nStudent '{name}' has been added successfully!")


#                 ------ Main Program ------


# Display existing averages

display_averages()


# Example of adding a new student

new_name = input("\nEnter new student's name: ")
new_marks = input(f"Enter marks of {new_name} separated by spaces: ")


# Convert marks string into a list of integers

marks_list = [int(m) for m in new_marks.split()]  
add_student(new_name, marks_list)


# Display averages again after adding new student

display_averages()
