import tkinter as tk
from tkinter import ttk
import queue
import time

# Predefined mazes
maze1 = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

maze2 = [
    ['#', 'O', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', ' ', '#', ' ', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'X', '#'],
]

maze3 = [
    ['#', 'O', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', '#', '#', ' ', '#', '#', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', ' ', '#', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#', ' ', '#', '#', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#'],
    ['#', ' ', '#', '#', ' ', '#', '#', '#', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', '#', ' ', ' ', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', '#', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#'],
    ['#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', ' ', ' ', '#', '#', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', ' ', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', '#', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', '#', ' ', '#', '#', '#', ' ', ' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', ' ', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', '#', '#', '#', '#', '#', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', '#', '#', ' ', ' ', ' ', '#', ' ', ' ', ' ', '#', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 'X', '#'],
]

class MazeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Maze solver")  # Seteaza titlul ferestrei principale

        # Seteaza labirintul initial
        self.maze = [row[:] for row in maze1]  # Creeaza o copie a labirintului initial
        
        # Calculeaza dimensiunea celulei pe baza dimensiunii labirintului
        self.cell_size = 500 // len(self.maze[0])  # Dimensiunea celulei pe baza latimii labirintului
        if len(self.maze) * self.cell_size > 500:
            self.cell_size = 500 // len(self.maze)  # Ajusteaza dimensiunea daca inaltimea depaseste 500px

        # Creeaza un canvas pentru vizualizarea labirintului
        self.canvas = tk.Canvas(self.root, width=500, height=500)
        self.canvas.pack()

        self.start = "O"  # Simbolul pentru punctul de start
        self.end = "X"    # Simbolul pentru punctul final

        # Creeaza un frame pentru butoanele de selectie a labirintului
        maze_frame = tk.Frame(self.root)
        maze_frame.pack(pady=20, side="top")  

        # Adauga butoane pentru selectarea labirintului
        self.maze1_button = ttk.Button(maze_frame, text="Maze 1", command=lambda: self.change_maze(maze1))
        self.maze1_button.grid(row=0, column=0, padx=10, pady=10)

        self.maze2_button = ttk.Button(maze_frame, text="Maze 2", command=lambda: self.change_maze(maze2))
        self.maze2_button.grid(row=0, column=1, padx=10, pady=10)

        self.maze3_button = ttk.Button(maze_frame, text="Maze 3", command=lambda: self.change_maze(maze3))
        self.maze3_button.grid(row=0, column=2, padx=10, pady=10)

        # Creeaza un frame pentru butoanele algoritmilor
        algo_frame = tk.Frame(self.root)
        algo_frame.pack(pady=20, side="top")

        # Adauga butoane pentru algoritmii BFS si DFS
        self.bfs_button = ttk.Button(algo_frame, text="Run BFS", command=self.run_bfs)
        self.bfs_button.grid(row=0, column=0, padx=15, pady=10)

        self.dfs_button = ttk.Button(algo_frame, text="Run DFS", command=self.run_dfs)
        self.dfs_button.grid(row=0, column=1, padx=15, pady=10)

        # Buton pentru proiectarea labirintului
        self.design_button = ttk.Button(algo_frame, text="Design Maze", command=self.design_maze)
        self.design_button.grid(row=0, column=2, padx=15, pady=10)

        # Creeaza butonul pentru stergerea labirintului
        self.clear_button = ttk.Button(self.root, text="Clear", command=self.clear_canvas)
        self.clear_button.pack(side="right", padx=20, pady=10)

        # Etichete pentru a afișa rezultatele
        self.result_label = tk.Label(self.root, text="Results: ", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.distance_label = tk.Label(self.root, text="Distance: -", font=("Arial", 12))
        self.distance_label.pack(pady=5)

        self.time_label = tk.Label(self.root, text="Execution time: -", font=("Arial", 12))
        self.time_label.pack(pady=5)

        # Deseneaza labirintul initial
        self.draw_maze()

    def change_maze(self, new_maze):
        #Schimbam labirintul curent si redeseneaza-l
        self.maze = [row[:] for row in new_maze]  # Actualizeaza labirintul
        
        # Recalculeaza dimensiunea celulei
        self.cell_size = 500 // len(self.maze[0])
        if len(self.maze) * self.cell_size > 500:
            self.cell_size = 500 // len(self.maze)

        self.clear_canvas()  # Curata canvas-ul
        self.draw_maze()     # Redesenaza labirintul

    def draw_maze(self, path=[]):
        #Deseneaza labirintul pe canvas
        for i, row in enumerate(self.maze):
            for j, value in enumerate(row):
                # Calculeaza coordonatele fiecarui dreptunghi
                x1 = j * self.cell_size
                y1 = i * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size

                # Seteaza culoarea in functie de continutul celulei
                if value == "#":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="black")  # Perete
                elif value == "O":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="green")  # Punct de start
                elif value == "X":
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="red")    # Punct final

                if (i, j) in path:
                    self.canvas.create_rectangle(x1, y1, x2, y2, fill="yellow")  # Drumul gasit

    def find_start(self, maze, start):
        #Caută poziția punctului de start ('O') în labirint.
        for i, row in enumerate(maze):  
            for j, value in enumerate(row): 
                if value == start: 
                    return i, j  
        return None  
    
    def find_neighbors(self, maze, row, col):
        #Găsește vecinii unei celule care sunt accesibili.
        neighbors = []
        if row > 0:  # Vecinul de sus
            neighbors.append((row - 1, col))
        if row + 1 < len(maze):  # Vecinul de jos
            neighbors.append((row + 1, col))
        if col > 0:  # Vecinul din stânga
            neighbors.append((row, col - 1))
        if col + 1 < len(maze[0]):  # Vecinul din dreapta
            neighbors.append((row, col + 1))
        return neighbors  # Returnează lista de vecini accesibili

    def bfs(self):
        #Implementare a algoritmului BFS pentru a găsi drumul în labirint.
        start_pos = self.find_start(self.maze, self.start) 
        q = queue.Queue()  # Creează un coadă pentru a ține pozițiile de explorat
        q.put((start_pos, [start_pos]))  # Adaugă poziția de start și calea inițială (doar punctul de start)

        visited = set()  # Set pentru a ține evidența celulelor vizitate

        while not q.empty():  
            current_pos, path = q.get() 
            row, col = current_pos  

            # Actualizează vizualizarea canvas-ului cu calea curentă
            self.canvas.delete("all")
            self.draw_maze(path)

            self.root.update()

            if self.maze[row][col] == self.end:  # Dacă a ajuns la punctul final ('X') returneaza calea gasita
                return path  

            neighbors = self.find_neighbors(self.maze, row, col)  # Găsește vecinii poziției curente
            for neighbor in neighbors:
                if neighbor in visited:  # Dacă vecinul a fost deja vizitat, îl ignoră
                    continue

                r, c = neighbor  
                if self.maze[r][c] == "#":  # Dacă vecinul este un perete, îl ignoră
                    continue

                new_path = path + [neighbor]  # Creează o nouă cale adăugând vecinul
                q.put((neighbor, new_path))  # Adaugă vecinul și noua cale în coadă
                visited.add(neighbor)  # Marchează vecinul ca vizitat

    def dfs(self):
        #Implementare a algoritmului DFS pentru a găsi drumul în labirint.
        start_pos = self.find_start(self.maze, self.start)  
        stack = [(start_pos, [start_pos])]  # Stivă care conține poziția curentă și calea parcursă

        visited = set()  # Set pentru a ține evidența celulelor vizitate

        while stack:  
            current_pos, path = stack.pop()  # Ia poziția curentă și calea din vârful stivei
            row, col = current_pos 

            # Actualizează vizualizarea canvas-ului cu calea curentă
            self.canvas.delete("all")
            self.draw_maze(path)

            self.root.update()

            if self.maze[row][col] == self.end:  # Dacă a ajuns la punctul final ('X') returneaza calea gasita
                return path  

            if current_pos in visited:  # Dacă poziția curentă a fost deja vizitată, trece peste ea
                continue

            visited.add(current_pos)  # Marchează poziția curentă ca vizitată

            neighbors = self.find_neighbors(self.maze, row, col)  # Găsește vecinii poziției curente
            for neighbor in neighbors:  
                r, c = neighbor  
                if self.maze[r][c] != "#" and neighbor not in visited:  # Dacă vecinul nu e un perete și nu a fost vizitat
                    new_path = path + [neighbor]  # Creează o nouă cale adăugând vecinul
                    stack.append((neighbor, new_path))  # Adaugă vecinul și noua cale în stivă

    def run_bfs(self):
        self.clear_canvas()
        start_time = time.time()  # Începe măsurarea timpului
        path = self.bfs()
        end_time = time.time()  # Sfârșește măsurarea timpului

        if path:
            self.draw_maze(path)
            distance = len(path) - 1  # Distanta este numărul de pași din drum minus 1
            time_taken = end_time - start_time  # Timpul de execuție
            # Actualizează etichetele cu rezultatele
            self.distance_label.config(text=f"Distance: {distance} steps")
            self.time_label.config(text=f"Execution time: {time_taken:.4f} seconds")
        else:
            self.distance_label.config(text="Distance: N/A")
            self.time_label.config(text="Execution time: N/A")

    def run_dfs(self):
        self.clear_canvas()
        start_time = time.time()  # Începe măsurarea timpului
        path = self.dfs()
        end_time = time.time()  # Sfârșește măsurarea timpului

        if path:
            self.draw_maze(path)
            distance = len(path) - 1  # Distanta este numărul de pași din drum minus 1
            time_taken = end_time - start_time  # Timpul de execuție
            # Actualizează etichetele cu rezultatele
            self.distance_label.config(text=f"Distance: {distance} steps")
            self.time_label.config(text=f"Execution time: {time_taken:.4f} seconds")
        else:
            self.distance_label.config(text="Distance: N/A")
            self.time_label.config(text="Execution time: N/A")

    def clear_canvas(self):
        self.canvas.delete("all")
        self.draw_maze()

    def design_maze(self):
        #Permite utilizatorului să creeze și să modifice un labirint personalizat.

        def update_cell(row, col):
            #Schimbă starea celulei din design_grid și actualizează labirintul
            current = design_grid[row][col]["bg"]  # Obține culoarea curentă a celulei
            if current == "white":
                design_grid[row][col]["bg"] = "black"  # Transformă în perete (#)
                self.maze[row][col] = "#"
            elif current == "black":
                design_grid[row][col]["bg"] = "white"  # Transformă în celulă goală ( )
                self.maze[row][col] = " "
            elif current == "green":
                design_grid[row][col]["bg"] = "white"  # Resetează celula de start (O)
                self.maze[row][col] = " "
            elif current == "red":
                design_grid[row][col]["bg"] = "white"  # Resetează celula de final (X)
                self.maze[row][col] = " "

        def get_maze_code():
            #Generează codul Python pentru labirintul curent.
            maze_code = "maze = [\n"
            for row in self.maze:
                maze_code += "    " + str(row) + ",\n"
            maze_code += "]"
            return maze_code

        def show_message():
            """Afișează în consolă codul generat pentru labirint."""
            maze_code = get_maze_code()
            print(f"Copy this Python code to use the maze:\n\n{maze_code}")

        # Creează o fereastră nouă pentru designul labirintului
        design_window = tk.Toplevel(self.root)
        design_window.title("Design Your Maze")

        # Setează dimensiunea ferestrei în funcție de dimensiunea labirintului
        design_window.geometry(f"{len(self.maze[0]) * self.cell_size}x{len(self.maze) * self.cell_size + 50}")

        design_grid = []  # Stochează butoanele care reprezintă grila labirintului

        for i, row in enumerate(self.maze):
            grid_row = []  # Reprezintă un rând din grilă
            for j, cell in enumerate(row):
                # Setează culoarea inițială în funcție de tipul celulei
                color = "white"
                if cell == "#":
                    color = "black"  # Perete
                elif cell == "O":
                    color = "green"  # Start
                elif cell == "X":
                    color = "red"  # Final

                # Creează un buton pentru fiecare celulă din labirint
                btn = tk.Button(design_window, bg=color, width=3, height=1,  # Dimensiuni crescute pentru vizibilitate
                                command=lambda r=i, c=j: update_cell(r, c))  # Legătură pentru actualizarea celulei
                btn.place(x=j * self.cell_size, y=i * self.cell_size, width=self.cell_size, height=self.cell_size)
                grid_row.append(btn)  # Adaugă butonul la rândul curent
            design_grid.append(grid_row)  # Adaugă rândul la grilă

        # Adaugă un buton de salvare sub grila labirintului
        save_button = ttk.Button(design_window, text="Save", command=show_message)
        save_button.place(x=0, y=len(self.maze) * self.cell_size + 10, width=len(self.maze[0]) * self.cell_size)

        # Permite setarea punctului de start și de final
        self.start = "O"
        self.end = "X"

root = tk.Tk()
app = MazeApp(root)
root.mainloop()