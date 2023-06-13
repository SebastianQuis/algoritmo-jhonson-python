def algoritmo_jhonson(tareas):
    n = len(tareas)
    tareas_ordenadas = sorted(tareas, key=lambda x: min(x[0], x[1]))
    cronograma = []
    
    while tareas_ordenadas:
        if tareas_ordenadas[0][0] < tareas_ordenadas[0][1]:
            cronograma.append(tareas_ordenadas.pop(0))
        else:
            cronograma.append(tareas_ordenadas.pop())
    
    return cronograma

# Ejemplo de uso
tasks = [(2, 1, 5), (3, 2, 6), (1, 4, 2), (4, 3, 5)]
optimal_schedule = algoritmo_jhonson(tasks)
# print().cle;
print("Orden óptimo de ejecución de las tareas:")

print("Tarea crítica\n",optimal_schedule[0])
print();
print("Tarea óptima\n",optimal_schedule[3])
print();


print("Lista de rutas - etapa de clasificación")
for task in optimal_schedule:
    print(task, end="\n")