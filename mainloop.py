import scoring_functions as sf
from bowler_profiles import bowler_profiles as bp



# Main program loop goes here.

print("Would you like to see your predicited scores?")
first_name = str.lower(input("What is your first name? "))
last_name = str.lower(input("What is your last name? "))
profile = first_name[0] + "_" + last_name


try:
    while bp[profile]:
        print("Bowler found. What would you like to do?")
        print("Roll a (s)eries?")
        print("Roll a (g)ame?")
        choice = input("(Q)uit? ")
        if choice.lower() == 's':
            num_of_games = int(input("How many games would you like to run? "))
            for i in range(num_of_games):
                game = sf.BowlingScores(bp[profile]).get_games()
                print(game)
                score = sf.Score(game)
                print(score.get_score())
        elif choice.lower() == 'g':
            game = sf.BowlingScores(bp[profile]).get_games()
            print(game)
            score = sf.Score(game)
            print(score.get_score())
        elif choice.lower() == 'q':
            break
        else:
            print("Invalid selection, try again please")
except KeyError:
    print("Bowler not found")
