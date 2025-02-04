# ייבוא ספריית socket לתקשורת רשת
import socket

# הפונקציה הראשית של הלקוח
def main():
    # כתובת ה-IP של השרת
    server_ip = "10.100.102.8"
    # מספר הפורט של השרת
    server_port = 4545
    # יצירת socket עם פרוטוקול TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # התחברות לשרת עם הכתובת והפורט שצוינו
        client_socket.connect((server_ip, server_port))
        print(f"Connected to server {server_ip}:{server_port}")

        while True:
            # קבלת קלט מהמשתמש לשליחה לשרת
            message = input("Enter msg: ")
            # שליחת ההודעה לשרת
            client_socket.send(message.encode())
            # בדיקה אם המשתמש שלח את הפקודה 'exit' לסיום החיבור
            if message.lower() == 'exit':
                print("Disconnected from server.")
                break
            # קבלת תגובה מהשרת והצגתה
            response = client_socket.recv(1024).decode()
            print(f"Server said: {response}")

    except Exception as e:
        # טיפול בשגיאות והצגת הודעה במקרה של בעיה
        print(f"Error: {e}")
    finally:
        # סגירת החיבור עם השרת
        client_socket.close()

# התחלת התוכנית
if __name__ == "__main__":
    main()



