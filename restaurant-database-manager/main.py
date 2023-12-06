import PySimpleGUI as sg #Using PySimpleGui to create the windows and the front_end
from backend import * #imports everything from the back_end file (Meal and Menu classes) to establish a connection to the backend

#Create a menu instane to allow access to the function that operate the backend
menu1 = Menu('restaurant_database.db')

#define the initial window layout details uising pySimpleGUI Commands
def main_window():
    layout = [[sg.Text('Restaurant Manager', size=(20, 1), justification='center', font=('Helvetica', 36, 'bold'), text_color='#804040', background_color='#D9A88F', pad=((0,0),(50,50)))],
            [sg.Button('Open Menu', size=(30, 2), font=('Helvetica', 16), border_width=0, button_color=('#D9A88F', '#B06660'), pad=((0,0),(0,20)), key='menu')],
            [sg.Button('Quit', size=(30, 2), font=('Helvetica', 16), border_width=0, button_color=('#D9A88F', '#B06660'), pad=((0,0),(0,0)), key='quit')]]
    return sg.Window('Bakery Menu App', layout, size=(800, 600), element_justification='center', background_color=('#D9A88F'), finalize=True)
# Define the menu list window layout
def menu_list_window(name = None, price=None, ingredient=None, tags=None, meal_type=None):
    #Filter the menu based on the user's search criteria
    menu1.filter_menu(name, price, ingredient, meal_type, tags)
    #Create the search bar
    search = [sg.Button('Filter', button_color=('#D9A88F', '#B06660'), key='filt',size=(10, 1), font=('Helvetica')), 
          sg.InputText(key='meal_name', size=(70, 1)), 
          sg.Button('Search', button_color=('#D9A88F', '#B06660'),key='srch',font=('Helvetica', 10)),
          sg.Button('Clear', button_color=('#D9A88F', '#B06660'), key='clr', font=('Helvetica', 10))]

    #Create a list to hold the menu items
    listm = []
    #Create the add and back buttonsS
    add = [sg.Button('Add', button_color=('#D9A88F', '#B06660'), key='add', size = (10, 2), font=('Helvetica', 20))]
    back = [sg.Button('Back', button_color=('#D9A88F', '#B06660'),key='back', size = (10, 2), font=('Helvetica', 20))]
    #Create a column for the menu items and a column for the buttons
    col2 = [add, back]
    current = menu1.mealList.head
    while current != None:
        listm.append([sg.Button(current.data.name, button_color=('#D9A88F', '#B06660'),key=current.data,size=(44, 3), font=('Helvetica', 14))])
        current = current.next
    #Create the layout for the menu list window
    layout = [
        search,
        [[sg.Column(listm, size=(500, 500), scrollable=True, vertical_scroll_only=True), sg.Column(col2, background_color='#D9A88F')]]
    ]
    return sg.Window('Menu List', layout, size=(800, 600), element_justification='center', background_color=('#D9A88F'), finalize=True)

#Creates window for the meal details menu
def meal_details_window(meal):
    #create layout for the menu details window
    layout = [
        [sg.Text('MEAL DETAILS', size=(20, 1), justification='center', font=('Helvetica', 24, 'bold'), text_color='#804040', background_color='#D9A88F')],
        [sg.Text(f'ID: {meal.id}', text_color='#804040', background_color='#D9A88F', size=(100, 1), font=('Helvetica', 16))],
        [sg.Text(f'Name: {meal.name}', text_color='#804040', background_color='#D9A88F', size=(100, 1), font=('Helvetica', 16))],
        [sg.Text(f'Price: {meal.price}', text_color='#804040', background_color='#D9A88F', size=(100, 1), font=('Helvetica', 16))],
        [sg.Text(f'Type: {meal.type}', text_color='#804040', background_color='#D9A88F', size=(100, 1), font=('Helvetica', 16))],
        [sg.Text(f'Tags: {meal.tags}', text_color='#804040', background_color='#D9A88F', size=(100, 1), font=('Helvetica', 16))],
        [sg.Column([[sg.Text(f'Ingredients: {meal.ingredients}', text_color='#804040', background_color='#D9A88F', size=(100, 1), font=('Helvetica', 16))]], size = (1000, 27), background_color=('#D9A88F'), scrollable=True)],
        [sg.Button('Remove', button_color=('#D9A88F', '#B06660'),key='rem', font=('Helvetica', 22)),sg.Button('Modify',button_color=('#D9A88F', '#B06660'),key='mod', font=('Helvetica', 22)),sg.Button('Back', button_color=('#D9A88F', '#B06660'),key='back', font=('Helvetica', 22))],
    ]
    #create and return the window
    return sg.Window('Meal Details', layout, size=(800, 600), element_justification='center', background_color=('#D9A88F'), finalize=True)

#creates a window for adding new meal to the system
def add_meal_window():
    layout = [
    [sg.Text('INSERT NEW MEAL', size=(20, 1), justification='center', font=('Helvetica', 24, 'bold'), text_color='#804040', background_color='#D9A88F', pad=((0,0),(50,50)))],
    [sg.Text('ID: ', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(20,10))), sg.InputText(key='id', size=(30, 1), pad=((0,20),(20,10)))],
    [sg.Text('Name:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='name', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Price:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='price', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Ingredients:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='ingredients', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Type:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='type', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Tags:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='tags', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Button('Add', button_color=('#D9A88F', '#B06660'),key='add', font=('Helvetica', 22)),sg.Button('Back',button_color=('#D9A88F', '#B06660'),key='back', font=('Helvetica', 22))],
    ]
    return sg.Window('INSERT NEW MEAL', layout, size=(800, 600), element_justification='center', background_color=('#D9A88F'), finalize=True)

#creates window for modifying existing meal in the system
def modify_meal_window():
    layout = [
    [sg.Text('MODIFY MEAL', size=(20, 1), justification='center', font=('Helvetica', 24, 'bold'), text_color='#804040', background_color='#D9A88F', pad=((0,0),(50,50)))],
    [sg.Text('Name:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='name', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Price:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='price', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Ingredients:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='ingredients', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Type:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='type', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Tags:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='tags', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Button('Done', button_color=('#D9A88F', '#B06660'),key='mod', font=('Helvetica', 22)),sg.Button('Cancel',button_color=('#D9A88F', '#B06660'),key='cncl', font=('Helvetica', 22))],
    ]
    return sg.Window('MODIFY MEAL', layout, size=(800, 600), element_justification='center', background_color=('#D9A88F'), finalize=True)

#define and creates window for filtering meals
def filter_window():
    layout = [
    [sg.Text('FILTER', size=(20, 1), justification='center', font=('Helvetica', 24, 'bold'), text_color='#804040', background_color='#D9A88F', pad=((0,0),(50,50)))],
    [sg.Text('Name:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='name', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Price (less than):', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='price', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Ingredients:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='ingredients', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Type:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='type', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Text('Tags:', text_color='#804040', background_color='#D9A88F', size=(15, 1), pad=((20,0),(0,10))), sg.InputText(key='tags', size=(30, 1), pad=((0,20),(0,10)))],
    [sg.Button('Apply', button_color=('#D9A88F', '#B06660'),key='app', font=('Helvetica', 22)),sg.Button('Back',button_color=('#D9A88F', '#B06660'),key='back', font=('Helvetica', 22))],
    ]
    return sg.Window('FILTER', layout, size=(800, 600), element_justification='center', background_color=('#D9A88F'), finalize=True)

#creates window that displays error message
def error_window():
    layout = [
        [sg.Text('INVALID INPUT!', size=(20, 1), justification='center', font=('Helvetica', 24, 'bold'), text_color='#804040', background_color='#D9A88F', pad=((0,0),(50,50)))],
        [sg.Button('Ok', button_color=('#D9A88F', '#B06660'),key='ok', font=('Helvetica', 14))]
    ]
    return sg.Window('FILTER', layout, size=(400, 200), element_justification='center', background_color=('#D9A88F'), finalize=True)

#this function creaes and runs the intial window 
def run_main_wind():
    #main window is created using the main_window() function.
    main_wind = main_window()
    #keep looping until user closes the window or quits the program.
    while True:
        #this line reads the events that occur in the main window and returns the event and its related values.
        event, values = main_wind.read()
        
        #if user closes the window or clicks the quit button, the program exits.
        if event == sg.WIN_CLOSED or event == "quit":
            exit()
        
        #if user clicks the menu button, close the main menu window and run the menu list window 
        if event == 'menu':
            main_wind.close()
            run_menu_list_wind()
            main_wind = main_window()

#define fucntion to run menu list window        
def run_menu_list_wind():
    #create menu list window
    menu_list_wind = menu_list_window()
    #start looping to wait for user input
    while True:
        #read user input from the menu list window
        event, values = menu_list_wind.read()
         #if user closes window, exit program
        if event == sg.WIN_CLOSED:
            exit()
        #if user clicks back button, close menu list window and go to prev window
        if event == "back":
            menu_list_wind.close()
            break
        
        if event == "add":
            menu_list_wind.close()
            run_add_meal_window()
            menu_list_wind = menu_list_window()
        
          #if user clicks on search button
        if event == 'srch':
             #get the value from the "meal_name" input field
            if values['meal_name'] == "":
                values['meal_name'] == None
            menu_list_wind.close()
             #run menu list with filtered results
            menu_list_wind = menu_list_window(name=values['meal_name'])
            
            
            #If user clicks on Clear button
        if event == 'clr':
            if values['meal_name'] == "":
                values['meal_name'] == None
            menu_list_wind.close()
            menu_list_wind = menu_list_window()
            
            
         #if user clicks the filter buttin, close the menu list window           
        if event == "filt":
            menu_list_wind.close()
             #and run the filter window
            filt = run_filter_wind()
            if filt == None:
                menu_list_wind = menu_list_window()
            else:
                menu_list_wind = menu_list_window(filt['name'], filt['price'], filt['ingredients'], filt['tags'], filt['type'])
        #if user clicks on meal, close the menu list window
        if type(event) == Meal:
            menu_list_wind.close()
            #and run the meal details window
            run_meal_details_wind(event)
            menu_list_wind = menu_list_window()
            
def run_meal_details_wind(meal):
        #ccreate a window to display meal details
    meal_details_wind = meal_details_window(meal)
    while True:
        #wait for user input
        event, values = meal_details_wind.read()
         #exit program if window is closed
        if event == sg.WIN_CLOSED:
            exit()
        
        if event == "back":
            meal_details_wind.close()
            break
        #remove the selected meal from the menu and close window if remove button clicked
        if event == "rem":
            menu1.removeMeal(meal)
            meal_details_wind.close()
            
            break
        #open a window to modify meal, if modify button is clicked
        if event == "mod":
            meal_details_wind.close()
            new_meal = run_modify_meal_wind(meal)
            #if a new meal is returned, update the current meal with the new meal
            if new_meal != None:
                meal = new_meal
            #create a new meal details window with the updated meal
            meal_details_wind = meal_details_window(meal)
            
                
def run_add_meal_window():
    
    add_meal_wind = add_meal_window()
    while True:
        event, values = add_meal_wind.read()
        
        if event == sg.WIN_CLOSED:
            exit()
        
        if event == "back":
            add_meal_wind.close()
            break
       
        if event == "add":
            # Checks for empty fields and sets them to None
            for i in values:
                if values[i] == '':
                    values[i] = None
            #set default values for ID and price if not entered
            if values['id'] == None:
                values['id'] = 0
            if values['price'] == None:
                values['price'] = 0.00
                
            try:
                #converts Id and price values to int and floats
                values['id'] = int(values['id'])
                values['price'] = float(values['price'])
                #add new meal to menu and closes the add meal menu
                menu1.addMeal(Meal(values['id'], values['name'], values['price'], values['ingredients'], values['type'], values['tags']))
                add_meal_wind.close()
                break
            #display an error message if the user has invalid input
            except ValueError:
                add_meal_wind.close()
                run_error_wind()
                add_meal_wind = add_meal_window()

#func runs the window reposnsible for meal modification and it takes an id (meal attribute) for the remove part (check remove_meal at beack_end)               
def run_modify_meal_wind(meal):
    modify_meal_wind = modify_meal_window()
    #input fields with the existing meal values
    modify_meal_wind['name'].update(value=meal.name)
    modify_meal_wind['price'].update(value=str(meal.price))
    modify_meal_wind['ingredients'].update(value=meal.ingredients)
    modify_meal_wind['type'].update(value=meal.type)
    modify_meal_wind['tags'].update(value=meal.tags)
    
    while True:
        event, values = modify_meal_wind.read()
        
        if event == sg.WIN_CLOSED:
            exit()
        
        if event == "cncl":
            modify_meal_wind.close()
            break
        
        if event == "mod":
            #empty strings are converted to None objects for query purposes
            for i in values:
                if values[i] == '':
                    values[i] = None
            try:
                # convert price to float to ensure type consistency
                if values['price'] != None:
                    values['price'] = float(values['price'])
                else:
                    values['price'] = 0.00
                     #Create a new Meal object with the updated values
                new_meal = Meal(meal.id, values['name'], values['price'], values['ingredients'], values['type'], values['tags'])
                menu1.modifyMeal(new_meal)
                modify_meal_wind.close()
                
                #return new_meal obj
                return new_meal
            #display an error message if the user has invalid input
            except ValueError:
                modify_meal_wind.close()
                run_error_wind()
                modify_meal_wind = modify_meal_window()
                
#runs filter window allowing user to filter the menu based on various criterias
def run_filter_wind():
    filter_wind = filter_window()
    while True:
        event, values = filter_wind.read()
        
        if event == sg.WIN_CLOSED:
            exit()
        
        if event == "back":
            filter_wind.close()
            break
        #starts the filtering operation if user clicks apply button
        
        if event == "app":
            for i in values:
                if values[i] == '':
                    values[i] = None
            #using try and except to stop program from crashing in case of errors due to input
            try:
               # convert price to float to ensure type consistency
                if values['price'] != None:
                    values['price'] = float(values['price'])
                    #Filter the menu items based on user's criteria
                menu1.filter_menu(values['name'], values['price'], values['ingredients'], values['tags'], values['type'])
                filter_wind.close()
                return values
            except ValueError:
                #display an error message if the user has invalid input
                filter_wind.close()
                run_error_wind()
                filter_wind = filter_window()
#func runs error window, displaying an error msg to the user that goes away only after window is closed (or ok is pressed), then goes back to the previous window
def run_error_wind():
    error_wind = error_window()
    while True:
        event, values = error_wind.read()
        
         
        #closes window if user clicks the ok button or closes the window
        if event == sg.WIN_CLOSED or event == "ok":
            error_wind.close()
            break

#Call the main widnow function to run the application as a whole and call the other functions when needed
run_main_wind()
