
class coffeeMachine:
    def __init__(self, water, milk, coffee, money):
        self.water = water #ml
        self.milk = milk #ml
        self.coffee = coffee #g
        self.money = money 
        self.espresso = {
            "cost": 1.50,
            "water": 50,
            "coffee": 18,
            "milk": 0
        }
        self.latte = {
            "cost": 2.50,
            "water": 200,
            "coffee": 24,
            "milk": 150
        }
        self.cappuccino = {
            "cost": 3.00,
            "water": 250,
            "coffee": 24,
            "milk": 100
        }

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")
    
    def promptUser(self):
        return input("What would you like? (espresso/latte/cappuccino): ").casefold()

    def canWeMakeDrink(self, drink):
        weCanMake = True
        cost, water, coffee, milk = drink.values()
        if self.water < water:
            print(f"Sorry, not enough water: need {water}ml, have: {self.water}ml.")
            weCanMake = False
        if (self.coffee < coffee):
            print(f"Sorry, not enough coffee: need {coffee}g, have: {self.coffee}g")
            weCanMake = False
        if (self.milk < milk):
            print(f"Sorry, not enough milk: need {milk}ml, have {self.milk}ml")
            weCanMake = False
        return weCanMake

    def canWeMakeDrinkName(self, drinkName):
        if drinkName == "espresso":
            return self.canWeMakeDrink(self.espresso)
        elif drinkName == "latte":
            return self.canWeMakeDrink(self.latte)
        elif drinkName == "cappuccino":
            return self.canWeMakeDrink(self.cappuccino)
        else :
            print("Invalid entry, please try again")
            return False

    def processPayment(self, drinkCost, quarters, dimes, nickles, pennies):
        moneyLeft = (quarters*(.25)+dimes*(.10)+nickles*(.05)+pennies*(.01) - drinkCost)
        if (moneyLeft < 0) : #not enough money
            print("Sorry, not enough money. Money refunded")
            return False
        elif (moneyLeft == 0) :
            print("Transaction Successful")
            return True
        else : #more than enough money
            print(f"Transaction Successful, heres your change: ${round(moneyLeft, 2)}")
            return True

    def takePayment(self, drinkName):
        quarters = int(input("Quarters: "))
        dimes = int(input("Dimes: "))
        nickles = int(input("Nickles: "))
        pennies = int(input("Pennies: "))
        drinkCost = self.getCost(drinkName)
        success = self.processPayment(drinkCost, quarters, dimes, nickles, pennies)
        if (success):
            self.makeDrink(drinkName)

    def makeDrink(self, drinkName):
        print(f"Making {drinkName}")
        cost, water, coffee, milk = self.getDrinkObject(drinkName).values()
        self.money += cost
        self.water -= water
        self.coffee -= coffee
        self.milk -= milk
        print(f"Here's your {drinkName}, enjoy!")
    
    def runMachine(self):
        userResponse = ''
        while (userResponse != "off"):
            userResponse = self.promptUser()
            if userResponse == "off":
                print("Turning Machine Off")
            elif userResponse == "report":
                self.report()
            else :
                weCanMakeDrink = self.canWeMakeDrinkName(userResponse)
                if weCanMakeDrink : 
                    self.takePayment(userResponse)
              

    def getCost(self, drinkName):
        if (drinkName == "espresso"):
            return self.espresso.get("cost")
        elif (drinkName == "latte"):
            return self.latte.get("cost")
        elif (drinkName == "cappuccino"):
            return self.cappuccino.get("cost")
                
    def getDrinkObject(self, drinkName):
        if (drinkName == "espresso"):
            return self.espresso
        elif (drinkName == "latte"):
            return self.latte
        elif (drinkName == "cappuccino"):
            return self.cappuccino




coffeeMachine1 = coffeeMachine(300, 200, 100, 0.00)
coffeeMachine1.runMachine()
