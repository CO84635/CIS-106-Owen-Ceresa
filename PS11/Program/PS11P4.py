def calculate_averages(game1, game2, game3, handicap):
    average_score = (game1 + game2 + game3) / 3
    average_score_with_handicap = average_score + handicap
    return average_score_with_handicap, average_score

lastname = str(input("What is your lastname?: "))
game1 = float(input("What is your first game score?: "))
game2 = float(input("What is your second game score?: "))
game3 = float(input("What is your third game sc ore?: "))
handicap = float(input("What is your handicap?: "))
average_score_with_handicap, average_score = calculate_averages(game1, game2, game3, handicap)
print(f"Dear {lastname}, the average score was {average_score} & average score with handicap was {average_score_with_handicap}")
