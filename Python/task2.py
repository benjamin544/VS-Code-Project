import json

# טוען את קובץ ה-JSON
with open("C:/Users/Benjamin/Desktop/Devops/employees.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# הדפסת שם החברה בלבד
print(data["company"])

