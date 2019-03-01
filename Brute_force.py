###################################
#####  Made by   Hous Unus   ######
###################################


import string



class  password_generator():
    def __init__(self,Min=0):
        self.Min = Min
        self.ALLOWED_CHARACTERS = string.ascii_letters + string.digits+string.punctuation   #string.printable
        self.NUMBER_OF_CHARACTERS = len(self.ALLOWED_CHARACTERS)
        self.sequence = list(self.ALLOWED_CHARACTERS[0]*self.Min)
        self.last = ""
    def characterToIndex(self,char):
        return self.ALLOWED_CHARACTERS.index(char)

    def indexToCharacter(self,index):
        if self.NUMBER_OF_CHARACTERS <= index:
            raise ValueError("Index out of range.")
        else:
            return self.ALLOWED_CHARACTERS[index]

    def next(self,string):
        """ Get next sequence of characters.
        Treats characters as numbers (0-255). Function tries to increment
        character at the first position. If it fails, new character is
        added to the back of the list.
        It's basically a number with base = 256.
        :param string: A list of characters (can be empty).
        :type string: list
        :return: Next list of characters in the sequence
        :rettype: list
        """
        
        
        #print("Enter function")
        #print(string)
        if len(string) <= 0:
            string.append(self.indexToCharacter(0))
            #print("First time")
        else:
            string[0] = self.indexToCharacter((self.characterToIndex(string[0]) + 1) % self.NUMBER_OF_CHARACTERS)
            #print("not first")
            if self.characterToIndex(string[0]) is 0:
                #print("is 0 state")
                return list(string[0]) + self.next(string[1:])
                
        return string

    def GetPassword(self):
        
        self.sequence = self.next(self.sequence)
        password = ''.join(self.sequence)
        
        return password
    


        

