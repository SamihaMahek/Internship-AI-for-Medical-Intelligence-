#Build a smart attendance calculator that shows attendance percentage and warns students if it is below 75%
total_classes = int(input("Enter total number of classes: "))
attended_classes = int(input("Enter attended classes: "))

attendance = (attended_classes / total_classes) * 100

print("Attendance Percentage =", attendance, "%")

if attendance < 75:
    print("Warning: Attendance is below 75%!")
else:
    print("Good! Attendance is above 75%.")