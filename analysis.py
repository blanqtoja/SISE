import os
import subprocess

#sprawdzenie i utworzenie folderu puzzle_solved oraz puzzle
if not os.path.exists("puzzle_solved"):
    os.makedirs("puzzle_solved")
if not os.path.exists("puzzle"):
    os.makedirs("puzzle")

#main.py bfs RDUL 4x4_01_0001.txt 4x4_01_0001_bfs_rdul_sol.txt 4x4_01_0001_bfs_rdul_stats.txt
#podbranie sciezek plikow z folderu puzzle
puzzleFiles = os.listdir("puzzle")

#permutacje kierunkow ruchu dla bfs i dfs (UDRL)
permutations = ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]

print("bfs start")
#dla kazdej permutacji i kazdego pliku z puzzleFiles uruchamiamy algorytm bfs
for perm in permutations:
    for puzzle in puzzleFiles:
        result = subprocess.run(["python", "main.py", "bfs", perm, f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_bfs_{perm}_sol.txt", f"puzzle_solved/{puzzle}_bfs_{perm.lower()}_stats.txt"], capture_output=True, text=True)
        # print("Standard Output:", result.stdout)
        # print("Standard Error:", result.stderr)

print("dfs start")
#dla kazdej permutacji i kazdego pliku z puzzleFiles uruchamiamy algorytm dfs
for perm in permutations:
    for puzzle in puzzleFiles:
        result = subprocess.run(["python", "main.py", "dfs", perm, f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_dfs_{perm}_sol.txt", f"puzzle_solved/{puzzle}_dfs_{perm.lower()}_stats.txt"], capture_output=True, text=True)
        # print("Standard Output:", result.stdout)
        # print("Standard Error:", result.stderr)
    print(perm)

print("a* hamm start")
#dla strategii a* i kazdego pliku z puzzleFiles uruchamiamy algorytm a* z heurystyka hamminga
for puzzle in puzzleFiles:
    result = subprocess.run(["python", "main.py", "astar", "hamm", f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_astar_hamm_sol.txt", f"puzzle_solved/{puzzle}_astar_hamm_stats.txt"], capture_output=True, text=True)
    # print("Standard Output:", result.stdout)
    # print("Standard Error:", result.stderr)

print("a* manh start")
#dla strategii a* i kazdego pliku z puzzleFiles uruchamiamy algorytm a* z heurystyka manhatan
for puzzle in puzzleFiles:
    result = subprocess.run(["python", "main.py", "astar", "manh", f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_astar_manh_sol.txt", f"puzzle_solved/{puzzle}_astar_manh_stats.txt"], capture_output=True, text=True)
    # print("Standard Output:", result.stdout)
    # print("Standard Error:", result.stderr)

print("all done")