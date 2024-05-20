import mysql.connector
from getpass import getpass
import hashlib

# Function to connect to MySQL database
def connect_to_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="sili1990",
            database="school_management_system"
        )
        return conn
    except mysql.connector.Error as err:
        print("Error connecting to MySQL database:", err)
        return None

# Function to create a new user
def register():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        username = input("Enter username: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        try:
            # Check if username already exists
            cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
            existing_user = cursor.fetchone()
            if existing_user:
                print("Username already exists. Please choose a different username.")
            else:
                # Insert new user
                cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, hashed_password))
                conn.commit()
                print("User registered successfully!")
        except mysql.connector.Error as err:
            print("Error registering user:", err)
        conn.close()

# Function to handle login
def login():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        username = input("Enter username: ")
        password = getpass("Enter password: ")  # Using getpass for secure password input
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        
        try:
            cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, hashed_password))
            user = cursor.fetchone()
            
            if user:
                print("Login successful!")
                username = user[1]  # Assuming username is the second column in your users table
                role = user[4]  # Assuming role is the fourth column in your users table
                print(f"Welcome, {username}!")
                print("User role:", role)
                
                # Redirect to appropriate page based on role
                if role.strip().lower() == "admin":
                    admin_page()
                elif role.strip().lower() == "staff":
                    staff_page()
                elif role.strip().lower() == "student":
                    student_page()
                elif role.strip().lower() == "parent":
                    parent_page()
                else:
                    print("Unknown role. Redirecting to home page.")
                    home_page()  # Default redirection if role doesn't match expected values
                    
            else:
                print("Invalid username or password.")
                
        except mysql.connector.Error as err:
            print("Error logging in:", err)
        
        conn.close()


# Function to handle password recovery
def forgot_password():
    conn = connect_to_database()
    if conn:
        cursor = conn.cursor()
        username = input("Enter your username: ")
        new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        hashed_password = hashlib.sha256(new_password.encode()).hexdigest()
        try:
            cursor.execute("UPDATE users SET password = %s WHERE username = %s", (hashed_password, username))
            conn.commit()
            print("Password reset successful! Your new password is:", new_password)
        except mysql.connector.Error as err:
            print("Error resetting password:", err)
        conn.close()

# Function to handle admin page
def admin_page():
    print("Welcome to the admin page!")
    print("Admin functionalities go here.")

# Function to handle staff page
def staff_page():
    print("Welcome to the staff page!")
    print("Staff functionalities go here.")

# Function to handle student page
def student_page():
    print("Welcome to the student page!")
    print("Student functionalities go here.")

# Function to handle parent page
def parent_page():
    print("Welcome to the parent page!")
    print("Parent functionalities go here.")

# Function to handle home page
def home_page():
    print("Welcome to the home page!")
    print("General functionalities go here.")

# Main function to handle user interactions
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")




# Updated main function with additional options
def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Forgot Password")
        print("4. Schools")
        print("5. Colleges")
        print("6. Universities")
        print("7. Reviews & Ratings")
        print("8. Contact Us")
        print("9. Career")
        print("10. Support")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            forgot_password()
        elif choice == "4":
            schools_page()
        elif choice == "5":
            colleges_page()
        elif choice == "6":
            universities_page()
        elif choice == "7":
            reviews_ratings_page()
        elif choice == "8":
            contact_us_page()
        elif choice == "9":
            career_page()
        elif choice == "10":
            support_page()
        elif choice == "11":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

# Function to handle schools page
def schools_page():
    print("\nTop Rated Schools:")
    # Implement fetching and displaying top-rated schools with filters/sorting
    # Example: Fetch data from database and display

# Function to handle colleges page
def colleges_page():
    print("\nTop Rated Colleges:")
    # Implement fetching and displaying top-rated colleges with filters/sorting
    # Example: Fetch data from database and display

# Function to handle universities page
def universities_page():
    print("\nTop Rated Universities:")
    # Implement fetching and displaying top-rated universities with filters/sorting
    # Example: Fetch data from database and display

# Function to handle reviews & ratings page
def reviews_ratings_page():
    print("\nReviews & Ratings:")
    # Implement functionality related to reviews and ratings
    # Example: Allow users to view and submit reviews

# Function to handle contact us page
def contact_us_page():
    print("\nContact Us:")
    # Implement contact form or details display
    # Example: Allow users to send inquiries or feedback

# Function to handle career page
def career_page():
    print("\nCareer:")
    # Implement career opportunities or job listings
    # Example: Display job openings and application details

# Function to handle support page
def support_page():
    print("\nSupport:")
    # Implement support information or FAQs
    # Example: Provide support contact details and FAQs

# Updated home page with navigation options
def home_page():
    print("Welcome to the home page!")
    print("Choose an option:")
    print("1. Schools")
    print("2. Colleges")
    print("3. Universities")
    print("4. Reviews & Ratings")
    print("5. Contact Us")
    print("6. Career")
    print("7. Support")
    print("8. Logout")

    option = input("Enter your choice: ")
    if option == "1":
        schools_page()
    elif option == "2":
        colleges_page()
    elif option == "3":
        universities_page()
    elif option == "4":
        reviews_ratings_page()
    elif option == "5":
        contact_us_page()
    elif option == "6":
        career_page()
    elif option == "7":
        support_page()
    elif option == "8":
        print("Logging out...")



if __name__ == "__main__":
    main()



