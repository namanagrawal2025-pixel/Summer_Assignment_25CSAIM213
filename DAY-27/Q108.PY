def generate_marksheet():
    name = input("Enter Student Name: ")
    roll = input("Enter Roll Number: ")
    sub1 = float(input("Enter Marks for Subject 1: "))
    sub2 = float(input("Enter Marks for Subject 2: "))
    sub3 = float(input("Enter Marks for Subject 3: "))
    
    total = sub1 + sub2 + sub3
    percentage = (total / 300) * 100
    
    if percentage >= 90:
        grade = "A+"
    elif percentage >= 75:
        grade = "A"
    elif percentage >= 50:
        grade = "B"
    else:
        grade = "C"
        
    print("\n--- MARKSHEET ---")
    print("Name:", name)
    print("Roll Number:", roll)
    print("Total Marks:", total, "/ 300")
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("-----------------")

def main():
    generate_marksheet()

main()
