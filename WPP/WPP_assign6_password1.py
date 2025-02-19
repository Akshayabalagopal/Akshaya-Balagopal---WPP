'''Write a class called Password_manager. The class should have a list called old_passwords that
holds all of the user’s past passwords. The last item of the list is the user’s current pass word.
There should be a method called get_password that returns the current password and a method
called set_password that sets the user’s password. The set_password method should only
change the password if the attempted password is different from all the user’s past passwords.
Finally, create a method called is_correct that receives a string and returns a boolean True or
False depending on whether the string is equal to the current password or not.
'''

class password_manager():
    def __init__(self):
        self.old_passwords=[]

    def get_password(self):
        if self.old_passwords:
            return self.old_passwords[-1]
        return None
    
    def set_password(self, new_password):
        if new_password not in self.old_passwords:
            self.old_passwords.append(new_password)
            print("Password set successfully")
        else:
            print("New password not the same")

    def is_correct(self,password):
        return password==self.get_password()
    
def main():
    pm = password_manager()

    while True:
        print("\nPassword Manager: ")
        print("1. Set password: ")
        print("2. Check current password: ")
        print("3. Verify the password: ")
        print("4. Exit")
        choice=input("Enter your choice: ")

        if choice=='1':
            new_password=input("Enter the password: ")
            pm.set_password(new_password)

        elif choice=='2':
            current_password=pm.get_password()
            if current_password:
                    print(f"Current password: {current_password}")
            else:
                print("No password")

        elif choice == '3':
            password = input("Enter password to verify: ")
            if pm.is_correct(password):
                print("Correct password.")
            else:
                print("Incorrect password.")

        elif choice == '4':
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__=="__main__":
    main()





