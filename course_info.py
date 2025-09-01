def main():
    # Create dictionaries with course information
    room_numbers = {
        "CSC101": "3004",
        "CSC102": "4501",
        "CSC103": "6755",
        "NET110": "1244",
        "COM241": "1411"
    }
    
    instructors = {
        "CSC101": "Haynes",
        "CSC102": "Alvarado",
        "CSC103": "Rich",
        "NET110": "Burke",
        "COM241": "Lee"
    }
    
    meeting_times = {
        "CSC101": "8:00 a.m.",
        "CSC102": "9:00 a.m.",
        "CSC103": "10:00 a.m.",
        "NET110": "11:00 a.m.",
        "COM241": "1:00 p.m."
    }
    
    print("Course Information System")
    print("=========================")
    print("Available courses: CSC101, CSC102, CSC103, NET110, COM241")
    print("Enter 'quit' to exit the program\n")
    
    while True:
        # Get user input
        course_number = input("Enter a course number: ").strip().upper()
        
        # Check if user wants to quit
        if course_number == "QUIT":
            print("Thank you for using the Course Information System!")
            break
        
        # Check if course exists and display information
        if course_number in room_numbers:
            print(f"\nCourse: {course_number}")
            print(f"Room Number: {room_numbers[course_number]}")
            print(f"Instructor: {instructors[course_number]}")
            print(f"Meeting Time: {meeting_times[course_number]}\n")
        else:
            print(f"Error: Course '{course_number}' not found. Please try again.\n")

if __name__ == "__main__":
    main()