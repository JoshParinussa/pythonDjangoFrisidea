def printFiboSeries(number):
    fiboSeries = [0,1]
    for i in range(2, number):
        next_number = fiboSeries[i-1] + fiboSeries[i-2]
        fiboSeries.append(next_number)
    print(fiboSeries)

# Excution
printFiboSeries(10)