import os
import mysql.connector # pip install mysql-connector-python

# MySQL ---------------------------------------------

def mySQL1():
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    showTag = input('Please specify a tag for the show genre [e.g.: Magic, Slice of Life, Fantasy, Action]: ')

    # Send a SQL query to the MySQL server:
    cursor.execute('\
                    SELECT animeID, title, genre \
                    FROM AnimeInfo \
                    INNER JOIN Production USING (title) \
                    WHERE genre LIKE "%' + showTag + '%";')

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    cursor.close()
    mydb.close()

def mySQL2(userID):
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    animeID = input('\n\nPlease specify the ID of the anime you wish to rate: ')
    meanScore = input('Assign a value between 0.00 and 10.00 for the rating: ')
    liked = input('Wanna Like this anime as a favorite show? [0 = No; 1 = Like]: ')

    # Send a SQL query to the MySQL server:
    cursor.execute('\
                    INSERT INTO UserRatings \
                    (userID, animeID, personalScore, liked) \
                    VALUES  (' + str(userID) + ',' + animeID + ',' + meanScore + ',' + liked + ');')

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    mydb.commit()
    cursor.close()
    mydb.close()
    print('\n\n')

def mySQL3(userID):
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    animeID = input('\n\nPlease specify the ID of the anime to modify the current rating: ')
    meanScore = input('Assign a new value between 0.00 and 10.00 for the rating: ')
    liked = input('Wanna Like this anime as a favorite show? [0 = No; 1 = Like]: ')

    # Send a SQL query to the MySQL server:
    query = '\
            UPDATE UserRatings \
            SET userID = ' + str(userID) +  ', personalScore = ' + meanScore + ', liked = ' + liked + \
            ' WHERE animeID = ' + animeID + ';'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    mydb.commit()
    cursor.close()
    mydb.close()
    print('\n\n')

def mySQL4(userID):
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    animeID = input('\n\nPlease specify the ID of the anime to delete the corresponding record: ')

    # Send a SQL query to the MySQL server:
    query = '\
            DELETE FROM UserRatings \
            WHERE animeID = ' + animeID + ';'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    mydb.commit()
    cursor.close()
    mydb.close()
    print('\n\n')


def mySQL5():
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    animeID = input('\n\nPlease specify the ID of the anime: ')

    # Send a SQL query to the MySQL server:
    query = '\
            SELECT animeID \
            FROM AnimeInfo \
            INNER JOIN Music USING (title)\
            WHERE animeID = ' + animeID + ';'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    # Send a SQL query to the MySQL server:
    query = '\
            SELECT title \
            FROM AnimeInfo \
            INNER JOIN Music USING (title)\
            WHERE animeID = ' + animeID + ';'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    # Send a SQL query to the MySQL server:
    query = '\
            SELECT openingTheme \
            FROM AnimeInfo \
            INNER JOIN Music USING (title)\
            WHERE animeID = ' + animeID + ';'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    # Send a SQL query to the MySQL server:
    query = '\
            SELECT endingTheme \
            FROM AnimeInfo \
            INNER JOIN Music USING (title)\
            WHERE animeID = ' + animeID + ';'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    mydb.commit()
    cursor.close()
    mydb.close()
    print('\n\n')   

def mySQL6():
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    keyword = input('\n\nPlease specify a keyword for filtering show titles: ')

    # Send a SQL query to the MySQL server:
    query = '\
            SELECT animeID, title, durationPerEpisode \
            FROM AnimeInfo \
            WHERE title LIKE "%' + keyword + '%";'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    mydb.commit()
    cursor.close()
    mydb.close()
    print('\n\n')   


def mySQL7():
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    print('R - 17+ (violence & profanity)')
    print('PG-13 - Teens 13 or older')
    print('PG - Children')
    print('R+ - Mild Nudity')
    print('G - All Ages')
    
    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    genre = input('\n\nPlease specify a keyword for filtering show ratings: ')
    title = input('\n\nPlease specify a keyword for filtering show titles: ')

    # Send a SQL query to the MySQL server:
    query = '\
            SELECT animeID, title, rating \
            FROM AnimeInfo \
            WHERE rating LIKE "%' + genre + '%"\
            AND title LIKE "%' + title+ '%";'
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    mydb.commit()
    cursor.close()
    mydb.close()
    print('\n\n')   

def mySQL8():
    # Connect to the local MySQL server
    mydb = mysql.connector.connect(
    host="localhost",
    user="admin",
    password="La332s$5r%",
    database="animedb"
    )

    print('R - 17+ (violence & profanity)')
    print('PG-13 - Teens 13 or older')
    print('PG - Children')
    print('R+ - Mild Nudity')
    print('G - All Ages')
    
    # Create a cursor to execute SQL queries:
    cursor = mydb.cursor()

    # Ask user for specity tags:
    genre = input('\n\nPlease specify a keyword for filtering show ratings: ')

    # Send a SQL query to the MySQL server:
    query = '\
            SELECT rating, COUNT(animeID) AS genreCount \
            FROM AnimeInfo \
            WHERE rating LIKE "%' + genre + '%"\
            GROUP BY rating;'
           
    
    cursor.execute(query)

    # Fetch the results of the query:
    result = cursor.fetchall()

    # Print the results:
    for i in result:
        print(i)

    mydb.commit()
    cursor.close()
    mydb.close()
    print('\n\n')   
    

# ---------------------------------------------------

# Clean the screen first:
os.system('clear')

# We have to start the MySQL Server:
os.system('echo "Starting MySQL Server..." ')
print('This is a test client, you can use the password "toor" when prompted: ')
os.system('sudo systemctl enable --now mysql ')

# Use the system test password "toor" to execute command as root:

# Now, print menu with options:

art = '''
⠤⠤⠤⠤⠤⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠤⠶⠶⠶⠦⠤⠤⠤⠤⠤⢤⣤⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⠄⢂⣠⣭⣭⣕⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠤⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉
⠀⠀⢀⠜⣳⣾⡿⠛⣿⣿⣿⣦⡠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣍⣀⣦⠦⠄⣀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠠⣄⣽⣿⠋⠀⡰⢿⣿⣿⣿⣿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⡿⠛⠛⡿⠿⣿⣿⣿⣿⣿⣿⣷⣶⣿⣁⣂⣤⡄⠀⠀⠀⠀⠀⠀
⢳⣶⣼⣿⠃⠀⢀⠧⠤⢜⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⠟⠁⠀⠀⠀⡇⠀⣀⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠁⠐⠀⣀⠀⠀
⠀⠙⠻⣿⠀⠀⠀⠀⠀⠀⢹⣿⣿⡝⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠋⠀⠀⠀⠀⠠⠃⠁⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⡿⠋⠀⠀
⠀⠀⠀⠙⡄⠀⠀⠀⠀⠀⢸⣿⣿⡃⢼⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡏⠉⠉⠻⣿⡿⠋⠀⠀⠀⠀
⠀⠀⠀⠀⢰⠀⠀⠰⡒⠊⠻⠿⠋⠐⡼⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⠀⠀⠀⠀⣿⠇⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠸⣇⡀⠀⠑⢄⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢖⠠⠤⠤⠔⠙⠻⠿⠋⠱⡑⢄⠀⢠⠟⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠉⠒⠒⠻⠶⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠡⢀⡵⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠦⣀⠀⠀⠀⠀⠀⢀⣤⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠙⠛⠓⠒⠲⠿⢍⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                   _                    _ _     
                  (_)                  | | |    
         _ _ _ __  _ _ __ ___   ___  __| | |__  
       / _` | '_ \| | '_ ` _ \ / _ \/ _` | '_ \ 
      | (_| | | | | | | | | | |  __/ (_| | |_) |
       \__,_|_| |_|_|_| |_| |_|\___|\__,_|_.__/ 
                                                                                    
'''

print(art)

# Print options menu (EOF to exit program):

while(1):

    print('\n\nSelect the operation you wish to perform: \n')
    print('-1: Quit! \n')
    print('0: Clean screen... 🧹\n')
    print('1: Filter shows by genre.\n')
    print('2: Rate a show.\n')
    print('3: Modify a rating for a show.\n')
    print('4: Delete a rating record.\n')
    print('5: Find Music by ID.\n')
    print('6: Find shows by keyword.\n')
    print('7: Filter shows by rating.\n')
    print('8: Check number of episodes per rating!\n')
    print('9: ~Credits~ \n')

    # This is the ID for our test user:
    userID = 0;

    option = int(input('Selected option: '))
    print('\n')

    # Options behaviour ----------------------------------------------------------------------------

    if(option == -1):
        exit()

    if(option == 0):
        os.system('clear')
        print(art)

    if(option == 1):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL1()

    if(option == 2):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL2(userID) 
    
    if(option == 3):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL3(userID)
        
    if(option == 4):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL4(userID)

    if(option == 5):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL5()

    if(option == 6):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL6()

    if(option == 7):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL7()

    if(option == 8):
        # The commands for MySQL are executed by calling the corresponding method: 
        mySQL8()

    if(option == 9):
       credits1 = '''
       Made by:
   _____             _   ______ _                                  
  / ____|           | | |  ____(_)                                 
 | (___   __ _ _   _| | | |__   _  __ _ _   _  ___ _ __ ___   __ _ 
  \___ \ / _` | | | | | |  __| | |/ _` | | | |/ _ \ '__/ _ \ / _` |
  ____) | (_| | |_| | | | |    | | (_| | |_| |  __/ | | (_) | (_| |
 |_____/ \__,_|\__,_|_| |_|    |_|\__, |\__,_|\___|_|  \___/ \__,_|
                                   __/ |                           
                                  |___/                            
        &
       ''' 

       credits2 = '''
   _____           _ _     _____      _       _ 
  / ____|         (_) |   |  __ \    | |     | |
 | (___  _ __ ___  _| |_  | |__) |_ _| |_ ___| |
  \___ \| '_ ` _ \| | __| |  ___/ _` | __/ _ \ |
  ____) | | | | | | | |_  | |  | (_| | ||  __/ |
 |_____/|_| |_| |_|_|\__| |_|   \__,_|\__\___|_|
                                                
       ''' 

       print(credits1)
       print(credits2)

    # ----------------------------------------------------------------------------------------------

    os.system('echo "Operation was successful!"\n\n')
