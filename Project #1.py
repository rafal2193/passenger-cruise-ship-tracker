#Rafal Krauze
#June 15,2024
#CMP 131
#Project #1 consited of creating a code for a cruise ship application that prints customized activity list for passsengers based on their age.
#I hereby attest that this code is original and written by me alone. I understand that I risk a penalty for violating the Academic Integrity policy at CCM





#Enter name into crusie ship database 
full_name = input("Enter passenger name: ")

#Enter age to see what activities you are allowed to participate in
age = int(input("Enter passenger age: "))

#Set initial flag over21 to False
over21 = False

# Determine passenger category based on age
#Passengers  12 or under are considered a child on the cruise
if age <= 12:
    passenger_category = "Child"


#Passengers between the ages of 18-20 are considered a young adult on the cruise
elif age >= 18 and age <= 20:
    passenger_category = "Young Adult"

#Passengers between the ages of 13-19 are considered a teenager on the cruise
elif age >= 13 and age <= 19:
    passenger_category = "Teenager"    

#Passengers 65 or older are considered senior on the cruise     
elif age >= 65:
    passenger_category = "Senior"
    over21= True

#Passengers 21 or older are considered adults on the cruise 
else: 
    passenger_category = "Adult"
    over21=True



#Determine activities based on passenger category
#Will demonstrate what activities a child can participate in
# Using \n to start a new line. this will help keep the output organized
#Covered it in my Rutgers coding bootcamp
if passenger_category == "Child":
   print(f'All children ages 12 and under can enjoy the following activities:\n'
             f'Kids Club\n'
             f'Spalsh Zone\n'
          f'Enjoy your cruise!')
#Will demonstrate what activites a teenager can participate in     
elif passenger_category == "Teenager":
     print(f'All teenagers ages 13-19 can enjoy the following activites:\n'
           f'Teen Club\n'
           f'Water Slides\n'
           f'Enjoy your cruise!\n')


#Will demonstrate what activites a young adult can partcipate in 
elif passenger_category == "Young Adult":
     print(f'All teenagers ages 13-19 can enjoy the following activites:\n'
           f'Teen Club\n'
           f'Water Slides\n'
           f'All 18,19,and 20 year old passengers may also participate in:\n'
           f'Dance Club\n'
           f'Comedy Club\n'
           f'Adult Pool\n'
           f'Enjoy your cruise!\n')
           


    

#Will demonstrate what actvities a adult can particiapte in 
elif passenger_category == "Adult":
     print(f'All adults can enjoy the following activities:\n'
           f'Dance Club\n'
           f'Comedy Club\n'
           f'Adult Pool\n'
           f'All bars and casinos\n'

           f'As a reminder please drink responsibly!\n'
           f'Enjoy your cruise!\n')

           

#Will demonstrate what activites a senior can participate in 
elif passenger_category == "Senior":
     print(f'All adults can enjoy the following activites:\n'
           f'Dance Club\n'
           f'Comedy Club\n'
           f'Adult Pool\n'
           f'All bars and casinos\n'
           f'Senior cruisers are entitled to a 15% purchase discount on board\n'

           f'As a reminder please drink responsibly!\n'
           f'Enjoy your cruise!\n')
        


