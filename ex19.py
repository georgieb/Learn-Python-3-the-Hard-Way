# call a function and name it, provide the arguments, print the arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man thats's enough for a party!")
    print("Get a blanket. \n")

#provide function numbers in arguments
print("We can just  give the function numbers directly:")
cheese_and_crackers(20,30)

#define variables
print("OR, we can use variables from out script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#use math to define arguments 
print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

#add to the variable
print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese +100, amount_of_crackers + 1000)

def milk_and_cookies(milk_type, cookie_type):
    print(f"You are dumping your {cookie_type} cookie in {milk_type} milk")
milk_type = "skim"
cookie_type = "chocolate chip"
milk_and_cookies(milk_type, cookie_type)

def Income_Statement(Revenue, COGS, Gross_Margin, Gross_Margin_Percent, OPEX, Net_Income, Operating_Margin):
    print(f"Your Revenue is {Revenue} \n your COGS are {COGS} \n so your Gross Margin is {Gross_Margin} \n your Gross Margin % is {Gross_Margin_Percent} \n your OPEX is {OPEX} \n so your Net Income is {Net_Income} \n and your Operating Margin is {Operating_Margin}")

Revenue1 = 80
COGS1 = 50
Gross_Margin1 = Revenue1 - COGS1
Gross_Margin_Percent1 = (Revenue1 - COGS1)/Revenue1
OPEX1 = 10
Net_Income1 = Gross_Margin1 - OPEX1
Operating_Margin1 = Net_Income1/Revenue1

Income_Statement(Revenue1, COGS1, Gross_Margin1, Gross_Margin_Percent1, OPEX1, Net_Income1, Operating_Margin1)

