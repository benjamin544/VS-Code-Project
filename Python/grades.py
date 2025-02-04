# יצירת קובץ עם ציונים לדוגמה
with open("grades.txt", "w", encoding="utf-8") as file:
    file.write("Hadas,85\n")
    file.write("Chen,90\n")
    file.write("Aviel,78\n")
    file.write("Doron,92\n")
    file.write("Tal,88\n")

# פונקציה לקריאת הציונים מהקובץ
def read_grades_from_file(file_name):
    grades = []
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line in file:
                name, grade = line.strip().split(",")
                grades.append((name, int(grade)))
    except FileNotFoundError:
        print(f"Error: The file '{file_name}' was not found.")
    except ValueError:
        print("Error: Issue with the file format. Ensure each line is in the format 'name,score'.")
    return grades

# פונקציה לחישוב ממוצע הציונים
def calculate_average(grades):
    if not grades:
        return 0
    total = sum(grade for _, grade in grades)
    return total / len(grades)

# פונקציה למציאת הציון הנמוך והגבוה ביותר
def find_min_and_max(grades):
    if not grades:
        return None, None
    grades_only = [grade for _, grade in grades]
    return min(grades_only), max(grades_only)

# פונקציה ראשית שמבצעת את כל השלבים
def main():
    file_name = "grades.txt"
    grades = read_grades_from_file(file_name)
    
    if not grades:
        print("Error: No grades to process in the file.")
        return

    average = calculate_average(grades)
    min_grade, max_grade = find_min_and_max(grades)

    print(f"Average grade: {average:.2f}")
    print(f"Lowest grade: {min_grade}")
    print(f"Highest grade: {max_grade}")

# הפעלת התוכנית
if __name__ == "__main__":
    main()
