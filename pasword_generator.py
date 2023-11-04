import random
import string

def generate_password(length, complexity):
  password = ""

  if complexity == "low":
    characters = string.ascii_lowercase
  elif complexity == "medium":
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits
  elif complexity == "high":
    characters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
  else:
    raise ValueError("Invalid complexity")

  for i in range(length):
    password += random.choice(characters)

  return password


def main():
  # Prompt the user to specify the desired length of the password.
  length = int(input("Enter the desired length of the password: "))

  # Generate a random password using the `generate_password()` function.
  password = generate_password(length, "high")

  # Display the generated password on the screen.
  print(f"Your generated password is: {password}")


if __name__ == "__main__":
  main()
