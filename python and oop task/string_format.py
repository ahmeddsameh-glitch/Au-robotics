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
 string=string.upper()
 print(string)
 return string
def _lowercase(string):
 string=string.lower()
 print(string)
 return string
def _capitalize(string):
 string=string.capitalize()
 print(string)
 return string
def _reverse(string):
 string=string[::-1]
 print(string)
 return string
format_string(s, operations)

