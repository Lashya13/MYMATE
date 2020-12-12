print("GOOD MORNING!!""\U0001f600" '\n''\n' "Today is the JUST" '\n' "chance to change DO" '\n' "yourself for the better." '\n''\n' "Hello!! Welcome to 'MY MATE' app" "\n")
print("ENTER YOUR DETAILS:-")
calories_intake={}
calories_burn = {}
work = {} 
expenditure={}
name=input("enter your name:")
age=int(input("enter your age:"))
email=input("enter your email address:")
weight=float(input("enter your weight:"))
height=float(input("enter your height:"))
BMI = (weight / (height * height))*10
print("\n" "your BMI value is:", BMI)
daily_income =int(input("enter your daily income:"))
    
def food(health):
    print("\n" "LET FOOD BE THY MEDICINE, THY MEDICINE SHALL BE THY FOOD")
    if(health == 'food'):
        for i in range(0,4):
            food_time = input("enter your food time:"'\n').lower()
            
            if (food_time == 'breakfast'):
                print("\n" "All happiness depends on a leisurely breakfast")
                Breakfast_count = int(input("enter number of items you take in breakfast:"))
                for b in range(Breakfast_count):
                    Breakfast_food = input("enter the Breakfast item name:")
                    food_quantity =int( input("enter your  Breakfast item quantity:"))
                    if (Breakfast_food ==  "idly"):
                        calories_intake_1 = food_quantity * 39
                        print(calories_intake_1)
                        
                        calories_intake.update({Breakfast_food :calories_intake_1 })
                       
                        
                    elif(Breakfast_food == "chapati"):
                      
                        calories_intake_1 = food_quantity * 71
                      
                        print(calories_intake_1)
                       
                        calories_intake.update({Breakfast_food  :calories_intake_1 })
                    
                    elif (Breakfast_food == "pongal"):
                      
                        calories_intake_1 = food_quantity * 212
                       
                        print(calories_intake_1)
                       
                        calories_intake.update({Breakfast_food :calories_intake_1 })
                      
            
            elif (food_time == 'lunch'):
                print("\n""Keep calm and eat lunch" "\n")
                lunch_count = int(input("enter number of items you had lunch:"))
                for l in range(lunch_count):
                    lunch_food = input("enter the lunch item name:").lower()
                    food_quantity =int( input("enter your lunch item quantity:"))
                    if (lunch_food == "sambar rice"):
                      
                        calories_intake_2 = food_quantity * 258.5
                       
                        print(calories_intake_2)
                      
                        calories_intake.update({lunch_food :calories_intake_2 })
                        
                    elif (lunch_food == "dhal rice"):
                       
                       calories_intake_2 = food_quantity * 236
                      
                       print(calories_intake_2)
                      
                       calories_intake.update({lunch_food :calories_intake_2 })
                     
                    elif (lunch_food == "vegetable rice"):
                     
                       calories_intake_2 = food_quantity * 241
                     
                       print(calories_intake_2)
                    
                       calories_intake.update({lunch_food :calories_intake_2 })
                      
            
            elif (food_time == 'dinner'):
                print("\n""Eat breakfast like a king,lunch like a prince, and dinner like a pauper"'\n')
                dinner_count = int(input("enter number of items you take in dinner:"))
                for d in range(dinner_count):
                    dinner_food = input("enter the dinner item name:").lower()
                    food_quantity =int( input("enter your dinner item quantity:"))
                    if (dinner_food == "dosa"):
                       
                        calories_intake_3 = food_quantity * 133
                       
                        print(calories_intake_3)
                        
                        calories_intake.update({dinner_food :calories_intake_3 })
                       
                    elif (dinner_food == "poori"):
                       
                        calories_intake_3 = food_quantity * 101
                        
                        print(calories_intake_3)
                    
                        calories_intake.update({dinner_food :calories_intake_3 })
                        
                    elif (dinner_food =="Noodles"):
                      
                        calories_intake_3 = food_quantity * 138
                    
                        print(calories_intake_3) 
                        
                        calories_intake.update({dinner_food :calories_intake_3 })
                        
            
            elif (food_time == 'snacks'):
                print("\n""Fruits are snacks,which are rich in vitamins,and can be eaten the whole day""\n")
                snacks_count = int(input("enter number of items you take in snacks:"))
                for s in range(snacks_count):
                    snacks_item = input("enter the snacks item name:").lower()  
                    food_quantity =int( input("enter your snacks item quantity:"))
                    if (snacks_item  == "milk"):
                       
                       calories_intake_4 = food_quantity * 42
                       
                       print(calories_intake_4)
                       
                       calories_intake.update({snacks_item :calories_intake_4 })
                       
                    elif (snacks_item  == "sundal"):
                       
                       calories_intake_4 = food_quantity * 111
                       
                       print(calories_intake_4)
                      
                       calories_intake.update({snacks_item:calories_intake_4 })
                      
                    elif (snacks_item  =="corn"):
                       
                       calories_intake_4 = food_quantity * 86
                       
                       print(calories_intake_4)
                       
                       calories_intake.update({snacks_item :calories_intake_4 })
                       
    else:
        activities(health)
    Total_Calories_intake = []
    for j in calories_intake.values():
        Total_Calories_intake.append(j)
    global Intake_calories
    
    Intake_calories =sum(Total_Calories_intake)    
    print("\n""calories_in:", calories_intake ,"\n")
    print("total intaking calories by taking a food:", Intake_calories)

health = input("enter your choice:")
food(health)

def activities(health):
    if(health == 'fitness'):
        print("\n""Exercise not only changes your body, it changes your mind, your attitude and your mood."'\n')
        for i in range(0,2):
            activity_time = input("enter the time(morning or evening):")
            if (activity_time == "morning"):
                morning_count = int(input("enter number of activites you done in the Morning:"))
                for j in range(morning_count):
                    activity_type= input("enter your morning activity type:")
                    if (activity_type == "running"):
                        hours = int(input("enter how many hours you run in the morning:"))
                       
                        calories_burn_m1 =  8*3.5*weight*60*hours /200
                        print(calories_burn_m1)
                        calories_burn.update({activity_type : calories_burn_m1})
                    if(activity_type == "cycling"):
                        hours= int(input("enter how many hours you do cycling in the morning:"))
                       
                        calories_burn_m2 =  5.3*3.5*weight*60*hours /200
                        print(calories_burn_m2)
                        calories_burn.update({activity_type : calories_burn_m2})
                    if(activity_type == "jogging"):
                        hours = int(input("enter how many hours you do jogging in the morning:"))
                        
                        calories_burn_m3 = 7*3.5*weight*60*hours /200
                        print(calories_burn_m3) 
                        calories_burn.update({activity_type : calories_burn_m3})
                    if(activity_type == "dancing"):
                        hours = int(input("enter how many hours you play sports in the morning:"))
                       
                        calories_burn_m4 = 4.5*3.5*weight*60*hours /200
                        print(calories_burn_m4)
                        calories_burn.update({activity_type : calories_burn_m4})
                    if(activity_type == "yoga"):
                        hours = int(input("enter how many hours you do yoga in the morning:"))
                        
                        calories_burn_m5 =3*3.5*weight*60*hours /200
                        print(calories_burn_m5)
                        calories_burn.update({activity_type : calories_burn_m5})
                    if(activity_type == "meditation"):
                        hours = int(input("enter how many hours you do meditation in the morning:"))
                        calories_burn_m6 = 3*3.5*weight*60*hours /200
                        print(calories_burn_m6)
                        calories_burn.update({activity_type : calories_burn_m6})
                    if(activity_type == "exercise"):
                        hours = int(input("enter how many hours you do exercise in the morning:"))
                        
                        calories_burn_m7 = 8*3.5*weight*60*hours /200
                        print(calories_burn_m7)
                        calories_burn.update({activity_type : calories_burn_m7})
                
                
            elif (activity_time == "evening"):
                evening_count = int(input("enter number of activites you done in the evening:"))
                for j in range(evening_count):
                    activity_type= input("enter your evening activity type:")
                    if (activity_type == "running"):
                        hours = int(input("enter how many hours you run in the Evening:"))
                        
                        calories_burn_e1 = 8*3.5*weight*60*hours /200
                        print(calories_burn_e1)
                        calories_burn.update({activity_type : calories_burn_e1})
                    if(activity_type == "cycling"):
                        hours = int(input("enter how many hours you do cycling in the Evening:"))
                        
                        calories_burn_e2 = 5.3*3.5*weight*60*hours /200
                        print(calories_burn_e2)
                        calories_burn.update({activity_type : calories_burn_e2})
                    if(activity_type == "jogging"):
                        hours = int(input("enter how many hours you do jogging in the Evening:"))
        
                        calories_burn_e3 = 7*3.5*weight*60*hours /200
                        print(calories_burn_e3)
                        calories_burn.update({activity_type : calories_burn_e3})
                    if(activity_type == "dancing"):
                        hours = int(input("enter how many hours you play sports in the Evening:"))
                        
                        calories_burn_e4 = 4.5*3.5*weight*60*hours /200
                        print(calories_burn_e4)
                        calories_burn.update({activity_type : calories_burn_e4})
                    if(activity_type == "yoga"):
                        hours = int(input("enter how many hours you do yoga in the Evening:"))
                        
                        calories_burn_e5 = 3*3.5*weight*60*hours /200
                        print(calories_burn_e5)
                        calories_burn.update({activity_type : calories_burn_e5})
                    if(activity_type == "meditation"):
                         hours = int(input("enter how many hours you do meditation in the Evening:"))
                         
                         calories_burn_e6 = 3*3.5*weight*60*hours /200
                         print(calories_burn_e6)
                         calories_burn.update({activity_type : calories_burn_e6})
                    if(activity_type == "exercise"):
                         hours = int(input("enter how many hours you do exercise in the Evening:"))
                         
                         calories_burn_e7 = 8*3.5*weight*60*hours /200
                         print(calories_burn_e7)
                         calories_burn.update({activity_type : calories_burn_e7})
                         
            else:
                work_in(health)           
           
            Total_Calories_burn = []
            for j in calories_burn.values():
                Total_Calories_burn.append(j)
            global Burn_calories
            Burn_calories = sum(Total_Calories_burn)    
        print("calories_out:", calories_burn , "\n")
        print("total burn calories by doing physical activities:", Burn_calories)                
    
health = input("enter your choice:")
activities(health)

work_rate = 0
sleep_rate = 0
def work_in(health):     
    health=input("enter your choice:")
    if(health == 'work'):
        print("\n""Don’t judge each day by the harvest you reap but by the seeds that you plant.""\n")
        no_of_works = int(input("enter no of works they did:"))
        for n in range(no_of_works): 
            work_name = input("what work are you done?")
            hours = int(input("how many hours do you spend:"))
            work.update({work_name : hours})
    
    print(work)
    sleep_rate = work['sleep']
    print(sleep_rate)
    if(sleep_rate == 8):               
        print("you had a good sleep")
    elif (sleep_rate < 8):
        print("you need to take some more hours sleep for next day" )    
    else:
        print("you took more sleeping hour, you want to reduce some hours for next day") 
    total_hours = []
    for w in work.values():
        total_hours.append(w)
    global work_hours    
    work_hours = sum(total_hours)
    print("\n""total_work_hours = " , work_hours,"\n")
    work_rate = work_hours - sleep_rate 
    print("working rate:", work_rate)
    if(work_rate >12):
        print("you need to spend some time for relax yourself ")
    else:
        print("Great!!! keep doing")    
       
    if (work_hours > 24):
        print("Enter proper work hours!!! It is exceeded than 24 hours")
        work_in(health)
    else:
        print("Good work split!! keep doing")
work_in(health)

def finance(health):
    if(health == "finance"):
        print("\n""Beware of little expenses; a small leak will sink a great ship""\n")
        category = int(input("No of category that you want to enter?"))
        for l in range(category):
            category_name = input("Mention the category that you spend in:")
            amount_spend = int(input("enter the amount that spend:"))
            expenditure.update({category_name: amount_spend})
            
        total_amount=[]
        for a in expenditure.values():
            total_amount.append(a)
        global total_expen
        total_expen = sum(total_amount)
        print("\n""Total expenditure that he/she spends in a day", total_expen,"\n")
        print("Remaining balance is ", daily_income - total_expen,"\n" )
        
health = input("enter your choice:")        
finance(health)
        
def Calories():
    food_calories = Intake_calories
    activity_colories = Burn_calories
    daily_left = Intake_calories - Burn_calories
    print("daily_left_calories:", daily_left,"\n")
    if (daily_left == 0):
        print("Good job!! you maintained your health properly, keep doing")
    elif (daily_left > 0):
        print("*****You have to do some more activities to maintain your calories**")
    else:
        print("@@@ You need to take some more healthy foods @@@")
    
Calories()    
   
       
print("THANK YOU" "\U0001263A" "\n""\n" "To ensure good health: eat lightly, breathe deeply, live moderately, cultivate cheerfulness, and maintain an interest in life.")