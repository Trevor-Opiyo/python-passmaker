import random

def main():
  numbers = "1234567890"
  upper_case_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  lower_case_letters = "abcdefghijklmnopqrstuvwxyz"
  special_characters = "!@#$%^*()_-+={[}]|?><"
  possible_chars = ""
  pass_length = 0
  
  print("--------------------------------\n       Password Generator\n--------------------------------")
  possible_chars = input_entry("numbers", numbers, possible_chars)
  possible_chars = input_entry("upper-case letters", upper_case_letters, possible_chars)
  possible_chars = input_entry("lower-case letters", lower_case_letters, possible_chars)
  possible_chars = input_entry("special characters", special_characters, possible_chars)
  pass_length = assign_length()
  pass_return(pass_length, possible_chars)
  pass_regenerate(pass_length, possible_chars)
  
def input_entry(name, values, possible_chars):
  while True:
    response = input("Include " + name + "? [Y/N]\n")
    if (response == "Y") or (response == "y") or (response == "yes") or (response == "Yes"):
      possible_chars += values
      return possible_chars
    if (response == "N") or (response == "n") or (response == "no") or (response == "No"):
      return possible_chars
    print("Please enter valid input.")
    
def assign_length():
  while True:
    try:
      pass_length = int(input("Total number of characters? [integer]\n"))
      return pass_length
    except ValueError:
      print("Please enter valid input.")
      
def pass_return(pass_length, possible_chars):
  print("Your password is: ")
  while pass_length > 0:
    print(random.choice(possible_chars), end='')
    pass_length -= 1
    
def pass_regenerate(pass_length, possible_chars):
  while True:
    response = input(
      "\nWould you like to regenerate another password with the same parameters? [Y/N]\n")
    if (response == "Y") or (response == "y") or (response == "yes") or (response == "Yes"):
      pass_return(pass_length, possible_chars)
    if (response == "N") or (response == "n") or (response == "no") or (response == "No"):
      break
    if (response != "Y") and (response != "y") and (response != "N") and (response != "n") and (response == "yes") and (response == "Yes") and (response == "no") and (response == "No"):
      print("Please enter valid input.")
      
main()
