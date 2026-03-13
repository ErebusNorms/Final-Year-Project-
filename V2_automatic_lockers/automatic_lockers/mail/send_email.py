import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_real_email():
    sender = "nguyentienphuonghaui@gmail.com"
    password = "ilkdzvvfzypkhsar"  # Mật khẩu ứng dụng Gmail

    receiver = "huongnt1@phenikaa-x.com"
    subject = "Email tự động từ Python"
    body = "xin chào, tôi là ma"

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)  # Hoặc SMTP_SSL port 465
        server.starttls()  # Mã hóa kết nối
        server.login(sender, password)
        server.sendmail(sender, receiver, msg.as_string())
        server.quit()
        print("Email thực đã được gửi thành công!")
    except Exception as e:
        print("Lỗi khi gửi email:", e)

send_real_email()
