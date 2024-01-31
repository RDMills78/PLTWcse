#count down code
def count_down ():
    global number
    for number in range(10, -1, -1):
        print(number)
    return 'Blast Off!'
print(count_down())

#what is your name
name = input('What is your name? ')
print (name)

#what is your name with concatination
#what is your name
name = input('What is your name? ')
print ('Nice to meet you ' + name)

# Name Length
def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

"""Describe this function...
"""
def Name_Length():
  global Name
  Name = text_prompt('What is your name?')
  print(''.join([str(x) for x in ['Hello ', Name, ' Your Name has ', len(Name), ' letters in it']]))


Name_Length()

