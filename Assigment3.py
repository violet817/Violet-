#Question 1
def classify_number():
    while True:
        user_input1 = input("Enter an integer: ")
        try:
            numbers = int(user_input1)  # Try converting input to integer
            break  # If successful, exit the loop
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    if numbers > 0:
        return "Positive"
    elif numbers < 0:
        return "Negative"
    else:
        return "Zero"

result = classify_number()
print("The number is:", result)

#Question 2
def calculate_average(*args):

    if len(args) == 0:
        return 0
    return sum(args) / len(args)


print(calculate_average(100, 250, 310))  # Output: 20.0
print(calculate_average())            # Output: 0

#Question 3
while True:
    try:
        user_input = input("Please enter a number: ")
        number = float(user_input)
        print(f"You entered the number: {number}")
        break  # Exit the loop if the input is valid
    except ValueError:
        print("Invalid input! Please enter a valid number.")

#Question4
# List of names to write to the file
names = ["John", "Peter", "Mark", "David"]

# Write names to 'names.txt', each on a new line
with open("names.txt", "w") as file:
    for name in names:
        file.write(f"{name}\n")

# Read the file and print each name
with open("names.txt", "r") as file:
    for line in file:
        print(line.strip())

#Question5
celsius = [0,15,25,30,100]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

def divide_numbers(numerator, denominator):

    try:
        result1 = numerator / denominator
        return result1
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print ("Error: Both numerator and denominator must be numbers.")
        return None

print(divide_numbers(10, 2))
print(divide_numbers(10, 0))
print(divide_numbers(10, 'g'))

#Question 7
# Define the custom exception
class NegativeNumberError(Exception):
    """Exception raised when a negative number is encountered."""
    pass


# Function that checks if a number is positive
def check_positive(number1):
    """
    Raises NegativeNumberError if the number is negative.

    Parameters:
        number1 (int or float): The number to check.
    """
    if number1 < 0:
        raise NegativeNumberError("Negative numbers are not allowed.")
    else:
        print(f"{number1} is positive.")


# Demonstration using try-except
try:
    num = -5
    check_positive(num)
except NegativeNumberError as e:
    print("Error:", e)

#Question8
import random

def generate_random_numbers(a, b, c):
    """
    Generate a list of random integers.

    Parameters:
        a (int): Number of integers to generate.
        b (int): Lowest possible integer.
        c (int): Highest possible integer.

    Returns:
        list: A list of random integers.
    """
    return [random.randint(b, c) for _ in range(a)]

def calculate_average(numbers):
    """
    Calculate the average of a list of numbers.

    Parameters:
        numbers (list): A list of numeric values.

    Returns:
        float: The average of the numbers.
    """
    return sum(numbers) / len(numbers)

# Generate 10 random integers between 1 and 100
random_numbers = generate_random_numbers(20, 1, 100)

# Calculate the average
average = calculate_average(random_numbers)

# Print the results
print("Random numbers:", random_numbers)
print("Average:", average)

#Question9
import re

# Part I: Extract all email addresses from a given text
def extract_emails(text):
    """
    Extracts all email addresses from the given text.
    """
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

# Part II: Validate a date in the format YYYY-MM-DD
def validate_date(date_string):
    """
    Validates if the given string is a date in YYYY-MM-DD format.
    """
    pattern = r"^\d{4}-\d{2}-\d{2}$"
    return bool(re.match(pattern, date_string))

# Part III: Replace all occurrences of a word with another word
def replace_word(text, old_word, new_word):
    """
    Replaces all occurrences of old_word with new_word in the given text.
    """
    pattern = rf"\b{re.escape(old_word)}\b"
    return re.sub(pattern, new_word, text)

# Part IV: Split a string by all non-alphanumeric characters
def split_by_non_alphanumeric(text):
    """
    Splits the string by all non-alphanumeric characters.
    """
    return re.split(r"[^A-Za-z0-9]+", text)

# -------------------- Example Usage --------------------

# I. Extract emails
sample_text = "Contact us at Nobody@gmail.com or Reply@mumushop.org for more info."
emails = extract_emails(sample_text)
print("Extracted emails:", emails)

# II. Validate dates
print("Is '2025-09-12' a valid date?", validate_date("2025-09-12"))
print("Is '12/09/2025' a valid date?", validate_date("12/09/2025"))

# III. Replace words
original_text = "The quick brown fox jumps over the brown fox!"
updated_text = replace_word(original_text, "fox", "cat")
print("Updated text:", updated_text)

# IV. Split by non-alphanumeric characters
text_to_split = "Hello how are you today_123."
parts = split_by_non_alphanumeric(text_to_split)
print("Split parts:", parts)

#Question10
import socket

def start_server(host='127.0.0.1', port=65432):
    """
    Starts a TCP server that listens for incoming client connections
    and sends a greeting message.
    """
    # Create a TCP/IP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the host and port
        server_socket.bind((host, port))
        print(f"Server started on {host}:{port}")

        # Listen for incoming connections (max 1 connection in the queue)
        server_socket.listen(1)
        print("Waiting for a client to connect...")

        # Accept a client connection
        conn, addr = server_socket.accept()
        with conn:
            print(f"Connected by {addr}")
            message = "Hello from server!"
            conn.sendall(message.encode())  # Send message to client
            print(f"Message sent to client: {message}")

    except socket.error as f:
        print(f"Socket error: {f}")

    finally:
        # Ensure the socket is closed properly
        server_socket.close()
        print("Server socket closed.")

if __name__ == "__main__":
    start_server()

#Question11
What_is_API= ["API stands for Application Programming Interface, "
              "It is a set of rules and protocols that allows different software programs to communicate with each other.,"
              "Web APIs let your program send and receive data over the internet (usually in JSON format)., "
              "For example, you might use an API to get weather data, stock prices, or user information from a web service."]
Make_GET= ["Step-by-step explanation:,"
           "Import requests – Gives you tools to send HTTP requests,"
           "Use requests.get(url) – Sends a GET request to the specified URL,"
           "Check response.status_code – Ensures the request was successful.,"
           "Use response.json() – Converts JSON response to a Python dictionary.,"
           "Handle exceptions – Catches any network-related errors."]

Connect_SQLite_Database= ["Step-by-step explanation:,"
                          "Connect to the database — sqlite3.connect example.dbn opens (or creates) a database file.,"
                          "Create a cursor — connection.cursor() gives you a way to run SQL commands.,"
                          "Create tables — CREATE TABLE sets up the structure for storing data.,"
                          "Insert data — INSERT INTO adds records to the table.,"
                          "Commit changes — connection.commit() permanently saves changes.,"
                          "Query data — SELECT * FROM reads data from the database.,"
                          "Close the connection — Frees system resources and ensures changes are saved."]