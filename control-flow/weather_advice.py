# weather_advice.py
# prompt user for weather input
weather = input(" What is the weather like tody? (sunny/rainy/cold): ").lower()

#provide clothing recommendation using if, elif ,else
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.") 
elif weather == "cold":
    print("Wear a warm jacket and a scarf.")
else:
    print("Sorry, I don't have recommendation for this weather.")