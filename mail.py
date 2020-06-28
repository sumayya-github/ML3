import smtplib
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()

s.login("sumayyakhatoon58@gmail.com", "********")


message = "Accuracy is less than 90%.Please try again"

s.sendmail("sumayyakhatoon58@gmail.com", "s8355827840@gmail.com", message)
    
s.quit()
