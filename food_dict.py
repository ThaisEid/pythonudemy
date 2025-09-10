foodPrice = {}

for _ in range(3):

    food = input("Digite o alimento: ")
    price = float(input("Digite o valor: "))
    foodPrice[food] = price


print(foodPrice)

for food, price in foodPrice.items():
    if price == max(foodPrice.values()):
        print(food)

avaregePrice = (sum(foodPrice.values()) / len(foodPrice))
print(round(avaregePrice, 2))
