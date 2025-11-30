# TODO Найдите количество книг, которое можно разместить на дискете
information = 1.44
number_of_pages = 100
number_of_lines = 50
number_of_characters = 25
one_character = 4

print("Количество книг, помещающихся на дискету:", int((information*(2**20))//(number_of_pages*number_of_lines*number_of_characters*one_character)))
