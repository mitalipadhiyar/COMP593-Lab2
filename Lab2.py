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

    my_info['movies'].append({'title':'jumanji', 'genre':'adventure'})
    print_student_name_id(my_info)
    print_pizza_toppings(my_info)
    add_pizza_toppings(my_info, ('pizza sauce', 'oregano', 'chiily flakes'))
    print_pizza_toppings(my_info)
    print_movie_genre(my_info)
    print_movie_title(my_info['movies'])
    return

def print_student_name_id(my_info):
    my_name = my_info['full_name']
    name_list = my_info['full_name'].split()
    first_name = name_list[0]
    student_id = my_info['student_id']
    print(f'My name is {my_name}, but you can call me Queen {first_name}.')
    print(f'My student ID is {student_id}.')
    return

def add_pizza_toppings(my_info, toppings):
     my_info['pizza_toppings'].extend(toppings)

     for i,topping in enumerate(my_info['pizza_toppings']):
        my_info['pizza_toppings'][i] = topping.lower()
     my_info['pizza_toppings'].sort()
     

def print_pizza_toppings(my_info):
    pizza_toppings = my_info['pizza_toppings']
    print('\nMy favourite pizza toppings are:')
    for p in pizza_toppings:
        print(f'- {p}')
        

def print_movie_genre(my_info):
    print('\nI like to watch ', end='')
    movies_list = my_info['movies']
    for i,m in enumerate (movies_list):
        if i < len(movies_list) - 1:
          print(m['genre'], end=', ')
        else:
          print(m['genre'], end=' movies.\n')  
    
    
            

def print_movie_title(movie_list):
    print(f"\nSome of my favourite movies are ", end='') 
    for i,m in enumerate (movie_list):
        if i < len(movie_list) - 1:
          print(m['title'].title(), end=', ')
        else: 
          print(m['title'].title(), end='!\n')
        
            
           


if __name__ == '__main__':
    main()