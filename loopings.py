
print("==================================================")

people = ['Lebron','Aaliyah','Diamond','Dominique','Aliyah','Jazmin','Darnell','Hatfield','Hawkins','Hayden','Hayes','Haynes','Hays','Head','Heath','Hebert','Henderson','Hendricks','Hendrix','Henry','Hensley','Henson','Herman','Hernandez','Herrera','Herring','Hess','Hester','Hewitt','Hickman','Hicks','Higgins','Hill','Hines','Hinton','Hobbs','Hodge','Hodges','Hoffman','Hogan','Holcomb','Holden','Holder','Holland','Holloway','Holman','Holmes','Holt','Hood','Hooper','Hoover','Hopkins','Hopper','Horn','Horne','Horton','House','Houston','Howard','Howe','Howell','Hubbard','Huber','Hudson','Huff','Wally','Hughes','Hull','Humphrey','Hunt','Hunter','Hurley','Hurst','Hutchinson','Hyde','Ingram','Irwin','Jackson','Jacobs','Jacobson','James','Jarvis','Jefferson','Jenkins','Jennings','Jensen','Jimenez','Johns','Johnson','Johnston','Jones','Jordan','Joseph','Joyce','Joyner','Juarez','Justice','Kane','Kaufman','Keith','Keller','Kelley','Kelly','Kemp','Kennedy','Kent','Kerr','Key','Kidd','Kim','King','Kinney','Kirby','Kirk','Kirkland','Klein','Kline','Knapp','Knight','Knowles','Knox','Koch','Kramer','Lamb','Lambert','Lancaster','Landry','Lane','Lang','Langley','Lara','Larsen','Larson','Lawrence','Lawson','Le','Leach','Leblanc','Lee','Leon','Leonard','Lester','Levine','Levy','Lewis','Lindsay','Lindsey','Little','Livingston','Lloyd','Logan','Long','Lopez','Lott','Love','Lowe','Lowery','Lucas','Luna','Lynch','Lynn','Lyons','Macdonald','Macias','Mack','Madden','Maddox','Maldonado','Malone','Mann','Manning','Marks','Marquez','Marsh','Marshall','Martin','Martinez','Mason','Massey','Mathews','Mathis','Matthews','Maxwell','May','Mayer','Maynard','Mayo','Mays','Mcbride','Mccall','Mccarthy','Mccarty','Mcclain','Mcclure','Mcconnell','Mccormick','Mccoy','Mccray','Wally','Mcdaniel','Mcdonald','Mcdowell','Mcfadden','Mcfarland','Mcgee','Mcgowan','Mcguire','Mcintosh','Mcintyre','Mckay','Mckee','Mckenzie','Mckinney','Mcknight','Mclaughlin','Mclean','Mcleod','Mcmahon','Mcmillan','Mcneil','Mcpherson','Meadows','Medina','Mejia','Melendez','Melton','Mendez','Mendoza','Mercado','Mercer','Merrill','Merritt','Meyer','Meyers','Michael','Middleton','Miles','Miller','Mills','Miranda','Mitchell','Molina','Monroe','Lucas','Jake','Scott','Amy','Molly','Hannah','Lucas']

# Your code here
i = 0
for n in people:
    if n == "Wally":
        print(i)
    i += 1

print("==================================================")

sample_list = [45, 67, 87, 23, 5, 32, 60]

# Your code below
new_list = []

for i in range(len(sample_list) -1, -1, -1):
    new_list.append(sample_list[i])

print(f"initial list: {sample_list}")
print(f"final list: {new_list}")

print("==================================================")

my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

# Your code here
new_list = []
for i in my_list:
    if type(i) == dict or type(i) == list:
        new_list.append(i)


print(new_list)

print("==================================================")

my_list = [4,5,734,43,45,100,4,56,23,67,23,58,45]


# Your code here
def sum_odds(num):
    total = 0
    for i in num:
        if i % 2 != 0:
            total += i
    
    return total

print(sum_odds(my_list))

print("==================================================")

people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    new_people = [p for p in people if p != person_name]
    return new_people
    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))

"""

Comprensión de Listas (List Comprehension)
Sintaxis

new_list = [expression for item in iterable if condition]

    - expression: La expresión que se evalúa y se agrega a la nueva lista.
    - item: El elemento actual del iterable que se está iterando.
    - iterable: La colección (lista, tupla, etc.) sobre la que se está iterando.
    - condition: (opcional) Una condición que filtra los elementos del iterable. Solo los elementos que satisfacen esta condición se incluirán en la nueva lista.

        new_people = [person for person in people if person != person_name]

    person for person in people:
        for person in people: Este es el bucle que itera sobre cada elemento en la lista people.
        person: Este es el elemento actual del bucle que se añadirá a la nueva lista.

    if person != person_name:
        Esta es la condición que filtra los elementos. Solo los elementos person que no sean iguales a person_name se incluirán en la nueva lista new_people.

Método: filter_even_numbers

def filter_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return even_numbers


my_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_even_numbers(my_numbers)
print(result)  # Salida: [2, 4, 6, 8, 10]

Explicación del Ejemplo

    Método filter_even_numbers:
        def filter_even_numbers(numbers):: Define una función llamada filter_even_numbers que toma un argumento numbers, que es una lista de números.

    Comprensión de Listas:
        even_numbers = [num for num in numbers if num % 2 == 0]:
            for num in numbers: Itera sobre cada número en la lista numbers.
            num: Representa el número actual en la iteración.
            if num % 2 == 0: Filtra solo los números que son pares (el residuo de dividir por 2 es 0).
            [num for num in numbers if num % 2 == 0]: Crea una nueva lista even_numbers que contiene solo los números pares de numbers.

    Retornar la Nueva Lista:
        return even_numbers: Retorna la lista de números pares.

"""


print("==================================================")

my_list = [43,23,6,87,43,1,4,6,3,67,8,3445,3,7,5435,63,346,3,456,734,6,34]

# Your code here
def max_integer(int_list):
    max = int_list[0]

    for i in int_list:
        if i > max:
            max = i
    return max

print(max_integer(my_list))


print("==================================================")



print("==================================================")



print("==================================================")
