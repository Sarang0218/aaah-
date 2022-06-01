import sys
def DoesNotExist(char, lineNo="<stdin>"):
  print(f"[Line {lineNo+1}] ParsingError: Following token does not exist: {char}")
  print(f"The following error occurs when there is a token that is unrecognized by the scanner")
  sys.exit(1)
  


def IntegerUnderflowError(lineNo="<stdin>"):
  print(f"[Line {lineNo}] RuntimeError: PointerUnderflow.")
  print(f"The following error occurs when the pointer goes below zero.")
  sys.exit(1)

def IntegerOverflowError(lineNo="<stdin>"):
  print(f"[Line {lineNo}] RuntimeError: PointerOverflow.")
  print(f"The following error occurs when the pointer goes above the allocated memory.")
  sys.exit(1)


