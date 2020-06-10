# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# Jeff Nelson,2020-06-08,Added menu to IO class
# Jeff Nelson,2020-06-08,Added Product class code and File processor
# Jeff Nelson,2020-06-09,Added comment and cleaned up code to make work
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []
strChoice = ""  # Captures the user option selection
data_flag = ""  # A flag to track if the data has been written to a file

class Product:
    """Stores data about a product:
    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        Jnelson, 2020-06-08, added constructor, Properties and Methods code
    """
    pass
    # TODO: Add Code to the Product class
    # --Fields--
    # product_name = ""
    # product_price = ""

    # --Constructor--
    def __init__(self, product_name: str, product_price: float):
        try:
            self.__product_name = str(product_name)
            self.__product_price = float(product_price)
        except Exception as e:
            raise Exception("Initial data input incorrect" + "\n")

    # --Properties--
    # Product Name
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value.title()
        else:
            raise Exception("Product name needs to only alpha characters")

    # Product Price
    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if str(value).isnumeric() == True:
            self.__product_price = float(value)
        else:
            raise Exception("Only number for the price please.")

    def __str__(self):  #
        return self.product_name + ', ' + str(self.product_price)

# --End of class--

# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
# check weather a number is passed in
class FileProcessor:
    """Processes data to and from a file and a list of product objects:
    methods:
        save_data_to_file(file_name, list_of_product_objects):
        read_data_from_file(file_name): -> (a list of product objects)
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        JNelson
    """
    pass
    # TODO: Add Code to process data from a file
    @staticmethod
    def read_data_from_file(file_name, lstOfProductObjects):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param lstOfProductObjects: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        file = open(file_name, "r")
        for lines in file:
            data = lines.split(",")
            row = Product(data[0], data[1])
            lstOfProductObjects.append(row)
        file.close()
        return lstOfProductObjects

    # TODO: Add Code to process data to a file
    @staticmethod
    def write_data_to_file(file_name, list_of_product_objects):
        """ Reads data from a file into a list of dictionary rows
        :param file_name: (string) with name of file:
        :param list_of_product_objects: (list) of product data saved to file data:
        :return: (list) of dictionary rows
        """
        try:
            file = open(file_name, "w")
            for row in list_of_product_objects:
                file.write(row.__str__() + "\n")
            file.close()
            print("Product has been saved to " + strFileName)
        except Exception as e:
            raise e
        return list_of_product_objects
# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """
    pass
    @staticmethod
    def print_menu_Products():
        """  Display a menu of choices to the user
        :return: nothing
        """
        print('''
        Menu of Options
        1) Show current list of Products.
        2) Add a new Product and Price.
        3) Save Data to Products.txt
        4) Exit Program.
        ''')
        print()  # Add an extra line for looks


    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user
        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 4] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user
        :return: string
        """
        return str(input(message)).strip().lower()


    @staticmethod
    def print_current_Tasks_in_list(table):
        """ Shows the current Tasks in the list of dictionaries rows
        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        i = 0
        print("******* The current Product are: *******")
        for row in table:
            print(row.product_name + " | " + "${:,.2f}".format(float(row.product_price)))
            i = 1
        if (i == 0):
            print("No tasks in file. Ready to add tasks!")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_new_product_and_price():
        """ Gathers the users new task and priority inputs
        :return: list () of products
        """
        pass  # TODO: Add Code Here!
        try:
            name = str(input("Product Name: ").strip())
            price = float(input("Product Price: ").strip())
            row = Product(product_name=name, product_price=price)
        except Exception as e:
            print("There was an error!")
            print(e, e.__doc__)
        return row


# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
# TODO: Add Data Code to the Main body
# Load data from file into a list of product objects when script starts
# Show user a menu of options
# Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file
    # exit program

# Main Body of Script  ---------------------------------------------------- #

FileProcessor.read_data_from_file(strFileName, lstOfProductObjects)

while(True):
    IO.print_menu_Products() # Show menu
    strChoice = IO.input_menu_choice()  # Get menu option

    # Process user's menu choice
    if strChoice.strip() == '1':  # Show Current list of products
        # TODO: Add Code Here
        IO.print_current_Tasks_in_list(lstOfProductObjects)
        continue  # to show the menu

    elif strChoice == '2':  # Add new product and price
        # TODO: Add Code Here
        lstOfProductObjects.append(IO.input_new_product_and_price())
        data_flag = 2 # set flag to double check if you want to save the file
        continue  # to show the menu

    elif strChoice == '3':  # Save Data to File
        FileProcessor.write_data_to_file(strFileName, lstOfProductObjects)
        data_flag = 3 # set flag that the new data has been saved
        continue  # to show the menu


    elif strChoice == '4':  # Exit Program
        if data_flag == 2:
            strChoice = IO.input_yes_no_choice("You have not saved new data. Are you sure you want Exit? (y/n) -  ")
            if strChoice.lower() == 'y':
                print("Goodbye!")
                break  # and Exit
            else:
                continue  # to shoe the menu
        elif data_flag != 1:
            print("Goodbye!")
            break  # and Exit