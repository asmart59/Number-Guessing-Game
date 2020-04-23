from UsersGuessLevel import GameLevel
game_level = GameLevel()
while True:
    select_level = input("""Select a level: Type 1 to select easy,
    Type 2 to select medium,
    Type 3 to select hard: 
    """)
    if select_level in ("1", "2", "3"):
        break
    print("Sorry, I don't understand")
if select_level == "1":
    game_level.game_level_is_easy()
elif select_level == "2":
    game_level.game_level_is_medium()
elif select_level == "3":
    game_level.game_level_is_hard()
