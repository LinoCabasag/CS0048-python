from mp3function import *

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def classify_bp(systolic, diastolic):
    if systolic < 120 and diastolic < 80:
        return "Normal"
    elif 120 <= systolic < 130 and diastolic < 80:
        return "Elevated"
    elif systolic >= 130 or diastolic >= 80:
        return "High"
    else:
        return "Unknown"
    
def get_reading(prompt):
    while True:
        try:
            value = input(prompt)
            value = float (value)
            if value < 0:
                print ("Invalid input: Blood pressure readings cannot be negative.")
                return None
            return value
        except ValueError:
            print ("Invalid Input: Please enter a valid number.")
    
def health_monitor():
    count = {"Normal": 0, "Elevated": 0, "High": 0}

    print ("\n Welcome to weekly Health Monitoring System\n")

    for day in days:
        print ("\n Enter readings for (day):")
        systolic = get_reading ("   Systolic: ")
        if systolic is None:
             continue
        diastolic = get_reading ("   Diastolic: ")
        if diastolic is None:
            continue
            
            
        category = classify_bp(systolic, diastolic)
        print (f"   Classification for {day}: {category}")
        if category in count:
                count [category] += 1

    print("\n--- Weekly Summary Report ---")
    print(f"Normal: {count[ 'Normal']} day(s)")
    print(f"Elevated: {count['Elevated']} day(s)")
    print(f"High: {count['High']} day(s)")

    if count ['High'] > 3:
        print ("Warning: More than 3 days classified as High. Please consult a doctor.")

if __name__ == "__main__":
    health_monitor()

