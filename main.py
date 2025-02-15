grades = {}

def add_grade(subject, grade):
    if subject in grades:
        grades[subject].append(grade)
    else:
        grades[subject] = [grade]
    print(f"Added grade {grade} for subject '{subject}'.")

def calculate_average(subject):
    if subject in grades:
        total = sum(grades[subject])
        count = len(grades[subject])
        average = total / count
        return average
    else:
        print(f"No grades found for subject '{subject}'.")
        return None

def display_grades():
    if not grades:
        print("No grades recorded.")
        return
    for subject, grade_list in grades.items():
        avg = calculate_average(subject)
        print(f"{subject}: {grade_list} | Average: {avg:.2f}")

while True:
    print("\nGrade Tracker Menu:")
    print("1. Add Grade")
    print("2. Calculate Average")
    print("3. Display Grades")
    print("4. Exit")

    choice = input("Choose an option (1-4): ")

    if choice == '1':
        subject = input("Enter the subject: ")
        grade = float(input("Enter the grade: "))
        add_grade(subject, grade)

    elif choice == '2':
        subject = input("Enter the subject to calculate average: ")
        average = calculate_average(subject)
        if average is not None:
            print(f"The average grade for '{subject}' is: {average:.2f}")

    elif choice == '3':
        display_grades()

    elif choice == '4':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please try again.")
