"""Exercise 6: Jeopardy Mansion."""

__author__ = "730249754"

points: int 

player: str = ""

PURE_PROFIT: int = 200_000
MONEY_EMOJI: str = "\U0001F4B0"
DOOR_EMOJI: str = "\U0001F6AA"
HOST_EMOJI: str = "\U0001F935"
WHITE_BOX: str = "\U00002B1C"
MAN_EMOJI: str ="\U0001F9CD"

from random import randint

stored_questions: list[str] = ["Category: Computer Stuff. \nQuestion: A class in school, or a record of where you've gone in a web browser? ", "Category: Celebrity Sister Surnames. \nQuestion: Britney and Jamie Lynn __? ", "Category: Lets Dance. \nQuestion: It's said that it 'takes two to' do this dance from Buenos Aires? ", "Category: Hunger Aims. \nQuestion: To make a quesadilla, you just need cheese and a ____ to wrap around it? ", "Category: 'V' is for... \nQuesstion: This most popular ice cream flavor? ", "Category: One-word Shout Outs. \nQuestion: What word signifies a freshly cut tree about to fall? ", "Category: In case you're thirsty. \nQuestion: The logo of this sports drink is a capital 'G' with an orange lightening bolt in it ", "Category: Just deserts. \nQuestion: Which desert in North Africa is the largest in the world? ", "Category: Getting Dressed. \nQuestion: What is the name of the slip-on shoes that is also a term for alligator relatives? ", "Category: Outdoors. \nQuestion: A fire ___ is a sidewalk fixture that allows firefighters to tap into the municipal water supply? "]
stored_answers: list[str] = ["History", "Spears", "Tango", "Tortilla", "Vanilla", "Timber", "Gatorade", "Sahara", "Crocs", "Hrydrant"]
jeop_index: int = randint(0, len(stored_questions) - 1)


def main() -> None:
    """Entry point to jeopardy mansion game."""
    global points
    points = 0
    greet()
    # create function for double jeopardy door and triple jeopardy door, and emergency exit door
    #create a while loop decrementing down each floor
    total_floors: int = 5
    floor: int = 5
    while floor <= total_floors and floor > 0:
        print(f"{MONEY_EMOJI}=============== Floor {floor} ==============={MONEY_EMOJI}")
        print(f"Current bank balance: ${points}\n")
        chosen_door: int = int(input(f"Alright {player}, which of the following doors do you choose:\n1. {DOOR_EMOJI} The Pure Profit Door\n2. {DOOR_EMOJI} The Double Jeopardy Door\n3. {DOOR_EMOJI} The Triple Jeopardy Door\n4. {DOOR_EMOJI} The Emergency Exit Door\n(1, 2, 3, or 4): "))
        if chosen_door == 1:
            points += PURE_PROFIT
            print(f"{HOST_EMOJI}: Playing safe is playing smart! ${PURE_PROFIT} has been deposited to your bank!")
        elif chosen_door == 2:
            # call double_jep function
            double_jeop()
        elif chosen_door == 3:
            # call triple_jeop function passing points as a parameter
            points = triple_jeop(points)
        elif chosen_door == 4:
            # quit game
            print(f"{HOST_EMOJI}: Sorry to see you leave earlier than expected, {player}. \nLooks like you will be leaving with ${points} in your bank. Play again sometime!")
            exit()
        print(f"Your bank balance is: ${points}\n \n \n")
        floor -= 1
    print(f"{HOST_EMOJI}: You made it, {player}!! You used your head and gut to complete the Million Dollar challange at my 5-floor Jeopardy Mansion!!")
    if points > 1_000_000: 
        print(f"{HOST_EMOJI}: You are on your million dollar status, my friend. At a whopping ${points} going home in your bank, you have become a self-made millionaire. Join us again another time to test your luck!")
    elif points < 1_000_000 and points > 0:
        print(f"You may not have become a millionaire, but ${points} can sure you get you a lot of twinkies. Enjoy and come back another time!")
    elif points < 0:
        print(f"Wow this mansion really did a number on you, {player}\nUnfortunately, your bank balance is now ${points}. Please grab a broom and mop.. you work here now!")


def greet() -> None:
    """Greets the player to the game in main procedure."""
    global player
    print(f"{HOST_EMOJI}: Hello and welcome to my Jeopardy Mansion! \n...")
    print(f"      {MAN_EMOJI}     ")
    mansion_build: str = f"{WHITE_BOX}{WHITE_BOX}{WHITE_BOX}{WHITE_BOX}{WHITE_BOX}{WHITE_BOX}{WHITE_BOX}{WHITE_BOX}{WHITE_BOX}\n{WHITE_BOX}_{DOOR_EMOJI}_{DOOR_EMOJI}__{DOOR_EMOJI}_{DOOR_EMOJI}_{WHITE_BOX}"
    floors: int = 5
    i: int = 0
    while i < floors:
        print(mansion_build)
        i += 1
    print(f"{HOST_EMOJI}: As the host of this mansion, I like to host my annual Million Dollar challenge. \n... ")
    print(f"{HOST_EMOJI}: Your challenge here is to begin on the roof of Jeopardy Mansion and make your way down. \n... \n{HOST_EMOJI}: Each floor that you descend has 4 doors that can either make or break your bank: \n - {DOOR_EMOJI} The Pure Profit door:\n   \nopening it guarantees a $200,000 deposit into your bank!\n \n - {DOOR_EMOJI} The Double Jeopardy Door door:\n \nbehind this door lies a question worth Double (2x) the amount of money you'd like to wager. Correct answers deposit the doubled amount into your bank, wrong answers deduct it. \n \n - {DOOR_EMOJI} The Triple Jeopardy door:\n \nbehind this door lies a question worth Triple (3x) the amount of money you'd like to wager. Correct answers deposit the tripled amount into your bank, wrong answers deduct it. \n \n - {DOOR_EMOJI} The Emergency Exit Door:\n \nhas your bank had enough? easily parachute out of this door to end the game with your current bank balance! \n... ")
    print(f"{HOST_EMOJI}: The goal is to exit the Jeopardy mansion a millionaire, but any profit is profit. \n... ")
    player = input("Say, what is your million dollar name? ")
    print(f"{HOST_EMOJI}: Alright then {player}, lets see if you can make a milli. Good luck!")


def double_jeop()-> None:
    """Provides player with Jeopardy question 2x worth wager of their choice."""
    global points
    print(f"\n{HOST_EMOJI}: Awesome {player}, you have chosen the Double Jeopardy Door! Playing boldly is always encouraged.")
    money_wagered: int = int(input(f"{HOST_EMOJI}: First, how much money would you like to wager for this Double Jeopardy question? $"))
    double_wager: int = money_wagered * 2
    print(f"\nTotal money to be wagered: ${double_wager}")
    
    double_jeop_question: str = stored_questions[jeop_index]
    double_jeop_answer: str = stored_answers[jeop_index]
    entered_answer: str = input(f"{double_jeop_question}\n[CAPITALIZE THE 1st LETTER ONLY]: ")
    stored_questions.pop(jeop_index)
    stored_answers.pop(jeop_index)
    if entered_answer == double_jeop_answer:
        print(f"\n{HOST_EMOJI}: That is correct! {player} is making their way to riches.")
        points += double_wager
    else: 
        points -= double_wager
        print(f"\n{HOST_EMOJI}: Sorry {player}, that is not correct! ${double_wager} has been deducted from your bank.")


def triple_jeop(game_points: int)-> int:
    """Provides player with Jeopardy question 3x worth wager of their choice."""
    print(f"\n{HOST_EMOJI}: Wow {player}, you are shooting for the stars, lets hope you win!")
    money_wagered: int = int(input("First, how much money would you like to wager for this Triple Jeopardy question? $"))
    triple_wager: int = money_wagered * 3
    print(f"\nTotal money to be wagered: ${triple_wager}")
    triple_jeop_question: str = stored_questions[jeop_index]
    triple_jeop_answer: str = stored_answers[jeop_index]
    entered_answer: str = input(f"{triple_jeop_question}\n[CAPITALIZE THE 1st LETTER ONLY]: ")
    stored_questions.pop(jeop_index)
    stored_answers.pop(jeop_index)
    if entered_answer == triple_jeop_answer: 
        print(f"\n{HOST_EMOJI}: That is correct! {player} has a priceless intuition.")
        game_points += triple_wager
    else: 
        game_points -= triple_wager
        print(f"\n{HOST_EMOJI}: Sorry {player}, that is not correct! ${triple_wager} has been deducted from your bank.")
    return game_points


if __name__ == "__main__":
  main()