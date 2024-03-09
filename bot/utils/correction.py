# RE allows us to use regular expressions within this program
import re
from bot.utils.constants import CONST


# This function takes in a string and returns a bool
# representing whether it needs corrected or not
def needs_correction(input):
  return bool(re.search(CONST.CORRECTION_REGEX, input))
