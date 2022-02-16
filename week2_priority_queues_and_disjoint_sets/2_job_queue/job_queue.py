# python3
import heapq


n_workers, n_jobs = map(int, input().split())
jobs = list(map(int, input().split()))
assert len(jobs) == n_jobs

q = []
for i in range(n_workers):
    heapq.heappush(q, (0, i)) # Inicializa el heap para la cantidad de threads existentes

for i in range(n_jobs):
    x, y = heapq.heappop(q) # Elimina el trabajo que tiene tiempo mínimo, guarda en x el tiempo, en y el thread
    print(y,x)
    heapq.heappush(q, (x+jobs[i], y)) # Añade al heap el tiempo que se tarda en el siguiente trabajo y el thread