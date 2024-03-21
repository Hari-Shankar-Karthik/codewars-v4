from engine.main import Game
import scriptblue
import scriptred
import trial_script

if __name__ == "__main__":
    G = Game((40, 40), trial_script, scriptblue)
    G.run_game()