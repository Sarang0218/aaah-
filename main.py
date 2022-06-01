# PYTHON IMPLEMENTATION
import errors
import vm
with open("main.ahh", "r") as source:
  charStream = source.read()
def lexer(charstream):
  toktype = {
    "a":"ADD",
    "h":"SUBTRACT",
    "!":"PRINT",
    "\n":"MOVE FORWARD",
    "?": "ASCII",
    "#":"MOVE BACK",
    "~":"NEWLINE",
    "d":"DEBUG"
    
  }
  toks = []
  lineNo = 0
  for char in charstream:   
    if char in toktype.keys():
      toks.append([toktype[char], lineNo])
      if char == "\n":
        lineNo += 1
    elif char in "\t ":
      pass
    else:
      errors.DoesNotExist(char, lineNo)
  return toks
def interpreter(tokens):
  VM = vm.VirtualMachine()
  pre = ""
  for tok in tokens:
    if tok[0] == "ADD":
      VM.addToSpot(tok, 1)
    elif tok[0] == "SUBTRACT":
      VM.addToSpot(tok, -1)
    elif tok[0] == "PRINT":
      if pre != "": print(pre, end=""); pre = ""
      else: print(VM.getSpot(tok), end="")
    elif tok[0] == "MOVE FORWARD":
      VM.movePointer(tok, 1)
    elif tok[0] == "ASCII":
      pre = chr(VM.getSpot(tok))
    elif tok[0] == "MOVE BACK":
      VM.movePointer(tok, -1)
    elif tok[0] == "NEWLINE":
      print("\n", end="") 
   
def debug(orig, tok):
  print("AHH! Interpreter (v. 1.0)")      
  print("-------------------------")
  print("By CompilingCoder")
  print("-------------------------")
  print("main.ahh:")
  print(orig)
  print("Tokens:")
  print(tok)
  print("Result:")
tokens = lexer(charStream)
debug(charStream,tokens)
interpreter(tokens)

  