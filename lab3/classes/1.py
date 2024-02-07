class first:
    string='' # Class attribute to store the string
    
    # Method to get the string from the user
    def get_String(k):
        k.string=input("Enter string: ")
        # Method to print the string in uppercase
    def print_String(k):
        print(k.string.upper())
        # Object creation 
obj=first()
obj.get_String()
obj.print_String()