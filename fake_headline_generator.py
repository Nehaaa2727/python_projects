#1- import the random module
import random

#2- create subjects
subjects = [
    "Sharukh khan",
    "Virat Kohli",
    "Nirmala sitharaman",
    "A mumbai cat",
    "A group of monkeys",
    "Prime minister Modi",
    "A cute puppy",
    "A girl from paris"
    
]

actions = [
      "launches",
      "cancels",
      "dance with",
      "eats",
      "declares war on",
      "orders",
      "celebrates"
]

places_or_things = [
    "at Red Fort",
    "in Mumbai local train",
    "a plate of momos",
    "inside parliament",
    "at Ganga Ghat",
    "during IPL match",
    "at India gate"
]

#3- start the headline generation loop
while True:
    subjects_choice = random.choice(subjects)
    actions_choice = random.choice(actions)
    places_or_things_choice = random.choice(places_or_things)

    headline = f"BREAKING NEWS: {subjects_choice} {actions_choice} {places_or_things_choice}"
    print("\n" + headline)

    user_input = input("\n do you want another headline? (yes/no)").strip().lower()
    if user_input == "no":
        break

# print goodbye msg
print("\n thanks for using the fake news headline generator. Have a funn dayy !")   