from pathlib import Path
import pulp
import re


#    /$$                                                     /$$                               /$$                           /$$          
#   |__/                                                    | $$                              |__/                          | $$          
#    /$$  /$$$$$$   /$$$$$$$  /$$$$$$         /$$$$$$       | $$  /$$$$$$        /$$$$$$/$$$$  /$$  /$$$$$$   /$$$$$$   /$$$$$$$  /$$$$$$ 
#   | $$ /$$__  $$ /$$_____/ /$$__  $$       |____  $$      | $$ |____  $$      | $$_  $$_  $$| $$ /$$__  $$ /$$__  $$ /$$__  $$ |____  $$
#   | $$| $$  \__/|  $$$$$$ | $$$$$$$$        /$$$$$$$      | $$  /$$$$$$$      | $$ \ $$ \ $$| $$| $$$$$$$$| $$  \__/| $$  | $$  /$$$$$$$
#   | $$| $$       \____  $$| $$_____/       /$$__  $$      | $$ /$$__  $$      | $$ | $$ | $$| $$| $$_____/| $$      | $$  | $$ /$$__  $$
#   | $$| $$       /$$$$$$$/|  $$$$$$$      |  $$$$$$$      | $$|  $$$$$$$      | $$ | $$ | $$| $$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$
#   |__/|__/      |_______/  \_______/       \_______/      |__/ \_______/      |__/ |__/ |__/|__/ \_______/|__/       \_______/ \_______/                                                                                                              
                                                                                                                                      

def part1(data):
    total = 0
    for idx, line in enumerate(data, 1): # Con el 1 evitamos el índice 0
        n_lights, light_state, buttons, _ = parse_line(line) # Extraer datos de la línea
        matrix = build_matrix(n_lights, buttons) # Construir la matriz del sistema
        min_presses, _ = minimal_weight_solution(matrix, light_state) # Resolver el sistema
        print(f"\r{int(idx/len(data)*100)}%", end='', flush=True)
        total += min_presses
    return total

def part2(data):
    total = 0
    for idx, line in enumerate(data, 1):
        n_lights, _, buttons, reqs = parse_line(line)
        matrix = build_matrix(n_lights, buttons)
        min_presses = parte2_nose_xd(matrix, reqs)
        print(f"\r{int(idx/len(data)*100)}%", end='', flush=True)
        total += min_presses
    return total

def parse_line(line: str):
    diagram_match = re.search(r'\[([.#]+)\]', line) # Buscar el diagrama entre corchetes
    buttons_matches = re.findall(r'\(([0-9, ]*)\)', line) # Buscar todas las listas de botones entre paréntesis
    req_match = re.search(r'\{([^}]*)\}', line) # Para parte 2: buscar requisitos entre llaves

    diagram = diagram_match.group(1).strip() # Extraer el diagrama
    reqs = [int(x) for x in req_match.group(1).split(",")]
    n_lights = len(diagram)
    light_state = [1 if ch == '#' else 0 for ch in diagram] 
    buttons = []
    for bm in buttons_matches: # Extraer cada lista de botones
        bm = bm.strip()
        if bm == "": 
            buttons.append([])
        else: 
            buttons.append([int(x.strip()) for x in bm.split(',') if x.strip()!=''])
    return n_lights, light_state, buttons, reqs

def build_matrix(n_lights, buttons):
    n_buttons = len(buttons)
    matrix = [[0]*n_buttons for _ in range(n_lights)] # Matriz de ceros
    for j, btn in enumerate(buttons): # Para cada botón
        for i in btn:
            matrix[i][j] ^= 1 # Toggle la luz i al presionar el botón j
    return matrix

def gaussian_elim_gf2(A, b): # A es la matriz de coeficientes, b el vector de términos independientes
    '''Realiza eliminación gaussiana en GF(2) y encuentra solución particular y espacio nulo'''
    '''TOMARSELO CON CALMA QUE ES COMPLICADO LA PUTA MADRE'''
    n = len(A); m = len(A[0]) if n > 0 else 0 # Dimensiones de A 
    M = [row[:] + [bb] for row, bb in zip(A, b)] # Matriz aumentada [A|b]
    row = 0; pivots=[] # Índices de columnas pivote. Los pivotes son las columnas donde hay un 1 líder en cada fila
    for col in range(m): # Para cada columna
        sel = next((r for r in range(row, n) if M[r][col]==1), None) # Buscar fila con 1 en esta columna
        if sel is None: continue
        M[row], M[sel] = M[sel], M[row] # Intercambiar filas
        pivots.append(col) # Registrar columna pivote
        for r in range(n): # Eliminar otros 1s en esta columna
            if r!=row and M[r][col]==1:
                for c in range(col, m+1): M[r][c] ^= M[row][c] # Sumar filas en GF(2) es un XOR
        row += 1
        if row==n: break
    rank = len(pivots) # Rango de la matriz
    for r in range(rank, n): # Comprobar filas inconsistentes
        if all(M[r][c]==0 for c in range(m)) and M[r][m]==1:
            return False, None, None
    x_part = [0]*m
    for r, col in enumerate(pivots): # Construir solución particular. Sí, se llama así porque puede no ser única
        x_part[col] = M[r][m] # Asignar valor de la variable pivote
    free_cols = [c for c in range(m) if c not in pivots]
    nullspace = []
    for fc in free_cols: # Cada columna libre genera un vector del espacio nulo
        vec = [0]*m; vec[fc]=1 # Poner 1 en la posición de la columna libre
        for r, pc in enumerate(pivots): # Completar el resto del vector
            if M[r][fc]==1: vec[pc]=1 # Si la columna libre tiene 1 en la fila del pivote, poner 1 en el pivote
        nullspace.append(vec) # Añadir vector al espacio nulo
    return True, x_part, nullspace

def minimal_weight_solution(A, b): # Encuentra solución de peso mínimo al sistema Ax=b en GF(2)
    ok, x_part, nullspace = gaussian_elim_gf2(A, b) # Resolver el sistema confiando en que siempre hay solución xdxd
    if not nullspace: return sum(x_part), x_part # Si no hay espacio nulo, la solución particular es la única
    k = len(nullspace)
    best_w = None; best_x = None # Pesos y soluciónes mejor encontradas
    for mask in range(1<<k): # Probar todas las combinaciones del espacio nulo
        x = x_part[:]
        for i in range(k):
            if (mask>>i)&1: # Si el i-ésimo bit está activo  
                for j in range(len(x)): x[j] ^= nullspace[i][j] # Sumar en GF(2) es XOR
        w = sum(x)
        if best_w is None or w < best_w:
            best_w, best_x = w, x[:]
    return best_w, best_x # Retornar peso mínimo y solución asociada

def parte2_nose_xd(A, reqs):
    '''MIRA ME CAGO EN DIOS CON LAS MATRICES Y SU PUTA MADRE PA QUE LUEGO HAYA UNA LIBRERÍA QUE TE LO HACE'''
    n = len(A)
    m = len(A[0])
    model = pulp.LpProblem("Joltage", pulp.LpMinimize) # Crear modelo de optimización
    x = [pulp.LpVariable(f"x_{j}", lowBound=0, cat="Integer") for j in range(m)] # Variables de decisión
    model += pulp.lpSum(x) # Función objetivo: minimizar suma de x[j]
    for i in range(n):
        model += ( # Restricciones: suma ponderada igual a reqs[i]
            pulp.lpSum(A[i][j] * x[j] for j in range(m)) == reqs[i] 
        )

    model.solve(pulp.PULP_CBC_CMD(msg=0))

    if pulp.LpStatus[model.status] != "Optimal": 
        return None
    return int(sum(v.value() for v in x))

def load_input(day):
    filename = Path(f"d{day}/input.txt")
    return filename.read_text().strip().splitlines()

if __name__ == "__main__":
    day = 10
    data = load_input(day)
    print("\rPart 1:", part1(data))
    print("\rPart 2:", part2(data))