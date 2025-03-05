student_count = 0

response = input("Do you want to enter student data? (Yes/No): ").strip().lower()

while response == "yes":
    last_name = input("Enter student last name: ")
    score1 = float(input("Enter first exam score: "))
    score2 = float(input("Enter second exam score: "))

    avg_score = (score1 + score2) / 2

    print("Student:", last_name)
    print("Average Score:", avg_score)

    student_count += 1

    response = input("Do you want to enter another student? (Yes/No): ").strip().lower()

print("Total students entered:", student_count)
