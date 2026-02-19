class Boggle:
    def __init__(self, grid, dictionary):
        self.grid = grid
        self.dictionary = dictionary
        self.solutions = set() # for dic use set not list so no duplicate  

    def setGrid(self,grid):
      self.grid =[]
      for row in grid:
         clean_row = [tile.upper() for tile in row] #making every tile uppercase
         self.grid.append(clean_row)

 
    def setDictionary(self,dictionary):
      self.dictionary = set()#set()so no duplicates
      for word in dictionary:
         word = word.upper()#upper case each word
         if len(word) >= 3 and word.isalpha():# if > 3 and letters
            continue
         else:
            pass
         if "S" in word and "ST" not in word:
              continue
         if "Q" in word and "QU" not in word:
                continue
         if "I" in word and "IE" not in word:
                continue
               #set()so no duplicates/is alpha so upper case/no less than 3 
         self.dictionary.add(word)
         


    def findWords(self,word,row,col,index,visited):
       if row < 0 or row >= len(self.grid) or col < 0 or col >= len(self.grid[0]):
            return
       if (row, col) in visited:
          return
       tile = self.grid[row][col]#the order when search

       if word[index:index+len(tile)] == tile:#num letter = len of string
          new_index = index + len(tile)#goes to next index
          if new_index == len(word):
            self.solutions.add(word)
            return
          visited.add((row, col))
          for dr in [-1,0,1]: #directions dr= row dc= column
            for dc in [-1,0,1]:
               if dr == 0 and dc == 0:
                  continue
               self.findWords(word, row + dr, col + dc, new_index, visited)
          visited.remove((row, col))
                
         
         
       

    def getSolution(self):
      self.solutions = set()
      for word in self.dictionary:
         for r in range(len(self.grid)):
            for c in range(len(self.grid[0])):
               self.findWords(word,r,c,0,set())
      return sorted(list(self.solutions))

def main(): 
   grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
   dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet", "arty", "rhr", "not", "quar"]
    
   mygame = Boggle(grid, dictionary)
   mygame.setGrid(grid)
   mygame.setDictionary(dictionary)
   print(mygame.getSolution())

# def array_read()
if __name__ == "__main__":
    main()
