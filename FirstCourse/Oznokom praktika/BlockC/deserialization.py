
import pickle

#десериализация 
with open('data.pkl', 'rb') as f:
    food1 = pickle.load(f)
    food2 = pickle.load(f)
    drink1 = pickle.load(f)
    drink2 = pickle.load(f)
    restaurant_menu = pickle.load(f)

#использование методов на серализированных файлах

print(drink1)
drink1.add_ingredient("Вода",150) #добавление ингредиента
drink1.print_ingredients()
food2.change_preparation_time(200)
print(food2)
print(food1)
print(restaurant_menu)
