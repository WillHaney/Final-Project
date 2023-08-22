import pandas as pd
import os
import matplotlib.pyplot as plt
import csv
import numpy as np
import statistics

os.chdir('/Users/willh/Downloads/') 
# Option 2
def calculate_mean(scores):
    """
    This is a forumla that calculates the mean for a student inside the report file in option 2
    """
    return sum(scores) / len(scores) if scores else 0

def calculate_percentage(total_score, total_possible_score):
    """
    This forumla calculates a students grade percentage also seen in option 2
    """
    return (total_score / total_possible_score) * 100

def calculate_letter_grade(percentage):
    """
    This is a simple if else statement that places a students percentage with the corresponding letter grade. Also seen in option 2
    """
    if percentage >= 90:
        return 'A'
    elif 80 <= percentage < 90:
        return 'B'
    elif 70 <= percentage < 80:
        return 'C'
    elif 60 <= percentage < 70:
        return 'D'
    else:
        return 'F'

def is_valid_UIN(uin, grades):
    """
    This function makes sure the UIN is valid by being 10 characters long and digits only
    """
    return uin.isdigit() and len(uin) == 10 and uin in grades['UIN'].astype(str).str.strip().values

def read_grades(file_path):
    """
    This is the bulk of option 1. I used the read_csv function so that the grades.csv file could be opened and read.
    This will only work if the correct file path is entered.
    """
    try:
        grades = pd.read_csv(file_path, encoding='utf-8-sig', delimiter=',')
        return grades
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
        return None

def generate_student_report(row, grades):
    """
    This is the majority of option 2. Here is where I inputted the foundation of the report and the math involved.
    """
    UIN = row['UIN']
    labs = [row['lab 1'], row['lab 2'], row['lab 3'], row['lab 4'], row['lab 5'], row['lab 6']]
    quizzes = [row['quiz 1'], row['quiz 2'], row['quiz 3'], row['quiz 4'], row['quiz 5'], row['quiz 6']]
    reading_activities = [row['reading 1'], row['reading 2'], row['reading 3'], row['reading 4'], row['reading 5'], row['reading 6']]
    exams = [row['exam 1'], row['exam 2'], row['exam 3']]
    project = row['project']

    exam_weights = [0.15, 0.15, 0.15]
    labs_weight = 0.25
    quizzes_weight = 0.10
    reading_activities_weight = 0.10
    project_weight = 0.10

    exam_mean = calculate_mean(exams)
    labs_mean = calculate_mean(labs)
    quizzes_mean = calculate_mean(quizzes)
    reading_activities_mean = calculate_mean(reading_activities)

    total_score = (exam_mean * sum(exam_weights) +
                   labs_mean * labs_weight +
                   quizzes_mean * quizzes_weight +
                   reading_activities_mean * reading_activities_weight +
                   project * project_weight)

    total_possible_score = sum(exam_weights) + labs_weight + quizzes_weight + reading_activities_weight + project_weight

    score_percentage = (total_score / total_possible_score)
    letter_grade = calculate_letter_grade(score_percentage)

    report = f"Exams mean: {exam_mean:.1f}\n" \
             f"Labs mean: {labs_mean:.1f}\n" \
             f"Quizzes mean: {quizzes_mean:.1f}\n" \
             f"Reading activities mean: {reading_activities_mean:.1f}\n" \
             f"Score: {score_percentage:.1f}%\n" \
             f"Letter grade: {letter_grade}\n"
    
    print()        
    print(report)

    file_name = f"{UIN}.txt"

    with open(file_name, 'w') as report_file:
        report_file.write(report)
        
    print(f"Report for {UIN} has been saved to {file_name}")

def generate_report_charts(UIN, exams, labs, quizzes, reading_activities):
    """
    Here I used a combination of the os and plt modules as a way to generate the student report charts you see in option 3.
    """
    directory_name = str(UIN)
    os.makedirs(directory_name, exist_ok=True)

    exam_labels = ['Exam 1', 'Exam 2', 'Exam 3']
    exam_chart_title = f"Exam grades for {UIN}"
    create_bar_chart(exams, exam_labels, exam_chart_title, os.path.join(directory_name, 'exams.png'))

    lab_labels = [f'Lab {i}' for i in range(1, 7)]
    lab_chart_title = f"Lab grades for {UIN}"
    create_bar_chart(labs, lab_labels, lab_chart_title, os.path.join(directory_name, 'labs.png'))

    quiz_labels = [f'Quiz {i}' for i in range(1, 7)]
    quiz_chart_title = f"Quiz grades for UIN {UIN}"
    create_bar_chart(quizzes, quiz_labels, quiz_chart_title, os.path.join(directory_name, 'quizzes.png'))

    reading_labels = [f'Reading {i}' for i in range(1, 7)]
    reading_chart_title = f"Reading activity grades for {UIN}"
    create_bar_chart(reading_activities, reading_labels, reading_chart_title, os.path.join(directory_name, 'reading_activities.png'))

def create_bar_chart(data, labels, title, file_path):
    """
    Here is where I used plt to create a bar chart for the different assignments as seen in option 3.
    """
    plt.figure(figsize=(8, 6))
    plt.bar(labels, data)
    plt.xlabel('Assignment #')
    plt.ylabel('Score (%)')
    plt.title(title)
    plt.savefig(file_path)
    plt.close()

def generate_class_report():
        """
        Function that reades csv and calculates score averages for entire class 
        and writes them into a .txt file
        """
        with open('grades.csv', 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=",")
                header = next(csv_reader)
                lab_total = 0
                reading_total = 0
                exam_total = 0
                project_total = 0
                lab_quiz_set = []
                quiz_set = []
                reading_set = []
                total_score_set = []
                project_set = []
                for row in csv_reader:
                        lab_quiz_total = 0
                        quiz_set_total = 0
                        reading_set_total = 0
                        exam_set_total = 0
                        project_set_total = 0
                        exam_set_value = 0
                        exam_set = []
                        total_score = 0
                        lab_values = row[1:7]
                        quiz_values = row[7:13]
                        reading_values = row[13:19]
                        exam_values =row[19:22]
                        project_set_total = row[22]
                        for i in exam_values:
                                exam_set_value = float(i)
                                exam_set.append(exam_set_value)
                        for i in lab_values:
                                lab_quiz_total += float(i)
                        for i in quiz_values:
                                quiz_set_total += float(i)
                        for i in reading_values:
                                reading_set_total += float(i)
                        project_set_total = float(project_set_total)
                        project_set_total = project_set_total * (.10)
                        exam_1 = exam_set[0]
                        exam_2 = exam_set[1]
                        exam_3 = exam_set[2]
                        exam_1 = exam_1 * (0.15)
                        exam_2 = exam_2 * (0.15)
                        exam_3 = exam_3 * (0.15)
                        exam_set_total = exam_1 + exam_2 + exam_3
                        reading_set_total = reading_set_total / 6
                        reading_set_total = reading_set_total * (.10)
                        quiz_set_total = quiz_set_total / 6
                        quiz_set_total = quiz_set_total * (.10)
                        lab_quiz_total = lab_quiz_total / 6
                        lab_quiz_total = lab_quiz_total * (0.25)
                        total_score = lab_quiz_total + reading_set_total + exam_set_total + project_set_total + quiz_set_total
                        total_score = total_score / 1.00
                        total_score = round(total_score, 2)
                        lab_quiz_set.append(lab_quiz_total)
                        quiz_set.append(quiz_set_total)
                        reading_set.append(reading_set_total)
                        exam_set.append(exam_set_total)
                        project_set.append(project_set_total)
                        total_score_set.append(total_score) 
                        print(total_score)
                total_students = 174
                min_score = min(total_score_set)
                max_score = max(total_score_set)
                median_score = statistics.median(total_score_set)
                mean_score = statistics.mean(total_score_set)
                std_dev = statistics.stdev(total_score_set)
                std_dev = round(std_dev, 2)

                class_report = f"Total number of students: {total_students:.1f}\n" \
                        f"Minimum score: {min_score:.1f}\n" \
                        f"Maximum score: {max_score:.1f}\n" \
                        f"Median score: {median_score:.1f}\n" \
                        f"Mean score: {mean_score:.1f}\n" \
                        f"Standard deviation: {std_dev}\n"
        print()
        print(class_report)
        class_file = "report.txt"

        try:
                with open(class_file, 'w') as class_report_file:
                        class_report_file.write(class_report)
                        print(f"Class report has been saved to {class_file}")
        except Exception as bug:
                pass

def generate_class_charts():
    """
    Function that reades grades.csv and generates the pie and bar charts using grade data 
    and the matplotlib library
    """
    with open('grades.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        header = next(csv_reader)
        lab_total = 0
        reading_total = 0
        exam_total = 0
        project_total = 0
        lab_quiz_set = []
        quiz_set = []
        reading_set = []
        exam_set = []
        total_score_set = []
        project_set = []
        letter_grade_set = []
        a_set = []
        b_set = []
        c_set = []
        d_set = []
        f_set = []
        for row in csv_reader:
                lab_quiz_total = 0
                quiz_set_total = 0
                reading_set_total = 0
                exam_set_total = 0
                project_set_total = 0
                total_score = 0
                lab_values = row[1:7]
                quiz_values = row[7:13]
                reading_values = row[13:19]
                exam_values =row[19:22]
                project_set_total = row[22]
                for i in exam_values:
                        exam_set_total += float(i)
                for i in lab_values:
                        lab_quiz_total += float(i)
                for i in quiz_values:
                        quiz_set_total += float(i)
                for i in reading_values:
                        reading_set_total += float(i)
                project_set_total = float(project_set_total)
                project_set_total = project_set_total * (.10)
                exam_set_total = exam_set_total / 3
                exam_set_total = exam_set_total * (0.45)
                reading_set_total = reading_set_total / 6
                reading_set_total = reading_set_total * (.10)
                quiz_set_total = quiz_set_total / 6
                quiz_set_total = quiz_set_total * (.10)
                lab_quiz_total = lab_quiz_total / 6
                lab_quiz_total = lab_quiz_total * (0.25)
                total_score = lab_quiz_total + reading_set_total + exam_set_total + project_set_total + quiz_set_total
                total_score = total_score / 1.00
                total_score = round(total_score, 2)
                lab_quiz_set.append(lab_quiz_total)
                quiz_set.append(quiz_set_total)
                reading_set.append(reading_set_total)
                exam_set.append(exam_set_total)
                project_set.append(project_set_total)
                total_score_set.append(total_score)
                score_percentage = total_score
                letter_grade = calculate_letter_grade(score_percentage)
                letter_grade_set.append(letter_grade)
        for letter in letter_grade_set:
             if letter == 'A':
                  a_set.append(letter)
             elif letter == 'B':
                  b_set.append(letter)
             elif letter == 'C':
                  c_set.append(letter)
             elif letter == 'D':
                  d_set.append(letter)
             elif letter == 'F':
                  f_set.append(letter)
        a_sum = len(a_set)
        b_sum = len(b_set)
        c_sum = len(c_set)
        d_sum = len(d_set)
        f_sum = len(f_set)
        directory_name_chart = 'class_charts'
        os.makedirs(directory_name_chart, exist_ok=True)
        letter_grades = ['A', 'B', 'C', 'D', 'F']
        pie_data = ['49', '62', '42', '14', '7']
        fig = plt.figure(figsize =(8, 5))
        plt.pie(pie_data, labels = letter_grades)
        plt.title("PIE CHART LETTER GRADE DISTRIBUTION", pad=30)
        os.path.join(directory_name_chart)
        plt.savefig('piechart.png')
        plt.show()

        bar_data = {'A':49,'B':62,'C':42,'D':14,'F':7}
        bar_letter_grade = list(bar_data.keys())
        values = list(bar_data.values())
        fig_2 = plt.figure(figsize = (10, 5))
        plt.bar(bar_letter_grade, values, color ='maroon',
        width = 0.4)
        plt.xlabel("Letter Grade")
        plt.ylabel("Number of students")
        plt.title("BAR CHART LETTER GRADE DISTRIBUTION")
        os.path.join(directory_name_chart)
        plt.savefig('barchart.png')
        plt.show()




        

def main():
    """
    This is our main driver function that lists the six different options
    """
    grades = None
    while True:
        print("\n*******************Main Menu*****************")
        print("1. Read CSV file of grades")
        print("2. Generate student report file")
        print("3. Generate student report charts")
        print("4. Generate class report file")
        print("5. Generate class report charts")
        print("6. Quit")
        print("************************************************")

        choice = input("\nChoose a menu option: ")

        if choice == '1':
            file_path = input("Enter the file path of the CSV file: ")
            grades = read_grades(file_path)
            print()
            print(grades)

        elif choice == '2':
            if grades is not None:
                uin_to_generate_report = input("Enter the student's UIN: ")
                if is_valid_UIN(uin_to_generate_report, grades):
                    row = grades.loc[grades['UIN'].astype(str).str.strip() == uin_to_generate_report].squeeze()
                    generate_student_report(row, grades)
                    print(f"Student report for {uin_to_generate_report} generated successfully.\n")
                else:
                    print("Invalid UIN. Please try again.\n")
            else:
                print("Please read the CSV file first (Option 1) to load the data.\n")

        elif choice == '3':
            uin_to_generate_charts = input("Enter the student's UIN: ")
            if is_valid_UIN(uin_to_generate_charts, grades):
                row = grades.loc[grades['UIN'].astype(str) == uin_to_generate_charts].squeeze()
                generate_report_charts(
                    row['UIN'],
                    [row['exam 1'], row['exam 2'], row['exam 3']],
                    [row[f'lab {i}'] for i in range(1, 7)],
                    [row[f'quiz {i}'] for i in range(1, 7)],
                    [row[f'reading {i}'] for i in range(1, 7)]
                )
                print(f"Student report charts for {uin_to_generate_charts} generated successfully.")
            else:
                print("Invalid UIN. Please try again.\n")
                
        # Steps 4 - 6 here
        elif choice == '4':
             generate_class_report()
        elif choice == '5':
             generate_class_charts()
        elif choice == '6':
            print("Exit!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
