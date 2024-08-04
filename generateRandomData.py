import csv
import random


def calculate_weighted_average(
    totalAttendance, quizAverage, assignmentAverage, examAverage
):
    weight_exam = 0.70
    weight_attendance = 0.10
    weight_quiz = 0.10
    weight_assignment = 0.10

    weighted_average = (
        examAverage * weight_exam
        + totalAttendance * weight_attendance
        + quizAverage * weight_quiz
        + assignmentAverage * weight_assignment
    )

    return weighted_average


def assign_grade(totalAttendance, quizAverage, assignmentAverage, examAverage):
    final_score = calculate_weighted_average(
        totalAttendance, quizAverage, assignmentAverage, examAverage
    )

    if final_score >= 80:
        grade = "A"
    elif final_score >= 70:
        grade = "B"
    elif final_score >= 50:
        grade = "C"
    elif final_score >= 40:
        grade = "D"
    else:
        grade = "F"

    return grade


def generate_random_scores():
    totalAttendance = random.uniform(1, 100)

    if 0 <= totalAttendance <= 20:
        quizAverage = random.uniform(0, 20)
        assignmentAverage = random.uniform(0, 20)
        examAverage = random.uniform(20, 35)
    elif 21 <= totalAttendance <= 40:
        quizAverage = random.uniform(10, 30)
        assignmentAverage = random.uniform(10, 20)
        examAverage = random.uniform(35, 50)
    elif 41 <= totalAttendance <= 60:
        quizAverage = random.uniform(30, 50)
        assignmentAverage = random.uniform(30, 50)
        examAverage = random.uniform(50, 65)
    elif 61 <= totalAttendance <= 80:
        quizAverage = random.uniform(50, 70)
        assignmentAverage = random.uniform(50, 70)
        examAverage = random.uniform(65, 80)
    else:
        quizAverage = random.uniform(70, 90)
        assignmentAverage = random.uniform(70, 90)
        examAverage = random.uniform(80, 95)

    return {
        "totalAttendance": round(totalAttendance, 2),
        "quizAverage": round(quizAverage, 2),
        "assignmentAverage": round(assignmentAverage, 2),
        "examAverage": round(examAverage, 2),
    }


def create_data_and_export_to_csv(filename, num_records):
    data = []
    for i in range(num_records):
        record = generate_random_scores()
        record["index"] = i + 1

        overAllGrade = assign_grade(
            record["totalAttendance"],
            record["quizAverage"],
            record["assignmentAverage"],
            record["examAverage"],
        )
        record["overAllGrade"] = overAllGrade

        data.append(record)

    fieldnames = [
        "index",
        "totalAttendance",
        "quizAverage",
        "assignmentAverage",
        "examAverage",
        "overAllGrade",
    ]

    with open(filename, mode="w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)


create_data_and_export_to_csv("random_scores_with_grades.csv", 1000)
