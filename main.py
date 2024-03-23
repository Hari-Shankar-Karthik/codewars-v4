from engine.main import Game
import scriptblue, scriptred, final_script, gradual_defense

if __name__ == "__main__":
    G = Game((40, 40), scriptblue, final_script)
    G.run_game()