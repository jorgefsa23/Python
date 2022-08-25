'''Exercise from coderbyte.com [TAG: level easy]

take the str parameter being passed and determine if the string is a valid username according to the following rules:

    1. The username is between 4 and 25 characters.
    2. It must start with a letter.
    3. It can only contain letters, numbers, and the underscore character.
    4. It cannot end with an underscore character.

If the username is valid then your program should return the string "true", otherwise return the string "false".
    Examples
        Input: "aa_"
        Output: false
        Input: "u__hello_world123"
        Output: true
'''

import re


def CodelandUsernameValidation(strParam): 
  # code goes here
  if len(strParam)<4 or len(strParam)>25:
    return "false"
  if not strParam[0].isalpha():
    return "false"
  if strParam[-1] == "_":
    return "false"
  for letra in strParam:
    if not (bool(re.match("^[A-Za-z0-9_-]*$", strParam))):
      return "false"
  return "true"
  
# keep this function call here 
print(CodelandUsernameValidation(input("Inform username:  ")))
