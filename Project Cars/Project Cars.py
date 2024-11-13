import os
import datetime
from typing import Any, Optional
from colorama import Fore, init
from rich.console import Console
from rich.table import Table


init(autoreset=True)



cars_txt_read_only = open("d:/School/Python/Python VS Code/Project Cars/Cars.txt", "r")

# the unordered list of cars contains lines with the stats of the cars. each line is in a string form and includes the details of each car.
unordered_list_cars: list[str] = cars_txt_read_only.readlines()  

# the database that will be used in the rest of the program for printing and data manipulation. it's a list contains dictionaries, one for each car, with its properties.
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






def input_registration_number_validator(input_item_number: str) -> Optional[int]:

    try:
        # Check if the input starts with '>' or '<' and remove the sign
        if input_item_number.startswith(">") or input_item_number.startswith("<"):

            input_registration_number_validator_with_operator(input_item_number)

        else:
            int_input_item_number = int(input_item_number)  # Convert numeric part to integer

            if 1001 <= int_input_item_number <= 9999:
                return int_input_item_number

            else:
                print("\nThe valid range of the registration number is between 1001 and 9999! Please give a number in this range!\n")
                return None


    except ValueError:
        print("\nValid registration numbers are only decimal numbers! Please try again!\n")
        return None


def search_per_registration_number_without_operator(input_item_number: int, items_database: list[dict]) -> None:

    item_found = False
        
    for item in items_database:

        item_number = item.get("Number")

        if item_number == input_item_number:
            print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n")
            item_found = True
    
    if not item_found:
        print(f"\nThere are no cars with the registration number {input_item_number} in the database!\n")


def input_registration_number_validator_with_operator(input_item_number: str) -> None:
    try:
        operator = input_item_number[0]  # Store the operator

        numeric_part = input_item_number[1:]  # Extract the number part

        int_input_item_number = int(numeric_part)

        if 1001 <= int_input_item_number <= 9999:

            search_per_registration_number_with_operator(int_input_item_number, operator, cars_database)

        else:
            print("\nThe valid range of the registration number is between 1001 and 9999! Please give a number in this range!\n")

    except ValueError:
        print("\nValid registration numbers are only decimal numbers! Please try again!\n")


def search_per_registration_number_with_operator(input_item_number: int, operator: str, items_database: list[dict])->None:        

    item_found = False
    item: dict[Any,Any]
        
    for item in items_database:
        
        
        item_number: int = 0
        item_number = item.get("Number")
        
        if operator == ">":
            if item_number > input_item_number:
                print(f"\nRegistration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n")
                item_found = True
        elif operator == "<":
            if item_number < input_item_number:
                print(f"\nRegistration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n")
                item_found = True

    if not item_found:
        print(f"\nThere are no cars with registration numbers {operator} {input_item_number} in the database!\n")






def search_per_brand(input_item_brand: str, items_database: list[dict]) -> None:

    item_found: bool = False

    for item in items_database:

        if input_item_brand == item["Brand"]:
            print(item)
            item_found = True        

    if not item_found:
        print(f"\nThere are no {input_item_brand} cars in the database!\n")   


def show_all_available_cars_brands(items_database: list[dict]) -> None:

    item:dict[Any, Any]
    brands: list[str]=[]

    for item in items_database:
        if item["Brand"] not in brands:
            brands.append(item["Brand"])

    print(f"\nThe available brands of the cars already in the database are the following: {((', '.join(sorted(brands)))).lower()}\n")


def input_brand_validator(input_item_brand: str) -> Optional[str]:
    
    if input_item_brand.isalpha():

        return input_item_brand
    
    else:
        print("\nYou entered an invalid input! Valid inputs are only words! Please try again!\n")

        return None






def show_all_available_cars_colors(items_database: list[dict]) -> None:

    item:dict[Any, Any]
    colors: list[str]=[]

    for item in items_database:
        if item["Color"] not in colors:
            colors.append(item["Color"])

    print(f"The available colors of the cars already in the database are the following: {((', '.join(sorted(colors)))).lower()}\n")


def search_per_color(input_item_color: str, items_database: list[dict]) -> None:
    found = False  # To track if any items are found

    for item in items_database:
        # Check if the item color starts with the input color
        if item["Color"].startswith(input_item_color):
            print(item)  # Print the item if the color matches
            found = True

    if not found:
        print(f"There are no {input_item_color} cars in the database!\n")



def input_color_validator(input_item_color: str) -> Optional[str]:
    
    if input_item_color.isalpha():
        return input_item_color

    else:
        print("You entered an invalid input! Valid inputs are only letters. Please try again!\n")
        return None






def input_year_validator(input_item_year: str) -> Optional[int]:

    current_year= int(datetime.datetime.now().strftime("%Y"))


    try:
        # Check if the input starts with '>' or '<' and remove the sign
        if input_item_year.startswith(">") or input_item_year.startswith("<"):

            input_year_validator_with_operator(input_item_year)

        else:
            int_input_item_year = int(input_item_year)  # Convert numeric part to integer

            if 1960 <= int_input_item_year <= current_year:
                return int_input_item_year

            else:
                print(f"Valid years are between 1960 and {current_year}. Please try again!\n")
                return None

    except ValueError:
        print("\nValid registration numbers are only decimal numbers! Please try again!\n")
        return None


def search_per_year_without_operator(input_item_year: int, items_database: list[dict]) -> None:

    item_found = False
        
    for item in items_database:

        item_number = item.get("Year")

        if item_number == input_item_year:
            print(f"Registration Number: {item_number}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item.get('Year')}\n")
            item_found = True
    
    if not item_found:
        print(f"\nThere are no cars with the registration number {input_item_year} in the database!\n")


def input_year_validator_with_operator(input_item_year: str) -> None:

    current_year= int(datetime.datetime.now().strftime("%Y"))


    try:
        operator = input_item_year[0]  # Store the operator

        numeric_part = input_item_year[1:]  # Extract the number part

        int_input_item_year = int(numeric_part)

        if 1960 <= int_input_item_year <= current_year:

            search_per_year_with_operator(int_input_item_year, operator, cars_database)

        else:
            print(f"Valid years are between 1960 and {current_year}. Please try again!\n")
            return None

    except ValueError:
        print("\nValid registration numbers are only decimal numbers! Please try again!\n")
        return None


def search_per_year_with_operator(input_item_year: int, operator: str, items_database: list[dict])->None:        

    item_found = False
    item: dict[Any,Any]
        
    for item in items_database:
        
        
        item_year: int = 0
        item_year = item.get("Year")
        
        if operator == ">":
            if item_year > input_item_year:
                print(f"\nRegistration Number: {item.get('Number')}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item_year}\n")
                item_found = True
        elif operator == "<":
            if item_year < input_item_year:
                print(f"\nRegistration Number: {item.get('Number')}{'Color':>25}: {item.get('Color')}{'Brand':>10}: {item.get('Brand'):<30}{'Production Year':>40}: {item_year}\n")
                item_found = True

    if not item_found:
        print(f"\nThere are no cars with registration numbers {operator} {input_item_year} in the database!\n")






def create_new_record(new_item_number: int, new_item_color: str, new_item_brand: str, new_item_year: int, items_database: list[dict]) -> None:
    

    new_item: dict[Any, Any]  

    new_item = {"Number": new_item_number, "Color": new_item_color, "Brand": new_item_brand, "Year": new_item_year}

    item: dict[Any, Any]  
    

    for item in items_database:        

        if new_item_number == item.get("Number"):
            print("You cannot enter a new car with the same registration number as the one present ALREADY in the database! Please give another registration number!")
            return None

    else:
        print(f"\nNew car had been added in the database succesfully!"
              f"\nRegistration number: {new_item["Number"]}\nColor: {new_item['Color']}\nBrand: {new_item['Brand']}\nProduction year: {new_item['Year']}\n")
        items_database.append(new_item)

  

    printing_database_with_specific_colors(items_database)






def delete_record(delete_item_registration_number: str, items_database: list[dict]) -> None:

    validated_number= input_registration_number_validator(delete_item_registration_number)

    found: bool = False

    if validated_number is None:
        return  # Exit if validation fails

    for item in items_database:

        if validated_number == item["Number"]:

            found = True

            items_database.remove(item)

            print(f"Car with registration number {validated_number} has been deleted successfully from the database!")

    printing_database_with_specific_colors(cars_database)
        
    if not found:
        print(f"No car with the registration number {validated_number} has been found in the database! Please give a valid registration number!")       






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
            
            
            print(item) 

        
    if not found:
        print(f"No car with the registration number {validated_number} has been found in the database! Please give a valid registration number!")  






def write_to_file(items_database: list[dict]):

    with open("d:/School/Python/Python VS Code/Project Cars/Cars.txt", "w") as file:
        for row in items_database:
            file.write(f"{row["Number"]}\t\t\t{row["Color"]}\t\t\t{row["Brand"]}\t\t\t{row["Year"]}\n")

    return "Database update successfully!"







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



def printing_database_with_specific_colors(database: list[dict]):

    console = Console()


    table = Table(title="Cars", style= "blue", show_lines=True, expand=True)

    if database:
        headers = database[0].keys()  # Assuming all dictionaries have the same keys
        for header in headers:
            table.add_column(header)
    
    for row_dict in database:
        row = [str(value) for value in row_dict.values()]
        table.add_row(*row)

    console.print(table)


'''
def printing_database_with_specific_colors(database: list[dict]) -> None:

    print(Fore.MAGENTA + f"{'Number':>33}{'Color':^45}{'Brand':^35}{'Year':^20}")

    print(Fore.YELLOW + "="*160)

    for item in database:

        item_color:str = ""

        if item.get("Color") == "WHITE":
            item_color = Fore.WHITE + f"{item.get('Color'):^48}"

        elif item.get("Color") == "BLACK":
            item_color = Fore.BLACK + f"{item.get('Color'):^48}"

        elif item.get("Color")== "RED":
            item_color = Fore.LIGHTRED_EX + f"{item.get('Color'):^48}"

        elif item.get("Color") == "YELLOW":
            item_color = Fore.LIGHTYELLOW_EX + f"{item.get('Color'):^48}"

        elif item.get("Color") == "BLUE":
            item_color = Fore.BLUE+ f"{item.get('Color'):^48}"

        elif item.get("Color") == "GREEN":
            item_color = Fore.GREEN+ f"{item.get('Color'):^48}"

        print(f"{item.get('Number'):>32}{item_color}{item.get('Brand'):^32}{item.get('Year'):^23}\n")
    
    print("\n\n")
'''





def search_menu() -> None:

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
            while True:
                input_registration_number_validation = input_registration_number_validator(input("\nPlease enter the registration number of the car you would like to search for:\n"))
                if input_registration_number_validation is not None:
                    search_per_registration_number_without_operator(input_registration_number_validation, cars_database)
                    break
                        
        elif selection_input == '2':
            while True:
                show_all_available_cars_brands(cars_database)
                input_brand_validation = input_brand_validator(input("\nPlease enter the brand of the car you would like to search for:\n").upper())
                if input_brand_validation is not None:
                    search_per_brand(input_brand_validation, cars_database)
                    break
                    
        elif selection_input == '3':
            while True:
                input_year_validation = input_year_validator(input("\nPlease enter the registration year of the car you would like to search for:\n"))
                if input_year_validation is not None:
                    search_per_year_without_operator(input_year_validation, cars_database)
                    break
                        

        elif selection_input == '4':
            while True:
                show_all_available_cars_colors(cars_database)
                input_color_validation = input_color_validator((input("\nPlease enter the color of the car you would like to search for:\n").upper()))
                if input_color_validation is not None:
                  search_per_color(input_color_validation, cars_database)
                  break
                                
        elif selection_input == '0':        
            return


   




def greeting() -> None:

    terminal_width = os.get_terminal_size().columns

    print("Welcome to the Cars Database Manipulation Program!\n\n".center(terminal_width))



def basic_menu() -> None:
    # Get terminal size (width, height)
    terminal_width = os.get_terminal_size().columns
    
    # Define the menu lines
    menu_lines = [
        "Please make a selection:\n",
        "Press 1 to see the unordered cars database.",
        "Press 2 to search for a car using specific search filters.",
        "Press 3 to create a new record.",
        "Press 4 to update an existing record.",
        "Press 5 to delete a record.",
        "Press 6 to store the changes!",
        "Press 0 to exit the program!\n"
    ]
    
    # Center and print each line
    for line in menu_lines:
        print(line.center(terminal_width))




greeting()


while True:

    basic_menu()

    selection: str = input()

    if selection == '1':

        printing_database_with_specific_colors(cars_database)

    elif selection == '2':

        search_menu()

    elif selection == '3':

        while True:

            new_record_registration_number = input_registration_number_validator(input("Please give the registration number of the car you want to put in the database:\n"))
            if new_record_registration_number is None:
                continue
            
            
            new_record_color = input_color_validator((input("Please give the color of the car you want to put in the database:\n")).upper())
            if new_record_color is None:
                continue

            new_record_brand = input_brand_validator((input("Please give the brand of the car you want to put in the database:\n")).upper())
            if new_record_brand is None:
                continue
            
            new_record_year = input_year_validator(input("Please give the production year of the car you want to put in the database:\n"))
            if new_record_year is None:
                continue
            
            create_new_record(new_record_registration_number, new_record_color, new_record_brand, new_record_year, cars_database)
            break

            

    elif selection == '4':

        sorted_registration_numbers = bubble_sort([item["Number"] for item in cars_database])

        print(f"Available registration numbers of the cars present in the database:\n{sorted_registration_numbers}\n")  

        update_record(input("Please give the registration number of the car you want to update in the database:\n"),cars_database)

        
    elif selection == '5':   
        
        sorted_registration_numbers = bubble_sort([item["Number"] for item in cars_database])

        print(f"Available registration numbers of the cars present in the database:\n{sorted_registration_numbers}\n")    

        delete_record(input("Please give the registration number of the car you want to remove from the database:\n"),cars_database)

    elif selection == '6':

        write_to_file(cars_database)

    elif selection == '0':
        print("Thank you for using the database manipulation program! Bye bye!")
        break






    
    
    
    
    
    
'''
    new_record_registration_number = input_registration_number_validator(input("Please give the registration number of the car you want to put in the database:\n"))
    
    new_record_color = input_color_validator((input("Please give the color of the car you want to put in the database:\n")).upper())

    new_record_brand = input_brand_validator((input("Please give the brand of the car you want to put in the database:\n")).upper())
    
    new_record_year = input_year_validator(input("Please give the production year of the car you want to put in the database:\n"))
    
    create_new_record(new_record_registration_number, new_record_color, new_record_brand, new_record_year, cars_database)
'''












'''
brands = []

for car in cars_database:
    if car["Brand"] not in brands:
        brands.append(car["Brand"])

print(f'The available brands of the cars in the database are: {", ".join(brands)}')



brands_set=set()

for car in cars_database:

    brands_set.add(car["Brand"])


print(f'The available brands of the cars in the database are: {", ".join(brands_set)}')




colors_set=set()

for car in cars_database:

    colors_set.add(car["Color"])

print(f'The available colors of the cars in the database are: {", ".join(colors_set)}')



TO BUBBLE SORT EINAI EDW!!!!!!!!!!!!!!

def bubble_sort(items_database: list[dict]) -> list[dict]:
            
        # Traverse through all cars in the list
    for i in range(len(items_database)):
            # Flag to detect if a swap occurred
        swapped = False
            
            # Last i elements are already sorted
        for j in range(0, len(items_database)-i-1):
                # If the current car's number is greater than the next car's number, swap them
            if items_database[j]["Number"] > items_database[j+1]["Number"]:
                    items_database[j], items_database[j+1] = items_database[j+1], items_database[j]
                    swapped = True
            
            # If no swap occurred in the inner loop, the list is already sorted
        if not swapped:
                break
        
    return items_database



def print_current_working_directory():
    print(f"The current working directory is the following: {os.getcwd()}. ")


print_current_working_directory()
'''
'''
def input_registration_number_validator(input_item_number: str):
    try:
        # Check if the input starts with '>' or '<' and remove the sign
        if input_item_number.startswith(">") or input_item_number.startswith("<"):
            operator = input_item_number[0]  # Store the operator
            numeric_part = input_item_number[1:]  # Extract the number part
        else:
            operator = None
            numeric_part = input_item_number  # Treat input as pure number if no operator
        
        int_input_item_number = int(numeric_part)  # Convert numeric part to integer

        if 1001 <= int_input_item_number <= 9999:
            # Call the search function with the appropriate parameters
            search_per_registration_number(input_item_number=int_input_item_number, 
                                           items_database=cars_database, 
                                           operator=operator)

        else:
            print("The valid range of the registration number is between 1001 and 9999! Please give a number in this range!")

    except ValueError:
        print("Valid registration numbers are only decimal numbers! Please try again!")




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


def search_menu_selection(selection_input: str) -> None:

    while True:

        selection_input = search_menu()

        if selection_input == '1':
            input_registration_number_validation = input_registration_number_validator(input("\nPlease enter the registration number of the car you would like to search for:\n"))
            if input_registration_number_validation is not None:
                search_per_registration_number_without_operator(input_registration_number_validation, cars_database)
                        
        elif selection_input == '2':
            show_all_available_cars_brands(cars_database)
            input_brand_validation = input_brand_validator(input("\nPlease enter the brand of the car you would like to search for:\n").upper())
            if input_brand_validation is not None:
                search_per_brand(input_brand_validation, cars_database)
                    
        elif selection_input == '3':
            input_year_validation = input_year_validator(input("\nPlease enter the registration year of the car you would like to search for:\n"))
            if input_year_validation is not None:
                search_per_year_without_operator(input_year_validation, cars_database)
                        

        elif selection_input == '4':
            show_all_available_cars_colors(cars_database)
            input_color_validation = input_color_validator((input("\nPlease enter the color of the car you would like to search for:\n").upper()))
            if input_color_validation is not None:
                search_per_color(input_color_validation, cars_database)
                            
        elif selection_input == '0':        
            return

'''
