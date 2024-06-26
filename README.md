# code-wars-v4
Hi everyone! This is where we'll be storing all our code on this project. Some basic guidelines:
- Always pull into your local machine before you start to work, so that you are working on the latest version of the code.
- Make sure your commit messages are descriptive, such as ADDED: `xyz` function in `my_script,py`
- Most importantly, ALWAYS create a new branch when you're adding something new, because if it is buggy it could break everything.
- Ensure you test thoroughly before pushing onto GitHub. Never push buggy code.

## Pirate Signal Composition: *Add more as required*
**NOTE: All items are ciphered and take up only 1 character space unless mentioned otherwise.**
- pirate_id (0)
- pirateX (1)
- pirateY (2)
- targetX (3)
- targetY (4)
- was_last_move_1: Required for explore_quadrant.py (5)
- is_home_explored: Required for explore_quadrant.py (6)
- quadrant_exploring: Required for explore_quadrant.py (7)
- is_exploring_X: Required for explore_quadrant.py (8)
- is_monk: monk of island1 (9)
          monk of island2 (10)
          monk of island3 (11)
- in_useless_island: Required for rebounding. (Added by Hari) (12)
- is_guard: if that pirate is a guard or not(13)
- has_infiltrated: stores whether that pirate has reached the enemy spawn (for infiltrate.py) (14)
- Rebound : Two indices for two separate quadrants (15, 16)
- attacking_monk : is attacking monk or not (17) for island 1 , (18)  for 2 , (19) for 3
## Team Signal Composition: *Add more as required*
**NOTE: All items are ciphered and take up only 1 character space unless mentioned otherwise.**
- island1X, island1Y, island2X, island2Y, island3X, island3Y (first 6 characters)
- Time frames stored in next 3 characters (required for gradual_defense)
- Total number of pirates alive
- Storing 10 closes pirate IDs to every island (30 characters in total)
-  presence of monk: island1 (40), island2 (41), island3 (42)
-  guards: is_there_a_need_to_guard(island2) (43)
-  guard_ID's: ID's of the pirates that will become a guard and it's location (44-68) excluding 68.
   format each location will have two pirate ID's corresponding to that location. (location,pirate1ID,pirate2ID)
   what is location here: each tile in the boundary of the island will have a number from 1-8 and that describes the location.
-  counter for L-shaped defence while capturing - (69)
-  pirade ids of 5 pirates -- (70-75), excluding 75
-  defending monk count- island1 -  75, island2 - 76 , island3 - 77
