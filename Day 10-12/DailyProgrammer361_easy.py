'''
Challenge #361 [Easy] Tally Program
Description
5 Friends (let's call them a, b, c, d and e) are playing a game and need to keep track of the scores. Each time someone
 scores a point, the letter of his name is typed in lowercase. If someone loses a point, the letter of his name is typed
  in uppercase. Give the resulting score from highest to lowest.
'''

testinput = 'dbbaCEDbdAacCEAadcB'

def solve(rawinput):
    return sorted(((char, rawinput.count(char) - rawinput.count(char.upper())) for char in 'abcde'), key=lambda x:
    x[1])

print(solve(testinput))
