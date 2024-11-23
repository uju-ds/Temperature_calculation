def main():
    try:
        # Get the temperature input from the user
        temperature = float(input("Enter a temperature: "))

        # Convert Celsius to Fahrenheit
        fahrenheit = (temperature * 1.8) + 32

        # Convert Fahrenheit to Celsius
        celsius = (temperature - 32) / 1.8

        # Print the results
        print(f"{temperature} degrees Celsius is {fahrenheit} degrees Fahrenheit")
        print(f"{temperature} degrees Fahrenheit is {celsius} degrees Celsius")

    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
