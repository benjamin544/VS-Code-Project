import random  # ייבוא מודול ליצירת מספרים אקראיים

def generate_random_number():
    """
    פונקציה ליצירת מספר אקראי בין 1 ל-100.
    """
    return random.randint(1, 100)  # יצירת מספר אקראי בין 1 ל-100

def check_even_or_odd(number):
    """
    פונקציה לבדיקת זוגיות או אי-זוגיות של מספר.
    """
    if number % 2 == 0:  # אם השארית בחלוקה ב-2 היא 0, המספר זוגי
        return "Even"
    else:
        return "Odd"  # אחרת, המספר אי-זוגי

def save_result_to_file(number, result, filename="results.txt"):
    """
    פונקציה לשמירת המספר והתוצאה בקובץ.
    """
    with open(filename, "a") as file:  # פתיחת קובץ במצב "הוספה"
        file.write(f"Number: {number}, Result: {result}\n")  # כתיבת התוצאה

def main():
    print("Welcome to the Random Number Checker!")  # הודעה למשתמש
    number = generate_random_number()  # יצירת מספר אקראי
    result = check_even_or_odd(number)  # בדיקת זוגיות
    print(f"The random number is {number}, and it is {result}.")  # הצגת התוצאה למשתמש
    save_result_to_file(number, result)  # שמירת התוצאה בקובץ
    print("The result has been saved to results.txt.")  # הודעה שהנתונים נשמרו

if __name__ == "__main__":
    main()  # קריאה לפונקציה הראשית
