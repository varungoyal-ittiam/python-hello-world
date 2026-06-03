# Intentional style and type violations for testing the GitHub Actions linter.
# This file is used to verify that .pylintrc and mypy flag style and type
# issues.
#
# fmt: off  # Disable editor auto-formatting to preserve testing violations!

"""Toy test module containing intentional style and type violations."""

# 1. Multiple imports on a single line.
# (Expected: multiple-imports / C0410)
import os, sys

# 2. Multiple statements on a single line.
# (Expected: multiple-statements / C0321)
def inline_helper(): x = 1; y = 2

# 3. Invalid function name style.
# (Expected: invalid-name / C0103 - CapWords function name)
def BadFunctionName(param_a):
  print(param_a)

# 4. Invalid class name style.
# (Expected: invalid-name / C0103 - snake_case class name)
class my_invalid_class:
  
  def __init__(self):
    pass

# 5. Dangerous default value (mutable) as argument.
# (Expected: dangerous-default-value / W0102)
def append_to_list(element, target_list=[]):
  target_list.append(element)
  return target_list

# 6. Bad indentation - uses 4 spaces instead of 2.
# (Expected: bad-indentation / W0311)
def indented_function():
    # 4 spaces!
    print("This has 4-space indentation, but pylintrc expects 2.")

# 7. Line too long - exceeds 80 characters.
# (Expected: line-too-long / C0301)
a_very_long_string_variable_that_exists_only_to_exceed_the_eighty_character_limit_value = "very long!"

# 8. Bare except clause.
# (Expected: bare-except / W0702)
try:
  res = 1 / 0
except:
  print("Failed to divide")

# 9. Unused variable definition.
# (Expected: unused-variable / W0612)
def unused_variable_test():
  unused_var = 123
  print("Done")

# 10. Type mismatch violation.
# (Expected: Mypy error - returning int when signature specifies str)
def type_check_test(val: int) -> str:
  # Returning int instead of str. Mypy should catch this!
  return val

# 11. Bad whitespace - missing space after comma.
# (Expected: bad-whitespace / C0326)
for (x,y) in [(1, 2)]:
  print(x)

# 12. Non-idiomatic comparison negation (not a in b).
# (Expected: g-comparison-negation)
my_list = [1, 2, 3]
if not 4 in my_list:
  print("4 is not in list")

# 13. Import not at top level.
# (Expected: g-import-not-at-top)
def calculate_square_root(value):
  import math  # Inline import!
  return math.sqrt(value)

# 14. Method signature mismatch in subclass (Mypy error).
# (Expected: Mypy error - Signature of "extract" incompatible with supertype)
class BaseExtractor:
  def extract(self, filepath: str) -> None:
    pass

class PDFExtractor(BaseExtractor):
  # Incompatible override: using **kwargs instead of explicit signature.
  def extract(self, **kwargs) -> None:
    pass

# fmt: on
