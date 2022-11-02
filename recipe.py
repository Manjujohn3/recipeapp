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
        sql = 'SELECT * FROM `recipes`'
        mycursor.execute(sql)
        result =  mycursor.fetchall()
        for i in result:
            print(i) 
        


    elif(choice==3):
        print("search recipeselected")
        name = input("enter the recipe name: ")
        sql = "SELECT `id`, `name`, `discription`, `ingredients`, `price` FROM `recipes` WHERE `name` ='"+name+"'"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)



    elif(choice==4):
        print("update recipe selected")
        name = input("enter the name")
        discription = input("enter the discription to be updated")
        ingredients = input("enter the ingrideinets to be updated")
        price = (input("enter the price to be updated"))
        sql = "UPDATE `recipes` SET `discription`='"+discription+"',`ingredients`='"+ingredients+"',`price`='"+price+"' WHERE `name`='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("updated succusfully")


    elif(choice==5):
        print("delete recipe selected")
        name = input("enter the name: ")
        sql = "DELETE FROM `recipes` WHERE `name` ='"+name+"'"
        mycursor.execute(sql)
        mydb.commit()
        print("data deleted successfully")

    elif(choice==6):
        break