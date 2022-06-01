import errors
class VirtualMachine():
  def __init__(self):
    self.pointer = 0
    self.memory = [0]*64 #FIFO
  def movePointer(self, tok, no=1):
    self.pointer += no
    if self.pointer < 0:
      errors.IntegerUnderflowError(tok[1])
    if self.pointer >= 64:
      errors.IntegerOverflowError(tok[1])
  def addToSpot(self, tok, val=1):
    self.memory[self.pointer] += val
  def getSpot(self, tok):
    return self.memory[self.pointer]
    
      

  
    
    

    
  