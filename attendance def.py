def attendance(roll_number):
    data = {
        1: "Present",
        2: "Absent",
        3: "Present",
        4: "Present",
        5: "Present",
        6: "Present",
        7: "Present",
        8: "Absent",
        9: "Present",
        10: "Present",
        11: "Absent",
        12: "Present",
    }
    if roll_number in data:
        print(f"roll number {roll_number} is {data[roll_number]}")
    else:
        print("roll number is not found",roll_number)
input_roll = int(input("Enter the roll number: "))
attendance(input_roll)










# def attendance(roll_number):

    
#     if roll_number % 2 == 0:
#         return "Present"
#     else:
#         return "Absent"


# roll_number = int(input("Enter the roll number: "))
# check = attendance(roll_number)
# print(f"roll number {roll_number} is {check}.")