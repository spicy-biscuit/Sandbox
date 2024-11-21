"""
Requires: N/A
Time Complexity: O(M * N) where M and N are the length and width
Memory Complexity: O(M * N) where M and N are the length and width
Input Type: List of a multi-line string. Will split on new lines and spaces.
"""

def SplitGrid(Grid):
  #Split the lines
  Grid = Grid[0].split("\n")

  #Takes a string and makes a list of ints
  def Func(String):
    String = String.split()
    String = list(map(int, String))
    return(String)

  #Applies func to every line in grid
  Grid = list(map(Func, Grid))
  return(Grid)