from datetime import *
p=datetime.now()
print(p)



from datetime import datetime
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)