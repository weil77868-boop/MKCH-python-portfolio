import csv
with open("students.csv", "r", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  students = list(reader)

averages = []
for s in students:
  chinese = int(s["chinese"])
  english = int(s["english"])
  math = int(s["math"])
  average = (chinese + english + math) / 3
  averages.append((s["name"], average))
  print(s["name"], f"{average:.2f}")

highest_student = max(averages, key=lambda student: student[1])
print("Highest average student:", highest_student[0], f"{highest_student[1]:.2f}")
highest_math = max(students, key=lambda student: int(student["math"]))
print("Highest math score student:", highest_math["name"], highest_math["math"])

failed_students = [s for s in students if int(s["chinese"]) < 60 or int(s["english"]) < 60 or int(s["math"]) < 60]
if failed_students:
  print("Failed students:")