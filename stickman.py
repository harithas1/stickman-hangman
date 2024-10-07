name=input("👉 Enter your name: ")
print(f"\n👋 Hello, {name.upper()}!🤩 Welcome to the Stickman Hangman game!")
print("\n🧨 Get ready to have some fun guessing words and saving Stickman.")
print("Let's start!💃")
print("\n---------------------------------------------------------------------------\n")

sports=["football","soccer","basketball","tennis","hockey","volleyball","golf"]
countries=["france","brazil","india","china","australia","egypt","japan"]
animals=["elephant","cheetah","penguin","tiger","gorilla","sloth","dolphin"]
fields=["sports","countries","animals"]
select_a_field=input(f"\n🧨 Please select your preferred field from this list: 👉 {fields}: ").lower()


print("\n---------------------------------------------------------------------------\n")

display_hangman=['''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
 
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']




word="" #Word which user is going to guess #tiger
if select_a_field in fields:
  index=int(input(f"\n🧨 I have 7 words in {select_a_field} category, enter a number"
                  f" between 1 and 7 to select the word you"
                  f" want to guess from {select_a_field} category:👉 ")) #7

  
  if select_a_field=="sports":
    word+=sports[index-1]
  if select_a_field=="countries":
    word+=countries[index-1]
  if select_a_field=="animals":
    word+=animals[index-1]
else:
  print("Invalid field, please select a correct field")
  exit()
  

print("\n---------------------------------------------------------------------------\n")



#CLUES
print(f"\n🧨 Hey, {name}👋 I've included some instructions and a hint below for you to "
      f" guess the word related to {select_a_field} category.")
print("Take a look!👇")
#this will tell user how many letter word they have to guess
if select_a_field=="sports":
  print("\n 1. Your task is to guess the name of the sport.")
if select_a_field=="contries":
  print("\n 1. Your task is to guess the name of the country.")
if select_a_field=="animals":
  print("\n 1. Your task is to guess the name of the animal.")
print(f"\n 2. You need to guess a/an {len(word)}-letter word.")
print("\n 3. You have 5 chances to guess wrong letters.")
print("\n 4. Guess the word by entering a single letter or the whole word.")
print("\n 5. Save your Stickman by guessing correctly; for each wrong answer, one body part will be removed.")
print("\n\n")



#SPORTS
if word=="football":
  print("Hint: Kick ball, goal, FIFA")
if word=="soccer":
  print("Hint: Goalie, field, World Cup, Corner kick, Yellow card ")
if word== "basketball":
  print("Hint: Hoop, dribble, NBA, rebound, dunk")
if word=="tennis":
  print("Hint: Racket, Wimbledon, serve, Grand Slam")
if word=="hockey":
  print("Hint: Puck, stick, goal, penalty")
if word=="volleyball":
  print("Hint: Net, spike, beach, bump")
if word=="golf":
  print("Hint: Club, tee, hole, ball, swing, green")


#hints for COUNTRIES

if word=="france":
  print("Hint: Eiffel Tower, baguette, Paris")
if word=="brazil":
  print("Hint: Carnival, Amazon Rainforest, Brasilia")
if word=="india":
  print("Hint: Land of Bengal tiger, Varanasi, Bharatanatyam")
if word=="china":
  print("Hint: Great Wall, pandas, Beijing")
if word=="australia":
  print("Hint: Kangaroo, Sydney Opera House")
if word=="egypt":
  print("Hint: Pyramids, Nile River")
if word=="japan":
  print("Hint: Sushi, Mount Fuji, Tokyo, cherry blossoms, samurai")


#hints for ANIMALS
if word=="elephant":
  print("Hint: Big ears, trunk, tusks")
if word=="cheetah":
  print("Hint: Fastest land animal, spots, Africa")
if word=="penguin":
  print("Hint: Waddling, black and white, Antarctica")
if word=="tiger":
  print("Hint: Stripes, big cat, roar")
if word=="gorilla":
  print("Hint: Largest primate, black fur, knuckle-walker")
if word=="sloth":
  print("Hint: Slow-moving, tree-dwelling, South America")
if word=="dolphin":
  print("Hint: Intelligent, playful, aquatic mammal")




print("\n")




# guessed_letters=[]
tries=5
print(display_hangman[tries-1],end=" "*len(word)+"_ "*len(word))

print("\n\n\n---------------------------------------------------------------------------\n")


guessed_letters=[]
while tries>0:
  guess=input("\n\n🧨Guess a letter or the whole word: ").lower()
  if len(guess)==1:
    if guess in guessed_letters:
      print("\n👉 You are already guessed that letter!")
    elif guess not in word:
      tries=tries-1
  
      if tries==0:
        print('''
                  +---+
                  |   |
                  O   |
                      |
                      |
                      |
                =========''',end=" "*len(word)+word)
        print(f"\n\n👎👎 Sorry, {name.upper()}😞. you have run out of chances!"
              f" The correct word is: ",word.upper())
        print("\n\n")
        break
        
      print(f"\n❌ Sorry {name.upper()}, your guess is wrong. You have only {tries} chances left.")  
    elif guess in word:
      guessed_letters.append(guess)
      print(f"\n🧨 ✅ Good guess, {name.upper()}!👏")
  else:#if guessed whole word
    if guess==word:
      print(f"\n\n🏆🏆🏆 Congratulations, {name.upper()}! 🥳🎉🎊 You guessed the word - '{word.upper()}' correctly\n")
      print("\n\n")
      break
    else:
      tries=tries-1
      print(f"\n❌ Sorry, {name.upper()}. Your guess is wrong!, you have only {tries} chances left!\n")

  #to display guessed letters
  display_word=""
  for letter in word:
    if letter in guessed_letters:
      display_word=display_word+letter+" "
    else:
      display_word=display_word+"_ "
  print(display_hangman[tries-1], end=" "*len(word)+display_word)
  
  
  print("\n\n---------------------------------------------------------------------------")
  
  if tries==0:
    print(f"👎👎 Sorry, {name.upper()}😞. you have run out of chances! The correct word is: ",word)
  
      
      
  

























