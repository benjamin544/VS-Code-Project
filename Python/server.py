# ייבוא ספריית socket לתקשורת רשת
import socket
# ייבוא ספריית os לעבודה עם מערכת הקבצים
import os
# ייבוא ספריית subprocess להרצת פקודות מערכת
import subprocess

# פונקציה לטיפול בלקוח שמתחבר לשרת
def handle_client(client_socket):
    try:
        # הודעה כאשר הלקוח מתחבר
        print("Client connected")
        while True:
            # קבלת נתונים מהלקוח
            data = client_socket.recv(1024).decode()
            if not data:  # אם אין נתונים, סיום הלולאה
                break

            # הדפסת הפקודה שהתקבלה
            print(f"Received command: {data}")
            
            # בדיקת סיום החיבור
            if data.lower() == 'exit':  
                print("Client disconnected")
                client_socket.send("Goodbye!".encode())  # שליחת הודעת פרידה ללקוח
                break

            # החזרת תיקיית העבודה הנוכחית
            elif data.lower() == 'pwd':  
                cwd = os.getcwd()  # קבלת הנתיב הנוכחי
                print(f"Sending current working directory: {cwd}")
                client_socket.send(cwd.encode())  # שליחת הנתיב ללקוח
            
            # החזרת רשימת הקבצים בתיקייה הנוכחית
            elif data.lower() == 'ls':  
                files = os.listdir(os.getcwd())  # קבלת רשימת הקבצים
                print(f"Sending files: {files}")
                client_socket.send('\n'.join(files).encode())  # שליחת הרשימה כטקסט
            
            # החזרת הודעה שנשלחה עם הפקודה 'echo'
            elif data.lower().startswith('echo'):  
                message = data[5:]  # חיתוך הטקסט אחרי 'echo '
                print(f"Sending echo message: {message}")
                client_socket.send(message.encode())  # שליחת ההודעה חזרה
            
            # הצגת זמן עבודה של השרת
            elif data.lower() == 'uptime':  
                uptime = subprocess.check_output("uptime", shell=True).decode()  # הרצת פקודת uptime
                print(f"Sending uptime: {uptime}")
                client_socket.send(uptime.encode())  # שליחת הזמן ללקוח

            # הצגת התאריך והשעה הנוכחיים
            elif data.lower() == 'date':  
                date = subprocess.check_output("date", shell=True).decode()  # הרצת פקודת date
                print(f"Sending date: {date}")
                client_socket.send(date.encode())  # שליחת התאריך ללקוח

            # טיפול בפקודות שאינן מוכרות
            else:  
                response = f"Unknown command: {data}"
                print(f"Sending unknown command response: {response}")
                client_socket.send(response.encode())  # שליחת תגובה מתאימה
    except Exception as e:
        # טיפול בשגיאות
        print(f"Error: {e}")
        client_socket.send(f"Error: {e}".encode())  # שליחת הודעת שגיאה ללקוח
    finally:
        # סגירת חיבור הלקוח
        client_socket.close()

# הפונקציה הראשית של השרת
def main():
    # יצירת socket עם פרוטוקול TCP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # קשירה לכתובת 0.0.0.0 (כל הכתובות) ולפורט 4545
    server_socket.bind(('0.0.0.0', 4545))  
    # האזנה לחיבורים נכנסים עם עד 5 חיבורים בתור
    server_socket.listen(5)
    print("Server listening on port 4545")

    while True:
        # קבלת חיבור חדש
        client_socket, addr = server_socket.accept()
        print(f"Client connected: {addr}")
        # טיפול בלקוח
        handle_client(client_socket)

# התחלת התוכנית
if __name__ == "__main__":
    main()




