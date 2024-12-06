import streamlit as st

# App Title
st.write("""
# Simple Temperature Conversion App
Enter a temperature in Celsius or Fahrenheit, and we'll convert it for you.
""")

# Main function for conversion
def main():
    # Input for temperature and scale
    temp_input = st.text_input("Enter a temperature (e.g., 100C or 212F):")

    if temp_input:  # Check if input is provided
        try:
            # Parse the input
            if temp_input[-1].upper() == 'C':  # If input ends with 'C' or 'c'
                celsius = float(temp_input[:-1])
                fahrenheit = (celsius * 1.8) + 32
                st.write(f"{celsius}°C is equal to {fahrenheit}°F.")
            elif temp_input[-1].upper() == 'F':  # If input ends with 'F' or 'f'
                fahrenheit = float(temp_input[:-1])
                celsius = (fahrenheit - 32) / 1.8
                st.write(f"{fahrenheit}°F is equal to {celsius}°C.")
            else:
                st.error("Please enter a valid temperature (e.g., 100C or 212F).")
        except ValueError:
            st.error("Invalid input. Please enter a numeric value followed by 'C' or 'F'.")

if __name__ == "__main__":
    main()
