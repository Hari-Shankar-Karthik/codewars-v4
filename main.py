from engine.main import Game
import scriptblue, scriptred, final_script, gradual_defense, final_script_doop

if __name__ == "__main__":
    G = Game((40, 40), scriptred, final_script)
    G.run_game()