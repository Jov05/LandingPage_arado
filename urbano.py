
def grade_classification():
    try:
        grade1 = float(input("Enter grade 1: "))
        grade2 = float(input("Enter grade 2: "))
        grade3 = float(input("Enter grade 3: "))

        average = (grade1 + grade2 + grade3) / 3

        if average > 100 or average <= 50:
            print("Invalid Grade")
        elif 98 <= average <= 100:
            print(f"Average: {average:.2f} - With Highest Honor")
        elif 95 <= average <= 97:
            print(f"Average: {average:.2f} - With High Honor")
        elif 90 <= average <= 94:
            print(f"Average: {average:.2f} - With Honor")
        elif 75 <= average <= 89:
            print(f"Average: {average:.2f} - Passed")
        elif 51 <= average <= 74:
            print(f"Average: {average:.2f} - Failed")
        else:
            print("Invalid Grade")
    except ValueError:
        print("Invalid input. Please enter valid numeric values for the grades.")

grade_classification()