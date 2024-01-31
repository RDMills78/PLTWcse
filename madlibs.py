#madlibs project - create a series of inputs to place in a printed story.

print("Welcome to the Mills Madlibs!")

#Prompts for the story
properNoun = input("Enter a proper noun: ")
place = input("Enter a place: ")
landmark = input("Enter a landmark in the place: ")
adverb = input("Enter an adverb: ")
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adjective = input("Enter another adjective: ")

#Create a story
story ="There once was a weasel named " + properNoun + " he lived in a place called "  + place + ". " + properNoun + \
       " loved to visit " + landmark + " when he was sad. It always made him feel " + adjective + " and soon spirits " \
                                                                                                  "began to rised." +\
       properNoun + " ..."

print(story)