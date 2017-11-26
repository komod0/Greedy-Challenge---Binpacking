import heapq


def empacar(nombre_de_archivo):
    # Basado en el algoritmo First Fit Decreasing(FFD)
    archivo = open(nombre_de_archivo, 'r')

    cantidad_de_elementos = int(archivo.readline().rstrip())

    # Para la linea en blanco que hay entre la cantidad y los valores en si.
    archivo.readline()

    valores = []
    bins = []

    for i in range(0, cantidad_de_elementos):
        valores.append(float(archivo.readline().rstrip()))

    archivo.close()

    valores.sort(reverse=True)

    for i in range(0, cantidad_de_elementos):
        entro = False
        if len(bins) > 0:
            tope = bins[0]
            if tope + valores[i] <= 1:
                nuevo_paq = heapq.heappop(bins)
                nuevo_paq += valores[i]
                heapq.heappush(bins, nuevo_paq)
                entro = True
        if not entro:
            heapq.heappush(bins, valores[i])

    print(len(bins))
