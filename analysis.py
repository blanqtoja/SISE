# import os
# import subprocess

# #sprawdzenie i utworzenie folderu puzzle_solved oraz puzzle
# if not os.path.exists("puzzle_solved"):
#     os.makedirs("puzzle_solved")
# if not os.path.exists("puzzle"):
#     os.makedirs("puzzle")

# #main.py bfs RDUL 4x4_01_0001.txt 4x4_01_0001_bfs_rdul_sol.txt 4x4_01_0001_bfs_rdul_stats.txt
# #podbranie sciezek plikow z folderu puzzle
# puzzleFiles = os.listdir("puzzle")

# #permutacje kierunkow ruchu dla bfs i dfs (UDRL)
# permutations = ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]

# print("bfs start")
# #dla kazdej permutacji i kazdego pliku z puzzleFiles uruchamiamy algorytm bfs
# for perm in permutations:
#     for puzzle in puzzleFiles:
#         result = subprocess.run(["python", "main.py", "bfs", perm, f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_bfs_{perm.lower()}_sol.txt", f"puzzle_solved/{puzzle}_bfs_{perm.lower()}_stats.txt"], capture_output=True, text=True)
#         # print("Standard Output:", result.stdout)
#         # print("Standard Error:", result.stderr)

# print("dfs start")
# #dla kazdej permutacji i kazdego pliku z puzzleFiles uruchamiamy algorytm dfs
# for perm in permutations:
#     for puzzle in puzzleFiles:
#         result = subprocess.run(["python", "main.py", "dfs", perm, f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_dfs_{perm.lower()}_sol.txt", f"puzzle_solved/{puzzle}_dfs_{perm.lower()}_stats.txt"], capture_output=True, text=True)
#         # print("Standard Output:", result.stdout)
#         # print("Standard Error:", result.stderr)
#     # print(perm)

# print("a* hamm start")
# #dla strategii a* i kazdego pliku z puzzleFiles uruchamiamy algorytm a* z heurystyka hamminga
# for puzzle in puzzleFiles:
#     result = subprocess.run(["python", "main.py", "astr", "hamm", f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_astar_hamm_sol.txt", f"puzzle_solved/{puzzle}_astar_hamm_stats.txt"], capture_output=True, text=True)
#     # print("Standard Output:", result.stdout)
#     # print("Standard Error:", result.stderr)

# print("a* manh start")
# #dla strategii a* i kazdego pliku z puzzleFiles uruchamiamy algorytm a* z heurystyka manhatan
# for puzzle in puzzleFiles:
#     result = subprocess.run(["python", "main.py", "astr", "manh", f"puzzle/{puzzle}", f"puzzle_solved/{puzzle}_astar_manh_sol.txt", f"puzzle_solved/{puzzle}_astar_manh_stats.txt"], capture_output=True, text=True)
#     # print("Standard Output:", result.stdout)
#     # print("Standard Error:", result.stderr)

# print("all done")
# # subprocess.run(["python", "main.py", "dfs", "DRUL", f"data.txt", f"puzzle_solved/data_sol.txt", f"puzzle_solved/data_stats.txt"], capture_output=True, text=True)
import os
import multiprocessing
import subprocess

def ensure_dirs():
    os.makedirs("puzzle_solved", exist_ok=True)
    os.makedirs("puzzle", exist_ok=True)

def run_solver(args):
#     print(f"Running command: {' '.join(args)}")
    result = subprocess.run(args, capture_output=True, text=True)
#     print(f"Output:\n{result.stdout}")
#     print(f"Error:\n{result.stderr}")

def main():

    # subprocess.run(["python", "main.py", "dfs", "DRUL", f"data.txt", f"puzzle_solved/data_sol.txt", f"puzzle_solved/data_stats.txt"], capture_output=True, text=True)
    ensure_dirs()
    puzzle_files = os.listdir("puzzle")
    permutations = ["RDUL", "RDLU", "DRUL", "DRLU", "LUDR", "LURD", "ULDR", "ULRD"]
    
    tasks = []
    
    print("bfs start")
    for perm in permutations:
        for puzzle in puzzle_files:
            tasks.append(["python", "main.py", "bfs", perm, f"puzzle/{puzzle}", 
                          f"puzzle_solved/{puzzle}_bfs_{perm.lower()}_sol.txt", 
                          f"puzzle_solved/{puzzle}_bfs_{perm.lower()}_stats.txt"])
    
    print("dfs start")
    for perm in permutations:
        for puzzle in puzzle_files:
            tasks.append(["python", "main.py", "dfs", perm, f"puzzle/{puzzle}", 
                          f"puzzle_solved/{puzzle}_dfs_{perm.lower()}_sol.txt", 
                          f"puzzle_solved/{puzzle}_dfs_{perm.lower()}_stats.txt"])
    
    print("a* hamm start")
    for puzzle in puzzle_files:
        tasks.append(["python", "main.py", "astr", "hamm", f"puzzle/{puzzle}", 
                      f"puzzle_solved/{puzzle}_astar_hamm_sol.txt", 
                      f"puzzle_solved/{puzzle}_astar_hamm_stats.txt"])
    
    print("a* manh start")
    for puzzle in puzzle_files:
        tasks.append(["python", "main.py", "astr", "manh", f"puzzle/{puzzle}", 
                      f"puzzle_solved/{puzzle}_astar_manh_sol.txt", 
                      f"puzzle_solved/{puzzle}_astar_manh_stats.txt"])
    
    with multiprocessing.Pool(processes=10) as pool:
        pool.map(run_solver, tasks)
    
    print("all done")

if __name__ == "__main__":
    main()
