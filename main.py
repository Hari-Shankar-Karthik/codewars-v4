from engine.main import Game
import scriptblue, scriptred, final_script, gradual_defense, trial_script

if __name__ == "__main__":
    G = Game((64, 64), scriptblue, trial_script)
    G.run_game()