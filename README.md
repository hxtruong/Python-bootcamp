# Learn Python Course
#### Note some interesting things
-- Self-taught
## Python Object and Data Structure Basics
- Power in number: ** . Ex: 2**4 = 2^4 = 16
- Negative index in string. Ex: str= 'Truong' -> str[-1] = 'g' mean this last character of string
- Get character in string: str[START:END:STEP]. Note: not including character[END]
- Function Split:
  * str.split() -> split each word in a string as array
  * str.split('i') -> split until meet character 'i'. Ex: str = "Hello! This is an bird." -> 'Hello! Th', 's ', 's an b', 'rd.'
- Format in print: use '{}'.format  to print string/result follow defined format
- Set just get the unique element. Ex: myset = set(); myset.add(element)
- IO file
  * open(), read()
  * when read() file, the cursor will be moved the end of file. Use seek(int) to set again cursor
  * read() evert line: readlines() -> list string follow each line in file
  * with open('myfile.txt') as my_new_file:
      contents = my_new_file.read()
      -> file open and close automatically, the contents in file will independence with file
## Statements
- Key word 'enumerate' use show (index, result) in loop
- Key word 'Zip' use zip lists together follow index
## Function
- *args : list of parameter when pass to Function
- **kwargs:  return a dictionary  
