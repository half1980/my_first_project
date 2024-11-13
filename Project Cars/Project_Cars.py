import os
import sys
import datetime
from typing import Any, Optional
from rich.console import Console
from rich.table import Table
from rich.theme import Theme
#python -m rich.color


custom_theme = Theme({"greeting": "bold italic blue3", "bye bye": "bright_red", "basic menu": "orange1", "info": "italic dodger_blue1", "danger": "underline bold red1"})
console = Console(theme=custom_theme)



def resource_path(relative_path):
    """ Get the absolute path to the resource, used for PyInstaller. """
    try:
        # PyInstaller creates a temporary folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

# Use the resource_path function to access your file







'''
cars_txt_read_only = open(resource_path('d:/School/Python/Python VS Code/Project Cars/Cars.txt'), "r")






#the unordered list of cars contains lines with the stats of the cars. each line is in a string form and includes the details of each car.
unordered_list_cars: list[str] = cars_txt_read_only.readlines()

#the database that will be used in the rest of the program for printing and data manipulation. it's a list contains dictionaries, one for each car, with its properties.
cars_database: list[dict] = []


for line in unordered_list_cars:

    # transforming each string (line) of the unordered_list_cars into lists, one for each car, containing its details.
    line_into_car_list: list[str] = line.split()
    
    # creating a variable named "car" which is a dictionary containing specific details with keys and values assigning the values from the "line_into_car_list" list
    car: dict [Any,Any] = {                     
        "Number": int(line_into_car_list[0]),   
        "Color": line_into_car_list[1],
        "Brand": line_into_car_list[2],
        "Year": int(line_into_car_list[3])
        }

    cars_database.append(car)


cars_txt_read_only.close()
'''





def input_registration_number_validator(input_item_number: str, items_database: list[dict]) -> Optional[int]:

    """function to validate user's input regarding the registration number"""


    try:
        # Check if the input starts with '>' or '<' and remove the sign
        if input_item_number.startswith(">") or input_item_number.startswith("<"):

            input_registration_number_validator_with_operator(input_item_number, items_database)
            return None
        
        int_input_item_number = int(input_item_number)  # Convert numeric part to integer

        if 1001 <= int_input_item_number <= 9999:
            return int_input_item_number

        console.print("\nThe valid range of the registration number is between 1001 and 9999! Please give a number in this range!\n", style="danger")
        return None


    except ValueError:
        console.print("\nValid registration numbers are only decimal numbers! Please try again!\n", style="danger")
        return None


def search_per_registration_number_without_operator(input_item_number: int, items_database: list[dict]) -> None:

    """function to search the database per registration number of the car without operator in user's input"""
    item_found = False

    for item in items_database:

        item_number = item.get("Number")

        if item_number == input_item_number:
            console.print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n", style="info")
            item_found = True
    if not item_found:
        console.print(f"\nThere are no cars with the registration number {input_item_number} in the database!\n", style="danger")



def input_registration_number_validator_with_operator(input_item_number: str, items_database: list[dict]) -> None:

    try:
        operator = input_item_number[0]  # Store the operator

        numeric_part = input_item_number[1:]  # Extract the number part

        int_input_item_number = int(numeric_part)

        if 1001 <= int_input_item_number <= 9999:

            search_per_registration_number_with_operator(int_input_item_number, operator, items_database)

        else:
            console.print("\nThe valid range of the registration number is between 1001 and 9999! Please give a number in this range!\n", style="danger")

    except ValueError:
        console.print("\nValid registration numbers are only decimal numbers! Please try again!\n", style="danger")


def search_per_registration_number_with_operator(input_item_number: int, operator: str, items_database: list[dict])->None:        

    item_found = False
    item: dict[Any,Any]
        
    for item in items_database:
        
        
        item_number: int = 0
        item_number = item.get("Number")
        
        if operator == ">":
            if item_number > input_item_number:
                console.print(f"\nRegistration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n", style="info")
                item_found = True
        elif operator == "<":
            if item_number < input_item_number:
                console.print(f"\nRegistration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n", style="info")
                item_found = True

    if not item_found:
        console.print(f"\nThere are no cars with registration numbers {operator} {input_item_number} in the database! Please search using another registration number!\n", style="danger")






def search_per_brand(input_item_brand: str, items_database: list[dict]) -> None:

    item_found: bool = False

    for item in items_database:

        if input_item_brand == item["Brand"]:
            console.print(f"{item}", style="info")
            item_found = True        

    if not item_found:
        console.print(f"\nThere are no {input_item_brand} cars in the database!\n", style="danger")   


def show_all_available_cars_brands(items_database: list[dict]) -> None:

    item:dict[Any, Any]
    brands: list[str]=[]

    for item in items_database:
        if item["Brand"] not in brands:
            brands.append(item["Brand"])

    console.print(f"\nThe available brands of the cars already in the database are the following: {((', '.join(sorted(brands))))}\n", style="info")


def input_brand_validator(input_item_brand: str) -> Optional[str]:
    
    if input_item_brand.isalpha():

        return input_item_brand
    
    else:
        console.print("\nYou entered an invalid input! Valid inputs are only words! Please try again!\n", style="danger")

        return None






def show_all_available_cars_colors(items_database: list[dict]) -> None:

    console = Console()

    item:dict[Any, Any]
    colors: list[str]=[]
    color_mapping: dict[str, str] = {
        "RED": "bold red1",
        "BLUE": "bold blue1",
        "GREEN": "bold green1",
        "YELLOW": "bold yellow2",
        "BLACK": "bold gray0",
        "BROWN": "bold rosy brown",
        "PINK": "bold magenta1",
        "SILVER": "bold gray74",
        "WHITE": "bold bright_white",
        "GOLD": "gold3"}

    for item in items_database:
        car_color = item.get("Color", "")  # Safely get color or default to empty string
        if car_color and car_color not in colors:
            # Append the original color, not the mapped one, to avoid duplication
            colors.append(car_color)

    # Format the output using rich's color formatting
    formatted_colors: list[str] = []
    for color in colors:
        rich_color = color_mapping.get(color, "white")  # Default to white if not found in mapping
        formatted_colors.append(f"[{rich_color}]{color}[/{rich_color}]")


    console.print(f"The available colors of the cars already in the database are the following: {((', '.join(sorted(formatted_colors))))}\n")


def search_per_color(input_item_color: str, items_database: list[dict]) -> None:
    found = False  # To track if any items are found

    for item in items_database:
        # Check if the item color starts with the input color
        if item["Color"].startswith(input_item_color):
            console.print(f"{item}\n", style="info")  # Print the item if the color matches
            found = True

    if not found:
        console.print(f"There are no {input_item_color} cars in the database!\n", style="danger")



def input_color_validator(input_item_color: str) -> Optional[str]:
    
    if input_item_color.isalpha():
        return input_item_color

    else:
        console.print("You entered an invalid input! Valid inputs are only letters. Please try again!\n", style="danger")
        return None






def input_year_validator(input_item_year: str, items_database: list[dict]):

    current_year= int(datetime.datetime.now().strftime("%Y"))


    try:
        # Check if the input starts with '>' or '<' and remove the sign
        if input_item_year.startswith(">") or input_item_year.startswith("<"):

            input_year_validator_with_operator(input_item_year, items_database)

        else:
            int_input_item_year = int(input_item_year)  # Convert numeric part to integer

            if 1960 <= int_input_item_year <= current_year:
                return int_input_item_year

            else:
                console.print(f"Valid years are between 1960 and {current_year}. Please try again!\n", style="danger")
                return None

    except ValueError:
        console.print("\nValid registration numbers are only decimal numbers! Please try again!\n", style="danger")
        return None


def search_per_year_without_operator(input_item_year: int, items_database: list[dict]) -> None:

    item_found = False
        
    for item in items_database:

        item_number = item.get("Year")

        if item_number == input_item_year:
            console.print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n", style="info")
            item_found = True
    
    if not item_found:
        console.print(f"\nThere are no cars with the registration number {input_item_year} in the database!\n", style="danger")


def input_year_validator_with_operator(input_item_year: str, items_database: list[dict]) -> None:

    current_year= int(datetime.datetime.now().strftime("%Y"))


    try:
        operator = input_item_year[0]  # Store the operator

        numeric_part = input_item_year[1:]  # Extract the number part

        int_input_item_year = int(numeric_part)

        if 1960 <= int_input_item_year <= current_year:

            search_per_year_with_operator(int_input_item_year, operator, items_database)

        else:
            console.print(f"Valid years are between 1960 and {current_year}. Please try again!\n", style="danger")
            return None

    except ValueError:
        console.print("\nValid registration numbers are only decimal numbers! Please try again!\n", style="danger")
        return None


def search_per_year_with_operator(input_item_year: int, operator: str, items_database: list[dict])->None:        

    item_found = False
    item: dict[Any,Any]
        
    for item in items_database:
        
        
        item_year: int = 0
        item_year = item.get("Year")
        
        if operator == ">":
            if item_year > input_item_year:
                console.print(f"\nRegistration Number: {item.get('Number')}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item_year}\n", style="info")
                item_found = True
        elif operator == "<":
            if item_year < input_item_year:
                console.print(f"\nRegistration Number: {item.get('Number')}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item_year}\n", style="info")
                item_found = True

    if not item_found:
        console.print(f"\nThere are no cars with registration years {operator} {input_item_year} in the database!\n", style="danger")






def create_new_record(new_item_number: int, new_item_color: str, new_item_brand: str, new_item_year: int, items_database: list[dict]) -> None:
    

    new_item: dict[Any, Any]  

    new_item = {"Number": new_item_number, "Color": new_item_color, "Brand": new_item_brand, "Year": new_item_year}

    item: dict[Any, Any]  
    

    for item in items_database:        

        if new_item_number == item.get("Number"):
            console.print("You cannot enter a new car with the same registration number as the one present ALREADY in the database! Please give another registration number!", style="danger")
            return None

    
    console.print(f"\nNew car has been added in the database succesfully!"
        f"\nRegistration number: {new_item["Number"]}\nColor: {new_item['Color']}\nBrand: {new_item['Brand']}\nProduction year: {new_item['Year']}\n", style="info")
    
    items_database.append(new_item)

  

    printing_database_with_specific_colors(items_database)






def delete_record(delete_item_registration_number: str, items_database: list[dict]) -> None:

    validated_number= input_registration_number_validator(delete_item_registration_number, items_database)

    found: bool = False

    if validated_number is None:
        return  # Exit if validation fails

    for item in items_database:

        if validated_number == item["Number"]:

            found = True

            items_database.remove(item)

            console.print(f"Car with registration number {validated_number} has been deleted successfully from the database!\n", style="info")

    printing_database_with_specific_colors(items_database)
        
    if not found:
        console.print(f"No car with the registration number {validated_number} has been found in the database! Please give a valid registration number!", style="danger")       






def update_record(update_item_registration_number: str, items_database: list[dict]):
        
    validated_number= input_registration_number_validator(update_item_registration_number)

    found: bool = False

    item: dict[Any, Any]

    if validated_number is None:
        return  # Exit if validation fails

    for item in items_database:

        if validated_number == item["Number"]:

            found = True

            for key, value in item.items():

                while True:  # Loop until a valid value is entered

                    user_input = input(f"{key} (current value: {value}, leave empty to keep current): ")
                    
                    # If user input is empty, keep the current value
                    if user_input == "":

                        break  # Skip update, keep current value

                    if key == "Number":

                        new_value = input_registration_number_validator(user_input)

                        if new_value is not None:  # Valid input

                            item[key] = new_value

                            break  # Exit the loop

                    elif key == "Brand":

                        new_value = (input_brand_validator(user_input)).upper()

                        if new_value:  # Valid input

                            item[key] = new_value

                            break  # Exit the loop

                    elif key == "Color":

                        new_value = (input_color_validator(user_input)).upper()

                        if new_value:  # Valid input

                            item[key] = new_value

                            break  # Exit the loop

                    elif key == "Year":

                        new_value = input_year_validator(user_input)

                        if new_value is not None:  # Valid input

                            item[key] = new_value

                            break  # Exit the loop
            
            
            console.print(f"{item}\n", style="info") 

        
    if not found:
        console.print(f"No car with the registration number {validated_number} has been found in the database! Please give a valid registration number!\n", style="danger")  






def write_to_file(items_database: list[dict]) -> None:

    with open(resource_path('d:/School/Python/Python VS Code/Project Cars/Cars.txt'), "w") as file:
        for row in items_database:
            file.write(f"{row["Number"]}\t\t\t{row["Color"]}\t\t\t{row["Brand"]}\t\t\t{row["Year"]}\n")

    console.print("The changes you did, are now saved! The database has been updated successfully!\n", style="info")







def bubble_sort(list_of_registration_numbers: list[int]) -> list[int]:
     
    # Traverse through all cars in the list
    for i in range(len(list_of_registration_numbers)):
        # Flag to detect if a swap occurred
        swapped = False

        # Last i elements are already sorted
        for j in range(0, len(list_of_registration_numbers)-i-1):
                # If the current car's number is greater than the next car's number, swap them
            if list_of_registration_numbers[j] > list_of_registration_numbers[j+1]:
                list_of_registration_numbers[j], list_of_registration_numbers[j+1] = list_of_registration_numbers[j+1], list_of_registration_numbers[j]
                swapped = True
            
            # If no swap occurred in the inner loop, the list is already sorted
        if not swapped:
            break
        
    return list_of_registration_numbers



def printing_database_with_specific_colors(items_database: list[dict]) -> None:

    console = Console()
    
    table = Table(title="Cars", style= "magenta", show_lines=True, expand=True)

    if items_database:
        headers = items_database[0].keys()  # Assuming all dictionaries have the same keys
        for header in headers:
            table.add_column(header, justify="center")
    
    # Define color mappings for row styles
    color_mapping = {
        "red": "bold red1",
        "blue": "bold blue1",
        "green": "bold green1",
        "yellow": "bold yellow2",
        "black": "bold gray0",
        "brown": "bold rosy brown",
        "pink": "bold magenta1",
        "silver": "bold gray74",
        "white": "bold bright_white",
        "gold": "gold3"
        # Add more mappings as needed
    }

    # Add rows for each dictionary in the database.
    for row_dict in items_database:
        # Get the color from the row and map it to a console style
        car_color = row_dict.get("Color", "").lower()  # Default to empty string if color is missing
        row_style = color_mapping.get(car_color, "white")  # Default to 'white' if color is not found

        # Add the row to the table with the respective style
        row = [str(value) for value in row_dict.values()]
        table.add_row(*row, style=row_style)

    # Print the table to the console.
    console.print(table)





def search_menu(items_database: list[dict]) -> None:
    """the function for the search menu"""

    while True:
        
        terminal_width = os.get_terminal_size().columns

        menu_lines = [
                "Press 1 to search a car by its registration number.",
                "Press 2 to search a car by its brand name.",
                "Press 3 to search a car by its registration year.",
                "Press 4 to search a car by its color.",
                "Press 0 to exit to main menu!\n"
            ]
        
        for line in menu_lines:
            print(line.center(terminal_width))

        selection_input = input()

        if selection_input == '1':
            os.system('cls')
            while True:
                input_registration_number_validation = input_registration_number_validator(input("\nPlease enter the registration number of the car you would like to search for:\n"), items_database)
                if input_registration_number_validation is None:
                    continue
                search_per_registration_number_without_operator(input_registration_number_validation, items_database)
                break
                
                                
        elif selection_input == '2':
            show_all_available_cars_brands(items_database)
            input_brand_validation = input_brand_validator(input("\nPlease enter the brand of the car you would like to search for:\n").upper())
            if input_brand_validation is not None:
                search_per_brand(input_brand_validation, items_database)
            
                    
        elif selection_input == '3':
            input_year_validation = input_year_validator(input("\nPlease enter the registration year of the car you would like to search for:\n"), items_database)
            if input_year_validation is not None:
                search_per_year_without_operator(input_year_validation, items_database)
            
                        

        elif selection_input == '4':
                
            show_all_available_cars_colors(items_database)
            input_color_validation = input_color_validator((input("\nPlease enter the color of the car you would like to search for:\n").upper()))
            if input_color_validation is not None:
                search_per_color(input_color_validation, items_database)
            
                                
        elif selection_input == '0':
            os.system('cls')
            console.print("\nExiting to main menu...\n", style="info")
            break  # Return to the main menu


        else:
            os.system('cls')
            console.print("\nInvalid option! Please select a valid option!\n", style="danger")


   




def greeting() -> None:

    terminal_width = os.get_terminal_size().columns

    console.print("Welcome to the Cars Database Manipulation Program!\n\n".center(terminal_width),style="greeting")



def basic_menu() -> None:
    # Get terminal size (width, height)
    terminal_width = os.get_terminal_size().columns
    
    # Define the menu lines
    menu_lines = [
        f"Please make a selection:\n",
        f"Press 1 to see the unordered cars database.",
        f"Press 2 to search for a car using specific search filters.",
        f"Press 3 to create a new car record.",
        f"Press 4 to update an existing car record.",
        f"Press 5 to delete a car record.",
        f"Press 6 to store the changes!",
        f"Press 0 to exit the program!\n"
    ]
    
    # Center and print each line
    for line in menu_lines:
        console.print(line.center(terminal_width), style="basic menu")





def main():
    
    cars_txt_read_only = open(resource_path('C:/Users/panag/Desktop/Project Cars/Cars.txt'), "r")
    


    #the unordered list of cars contains lines with the stats of the cars. each line is in a string form and includes the details of each car.
    unordered_list_cars: list[str] = cars_txt_read_only.readlines()

    cars_database:list[dict]=[]

    for line in unordered_list_cars:

        # transforming each string (line) of the unordered_list_cars into lists, one for each car, containing its details.
        line_into_car_list: list[str] = line.split()
            
        # creating a variable named "car" which is a dictionary containing specific details with keys and values assigning the values from the "line_into_car_list" list
        car: dict [Any,Any] = {                     
                "Number": int(line_into_car_list[0]),   
                "Color": line_into_car_list[1],
                "Brand": line_into_car_list[2],
                "Year": int(line_into_car_list[3])
                }

        cars_database.append(car)

    cars_txt_read_only.close()




    greeting()


    while True:

        basic_menu()

        selection: str = input()

        if selection == '1':

            os.system('cls')

            printing_database_with_specific_colors(cars_database)

        elif selection == '2':

            search_menu(cars_database)


        elif selection == '3':

            os.system('cls')

            while True:

                new_record_registration_number = input_registration_number_validator(input("Please give the registration number of the car you want to put in the database:\n"), cars_database)
                if new_record_registration_number is None:
                    continue
                
                
                new_record_color = input_color_validator((input("Please give the color of the car you want to put in the database:\n")).upper())
                if new_record_color is None:
                    continue

                new_record_brand = input_brand_validator((input("Please give the brand of the car you want to put in the database:\n")).upper())
                if new_record_brand is None:
                    continue
                
                new_record_year = input_year_validator(input("Please give the production year of the car you want to put in the database:\n"), cars_database)
                if new_record_year is None:
                    continue
                
                create_new_record(new_record_registration_number, new_record_color, new_record_brand, new_record_year, cars_database)
                break
                

        elif selection == '4':

            os.system('cls')

            sorted_registration_numbers = bubble_sort([item["Number"] for item in cars_database])

            print(f"Available registration numbers of the cars present in the database:\n{sorted_registration_numbers}\n")  

            update_record(input("Please give the registration number of the car you want to update in the database:\n"),cars_database)

            
        elif selection == '5': 

            os.system('cls')  
            
            sorted_registration_numbers = bubble_sort([item["Number"] for item in cars_database])

            print(f"Available registration numbers of the cars present in the database:\n{sorted_registration_numbers}\n")    

            delete_record(input("Please give the registration number of the car you want to remove from the database:\n"),cars_database)

        elif selection == '6':
            os.system('cls')
            write_to_file(cars_database)

        elif selection == '0':
            os.system('cls')
            console.print("Thank you for using the database manipulation program! Bye bye!\n", style="bye bye")
            os.system("pause")
            break

        else:
            os.system('cls')
            console.print("\nInvalid option! Please select a valid option!\n", style="danger")






if __name__ == "__main__":

    main()



























'''
def search_per_registration_number(*args, **kwargs):
    items_database = kwargs.get('items_database', [])
    operator = kwargs.get('operator', None)  # Can be None, '>', or '<'
    input_item_number = kwargs.get('input_item_number', None)

    item_found = False

    

    for item in items_database:
        
        item_number = item.get("Number")

        # Check based on the operator
        if operator == ">":
            if item_number > input_item_number:
                print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n")
                item_found = True
        elif operator == "<":
            if item_number < input_item_number:
                print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n")
                item_found = True
        else:
            if item_number == input_item_number:
                print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n")
                item_found = True

    if not item_found:
        if operator:
            print(f"There are no cars with registration numbers {operator} {input_item_number} in the database!")
        else:
            print(f"There are no cars with the registration number {input_item_number} in the database!")

            

            
            
def input_year_validator(input_item_year: str):
    
    current_year= int(datetime.datetime.now().strftime("%Y"))

    try:
                # Check if the input starts with '>' or '<' and remove the sign
        if input_item_year.startswith(">") or input_item_year.startswith("<"):
            operator = input_item_year[0]  # Store the operator
            numeric_part = input_item_year[1:]  # Extract the number part
        else:
            operator = None
            numeric_part = input_item_year  # Treat input as pure number if no operator


        int_input_item_year = int(numeric_part)  
            
        if 1960 <= int_input_item_year <= current_year:
                        # Call the search function with the appropriate parameters
            search_per_year(input_item_year=int_input_item_year, 
                                           items_database=cars_database, 
                                           operator=operator)
        
        else:
            print(f"Valid years are between 1960 and {current_year}. Please try again!\n")
        
    except ValueError:
        print("\nValid input options are only decimal numbers! Please try again!\n")



def search_per_year(*args, **kwargs) -> None:

    items_database = kwargs.get('items_database', [])
    operator = kwargs.get('operator', None)  # Can be None, '>', or '<'
    input_item_year = kwargs.get('input_item_year', None)

    item_found: bool = False

    for item in items_database:

        item_year = item.get("Year")

        if operator == ">":
            if item_year > input_item_year:
                print(item)
                item_found = True
        elif operator == "<":
            if item_year < input_item_year:
                print(item)
                item_found = True
        else:
            if item_year == input_item_year:
                print(item)
                item_found = True

    if not item_found:
        if operator:
            print(f"There are no cars with registration numbers {operator} {input_item_year} in the database!")
        else:
            print(f"There are no cars with the registration number {input_item_year} in the database!")




'''

