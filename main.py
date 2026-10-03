print("first program")
print("\nOptions:")
print("1 - Celsius to Fahrenheit")
print("2 - Fahrenheit to Celsius")
print("0 - Exit")
choice = input("Your choice: ")
if choice == "1":
    celsius = float(input("Insert temperature in Celsius: "))
    fahrenheit = (celsius * 1.8) + 32
    fahrenheit = round(fahrenheit, 1)
    print(f"{celsius} °C equals to {fahrenheit} °F")
elif choice == "2":
    fahrenheit = float(input("Insert temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) / 1.8
    celsius = round(celsius, 1)
    print(f"{fahrenheit} °F equals to {celsius} °C")
elif choice == "0":
    print("Exiting...")
else:
    print("Unknown option.")
print("program ending.")
