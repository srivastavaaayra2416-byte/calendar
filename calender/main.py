import display
import calendar_math
import models
import storage

def run():
    while True:
        choice = display.show_menu()
        
        if choice == "1":
            y = int(input("Enter Year (e.g., 2026): "))
            m = int(input("Enter Month (1-12): "))
            print("\n" + calendar_math.get_text_calendar(y, m))
            
        elif choice == "2":
            date = input("Enter Date (e.g., 15-Oct): ")
            note = input("Enter your note: ")
            formatted_text = models.format_event(date, note)
            storage.save_data(formatted_text)
            print("Saved!")
            
        elif choice == "3":
            print("\n--- YOUR EVENTS ---")
            print(storage.read_data())
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    run()