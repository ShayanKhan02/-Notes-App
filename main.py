def add_notes():
   note = input("Enter your note: ")
   with open("notes.txt","a")as f:
       f.write(note + "\n")
       print("Note saved!")
       
def view_notes():
   try:
      with open("notes.txt", "r") as f:
          notes = f.readlines()
          print("\nYour notes:")
          for note in notes:
             print(f"- {note.strip()}")
   except FileNotFoundError:
       print("No notes found!")

def clear_notes():
   with open("notes.txt","w")as f:
      f.write("")
      print("All notes cleared!")

while True:
    print("\n1. Add notes")
    print("2. View notes")
    print("3.Clear notes")
    print("4.Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
       add_notes()
    elif choice == "2":
        view_notes()
    elif choice == "3":
        clear_notes()
    elif choice == "4":
        break
    else:
        print("Invalid choice.")

      