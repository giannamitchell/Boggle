class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = [] # for dic use set not list so no duplicate  

    def setGrid(self,grid):
      self.grid =[]
      for row in grid:
         clean_row = [tile.upper() for tile in row] 
         self.grid.append(clean_row)

 
    def setDictionary(self,dictionary):
      self.dictionary = set()#set()so no duplicates
      for word in dictionary:
         word = word.upper()#upper case each word
         if len(word) >= 3 and word.isalpha:# if > 3 and letters
            self.dictionary.add(word)
         else:
            pass
               #set()so no duplicates/is alpha so upper case/no less than 3 


    def findWords(self,word,row,col,visited):
      #no less than 3 letters for word

    def getSolution(self):
      #test cases Qu as one cube 

def main():#use getter and setter methods here
    grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())

# def array_read()
if __name__ == "__main__":
    main()
