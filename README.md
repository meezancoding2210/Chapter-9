1. Files in Python (Why We Need Them)

In Python, variables (like `score = 0`) only live temporarily in your computer's short-term memory (RAM) while the program is running. The moment you close the program, that memory is wiped clean. 

**Files** solve this by giving your program a way to save data permanently on your computer's hard drive. 

* **The Code File (`.py`):** Acts like an instruction manual or blueprint (the fixed rules of how the program runs).
* **The Data File (`.txt`, `.json`, etc.):** Acts like a game save file or scratchpad, keeping track of changing data (like high scores, user settings, or logs) so it stays there the next time you open the program.

2. By default, whenever we open a file, it opens in read. But we have to put "w" in order to write.

3. .readlines() reads all the lines at once, however .readline() reads only one line, using it again would print the next line.

4. "a" Can be used to append a line in the .txt file. 

5. when we exit the with statement, the file closes itself.