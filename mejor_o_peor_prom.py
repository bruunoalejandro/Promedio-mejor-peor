mejorprom = 0.0
peorprom = 11.0
suma = 0.0
peormat = 0
mejormat = 0
cant = int(input("Ingrese cantidad de alumnos que quieres ingresar: "))
if cant > 0:
    for i in range(1, cant+1):
        mat = int(input("Ingrese la matricula del alumno: "))
        nota1 = float(input("Ingrese la primera nota: "))
        nota2 = float(input("Ingrese la segunda nota: "))
        nota3 = float(input("Ingrese la tercera nota: "))
        nota4 = float(input("Ingrese la cuarta nota: "))
        nota5 = float(input("Ingrese la quinta nota: "))
        suma = nota1 + nota2 + nota3 + nota4 + nota5
        prom = suma/5
        print("El promedio del alumno", mat, "es:", prom)
        if prom > mejorprom:
                mejorprom = prom
                mejormat = mat
        elif prom < peorprom:
                peorprom = prom
                peormat = mat
    print("El mejor promedio es:", round(mejorprom, 2),"que corresponde al alumno:", mejormat)
    print("El peor promedio es:", round(peorprom, 2),"que corresponde al alumno:", peormat)
else:
    print("El valor debe ser positivo")