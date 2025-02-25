class Student:
    """
    Estructura para almacenar los datos de un estudiante.
    
    Atributos:
        name (str): Nombre del estudiante.
        enrollment (str): Matrícula del estudiante.
        grade (float): Calificación del estudiante.
    """
    def __init__(self, name, enrollment, grade):
        self.name = name
        self.enrollment = enrollment
        self.grade = grade

def top_student(students):
    """
    Función que encuentra al estudiante con la calificación más alta.

    Argumentos:
        students (list): Arreglo de objetos Student.

    Devuelve:
        str: Nombre del estudiante con la calificación más alta.
    """
    if not students:
        return "No hay estudiantes en la lista."
    
    best = students[0]  # Se asume que el primer estudiante tiene la mejor calificación
    for student in students[1:]:
        if student.grade > best.grade:
            best = student
    
    return f"El estudiante con la calificación más alta es {best.name} con {best.grade}."

def main():
    # Definición de un arreglo de estudiantes
    student_list = [
        Student("Ana Pérez", "A123", 95.5),
        Student("Luis Gómez", "B456", 88.0),
        Student("María López", "C789", 99.0),
        Student("Carlos Díaz", "D101", 91.5)
    ]

    # Se obtiene y muestra el estudiante con la mejor calificación
    result = top_student(student_list)
    print(result)

if __name__ == "__main__":
    main()