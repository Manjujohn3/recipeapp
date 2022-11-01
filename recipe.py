import mysql.connector

mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'recipedb')
mycursor = mydb.cursor() 

while True:
    print("select an option from menu")
    print("1 add recipe")
    print("2 view allrecipe")
    print("3 search a recipe")
    print("4 update the recipe")
    print("5 delete a recipe")
    print("6 exit")

    choice = int(input("Enter an option: "))
    if(choice==1):
        print("recipe enter selected")

        name = input("enter the name")
        discription = input("enter the discription")
        ingredients = input("enter the ingrideinets")
        price = int(input("enter the price"))
        sql = 'INSERT INTO `recipes`(`name`, `discription`, `ingredients`, `price`) VALUES (%s,%s,%s,%s)'
        data = (name,discription,ingredients,price)
        mycursor.execute(sql , data)
        mydb.commit()
        print("value inserted succesfully")

    elif(choice==2):
        print("view recipe selected")
    elif(choice==3):
        print("search recipeselected")
    elif(choice==4):
        print("update recipe selected")
    elif(choice==5):
        print("delete recipe selected")
    elif(choice==6):
        break