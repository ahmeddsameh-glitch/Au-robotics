operations =['uppercase', 'lowercase', 'capitalize', 'reverse' ]
s="ahmed"
def format_string(string, operations):
 for operation in operations:
  if operation == 'uppercase':
    string = _uppercase(string)
  elif operation == 'lowercase':
    string = _lowercase(string)
  elif operation == 'capitalize':
    string = _capitalize(string)
  elif operation =='reverse':
    string = _reverse(string)
 return string
def _uppercase(string):
 word =''
 for char in string:
  if 'a' <= char <= 'z':
    letter = chr(ord(char) - 32)
    word += letter
  else:
   word += letter
 print(word)
 return word
def _lowercase(string):
 word =''
 for char in string:
  if 'A' <= char <= 'Z':
    letter = chr(ord(char) + 32)
    word += letter
  else:
   word += letter
 print(word)
 return word
def _capitalize(string):
 
 firstChar = string[0]
 if 'a' <= firstChar <= 'z':
    firstChar = chr(ord(firstChar) - 32)
 print(firstChar+string[1:])
 return firstChar + string[1:]
def _reverse(string):
 string=string[::-1]
 print(string)
 return string
format_string(s, operations)

