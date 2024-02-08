class first:
    string='' # Class attribute to store the string
    
    # Method to get the string from the user
    def get_String(s):
        s.string=input("Enter string: ")
        # Method to print the string in uppercase
    def print_String(s):
        print(s.string.upper())
        # Object creation 
object=first()
object.get_String()
object.print_String()
#ans Enter string: hello
#HELLO