from engine.main import Game
import scriptblue
import scriptred
import trial_script

if __name__ == "__main__":
    G = Game((40, 40), scriptblue, trial_script)
    G.run_game()