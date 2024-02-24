import random

def generate_passwords(count):
    passwords = [str(random.randint(10000000, 99999999)) for _ in range(count)]
    return passwords

def save_to_file(passwords, filename):
    with open(filename, 'w') as file:
        for password in passwords:
            file.write(password + '\n')

if __name__ == "__main__":
    # Define the number of passwords to generate
    num_passwords = 1000000  # Adjust this as per your requirement
    
    # Generate the list of passwords
    passwords_list = generate_passwords(num_passwords)
    
    # Save passwords to a text file
    save_to_file(passwords_list, '1millpasswords.txt')
