# Setup imports
import sys

# Setup vars
pwdGood = False

# Function to check length
def checkLength(pwd):
  if len(pwd) > 6:
    return True
  else:
    return False

# Function to check for numeric digit
def alphaNum(pwd):
  for chr in (pwd):
    if chr.isdigit():
      return True 
  return False

# Function to check for upper / lower case
def diffCases(pwd):
  pwdLwr = str.lower(pwd)
  if pwdLwr != pwd:
    return True
  return False

# Loop until a good password is entered
while pwdGood is False:
 
  # raw_input should be compatible with all OSes 
  Password = raw_input ("Please enter a password:\n")
 
  # call each function in turn which returns a boolean value
  # these can then be used to form an overall check 
  pwdchk1 = checkLength(Password)
  pwdchk2 = alphaNum(Password)
  pwdchk3 = diffCases(Password)

  # examine all checks
  if pwdchk1 is True and pwdchk2 is True and pwdchk3 is True:
    print("Password is good")
    sys.exit(0)
  else:
    print("Password invalid")
    if pwdchk1 is False:
      print("Failed length check")
    if pwdchk2 is False:
      print("Failed numeric check")
    if pwdchk3 is False:
      print("Failed case check")
