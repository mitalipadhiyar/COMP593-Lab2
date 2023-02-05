def main():

    my_info ={
        
        'full_name' : 'Mitali Padhiyar',
        'student_id':  10284088,
        'pizza_toppings': [
                'RED ONIONS',
                'BELL PEPPER',
                'BLACK OLIVES'
               
         ],
         'movies' : [
               {
                  'title' : '3 idiots',
                  'genre' : 'comedy'
               },

               {
                   'title' : 'yeh jawanni hai dewaani',
                   'genre' : 'romance'
               },

         ],

    }

    my_info['movies'].append("'title':'jumanji', 'genre':'adventure'")
    print_student_name_id(my_info)
    print(print_pizza_toppings(my_info))
    add_pizza_toppings(my_info, ('pizza sauce', 'oregano', 'chiily flakes'))
    print(print_pizza_toppings(my_info))
    movie_genre = print_movie_genre(my_info)
    print(f'/nI like to watch {movie_genre} movies.')
    movie_title = print_movie_title(my_info)
    print(f'/nSome of my favourite movie are {movie_title}!')
    return

def print_student_name_id(my_info):
    my_name = my_info['full_name']
    first_name = my_info['full_name'].split(' ',1)
    student_id = my_info['student_id']
    print(f'My name is {my_name},but you can call me Queen{first_name}')
    print(f'My student ID is{student_id}')
    return

def add_pizza_toppings(my_info, toppings):
     my_info['pizza_toppings'].append(toppings)
     my_info['pizza_toppings'].sort(my_info, toppings)
     my_info['pizza_toppings'].lowercase(my_info, toppings)
     return

def print_pizza_toppings(my_info):
    pizza_toppings = my_info['pizza_toppings']
    print('\nMy favourite pizza toppings are:')
    for p in pizza_toppings:
        print(f'- {p}')
        return

def print_movie_genre(my_info):
     movies_genre = my_info['movies']
     for m in movies_genre:
            print(m['genre'],end=',')
            return

def print_movie_title(my_info):
     movie_title = my_info['movies']
     for m in movie_title:
            print(m['title'].title, end=' ,')
            return





if __name__ == '___main___':
    main()