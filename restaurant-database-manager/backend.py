import sqlite3 #importing a library that supports SQL to manage the restaurants menu database

class Node: #The node class for use in the linked list class
    def __init__(self, data, next = None): #constructor taking data to be stored in the node and the node it should point to
        self.data = data
        self.next = next

class Linked_list: #linked list to be used as a data structure to store the meal objects
   def __init__(self, list1 = None): #constructor that can either take nothing or a list as a parameter
        self.head = None
        if list1 != None: #if the parameter is not None, transform the given list into a linked list format
            for i in list1:
                self.head = Node(i, self.head) #using nodes as part of the linked list
            

class Meal: #Define meal class which will hold the basic information about a meal as attributes
    #The front_end and back_end will interact with the meal object and its compents 
    #We use constructor for the meal class to set the attributes when a new meal obj is created
    def __init__(self, id = None, name = None, price = None, ingredients = None, type = None, tags = None):
        #An int that holds id that repesents the meal item
        self.id = id
        #A string taht holds the name of the meal item
        self.name = name
        #A float that holds price of the meal item
        self.price = price
        #A string that holds all the ingredients in a commented format
        self.ingredients = ingredients
        #A string that holds the type of meal e.g. drink, dessert...
        self.type = type
        #A string that holds all the relevant tags (e.g. spicy, cold, kids...) in a commented format
        self.tags = tags

class Menu:
    def __init__(self, dbName):
        #Initlize a list to hold all meals
        self.mealList = Linked_list()
        #Connect to database, or create one if does not exist
        self.app = sqlite3.connect(dbName)
        #and create "menu" table and format it in desired way if it doesn't already exist in file
        self.app.execute(
            "CREATE TABLE IF NOT EXISTS menu (id INTEGER, name TEXT, price REAL, ingredients TEXT, type TEXT, tags TEXT)"
        )
        self.app.commit()
        
    #Add meal to the database, using a meal object as a parameter
    def addMeal(self, Meal):
        #Take each attribute of the meal object and save it in the appropriate place in the table
        self.app.execute(
            "INSERT INTO menu (id, name, price, ingredients, type, tags) VALUES (?, ?, ?, ?, ?, ?)", (Meal.id, Meal.name, Meal.price, Meal.ingredients, Meal.type, Meal.tags)
        )
        #update and save changes in database
        self.app.commit()
        
    #Remove meal from the database based on its ID
    def removeMeal(self, meal):
        #search the table for rows that share the same id and deletes them (each row holds information about and represents a meal)
        self.app.execute(
            "DELETE FROM menu WHERE id = ?", (meal.id,)
        )
        #update and save changes in database
        self.app.commit()
        
        
    #Modify a meal in the database   
    def modifyMeal(self, Meal):
        #First remove the old meal with same ID
        self.removeMeal(Meal)
        #Then add the modified meal withe the changes attributes in its place, essentially replacing it
        self.addMeal(Meal)

    #Filter the menu based on various criteria, by using queries on the table
    def filter_menu(self, name = None, price=None, ingredient=None, meal_type=None, tags=None):
        #Filter the menu based on various criteria
        #Using text manipulation to make a query to feed into the table based on the parameters given in the function
        query = "SELECT * FROM menu"
        parameters = []
        if name is not None:
            if len(parameters) == 0:
                query += " WHERE name LIKE ?"
            else:
                query += " AND name LIKE ?"
            parameters.append('%'+name+'%')

        #Searching for prices less than or equal to the parameter given
        if price is not None:
            query += " WHERE price <= ?"
            parameters.append(price)

        if ingredient is not None:
            if len(parameters) == 0:
                query += " WHERE ingredients LIKE ?"
            else:
                query += " AND ingredients LIKE ?"
            parameters.append('%'+ingredient+'%')

        if meal_type is not None:
            if len(parameters) == 0:
                query += " WHERE type LIKE ?"
            else:
                query += " AND type LIKE ?"
            parameters.append('%'+meal_type+'%')
            
        if tags is not None:
            if len(parameters) == 0:
                query += " WHERE tags LIKE ?"
            else:
                query += " AND tags LIKE ?"
            parameters.append('%'+tags+'%')
            
        #Execute the query with the given parameters and fetch all the rows
        rows = self.app.execute(query, tuple(parameters)).fetchall()
        meals = []
        for row in rows:
            # Create Meal objects from the rows and add them to the meals list
            meals.append(Meal(row[0], row[1], row[2], row[3], row[4], row[5]))
            #Set the mealList attribute to the list of filtered meals
        self.mealList = Linked_list(meals)
        
    
