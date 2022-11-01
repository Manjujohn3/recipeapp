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