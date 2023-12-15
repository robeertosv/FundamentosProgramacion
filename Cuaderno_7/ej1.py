fechas = ['13/12/2005', '14/01/2005', '15/01/2022', '14/06/2004', '26/05/2007', '13/10/2006', '10/03/2023']


def sortByYear(dates: list) -> list:
    fechas = []

    for fecha in dates:
        t = fecha.split('/')
        fechas.append(t)

    n = len(fechas)-1

    for i in range(n):
        for j in range(n-i):
            if fechas[j+1][2] < fechas[j][2]:
                fechas[j+1], fechas[j] = fechas[j], fechas[j+1]
            elif fechas[j+1][2] == fechas[j][2]:
                if fechas[j+1][1] < fechas[j][1]:
                    fechas[j+1], fechas[j] = fechas[j], fechas[j+1]
                elif fechas[j+1][1] == fechas[j][1]:
                    if fechas[j+1][0] < fechas[j][0]:
                        fechas[j+1], fechas[j] = fechas[j], fechas[j+1]

    return fechas