# """
#  *****************************************************************************
#    FILE:        marathon.py
#
#    AUTHOR:      {Fatima Carolina Cortinas}
#
#    ASSIGNMENT: A marathon calculator to determine if a U.S. participant can
#    run in the Tokyo Marathon. 
#
#    DATE:         {06/12/2022}
#
#    DESCRIPTION: {#Print a welcome statement to the user. #Ask the user for their name (first and last). #Ask the user how many miles they can run in 10 minutes. #Ask the user how much U.S $ they have saved for the marathon. #Print a statement where it says the last name that the user input, their pace (miles to kilometers) per minute and how much ¥ they have to spend. #add a while loop so that the user cant try again. #Round the kilometers of the output to the nearest 10th.}
#
#  *****************************************************************************
METER_IN_MILE=1609.34
M_IN_KM=1000
JAPANESE_YEN= 134.28

def fitness():
    
    #Collecting input from user
    print("Tokyo Marathon Qualifier")
    runner_name=input("Please Enter Your Name: ")
    miles_in_10min=float(input("How many miles can you run in 10 minutes? "))
    us_savings=input("How much U.S$ do you have saved for the marathon? ")
    # savings=float(input("How much U.S$ do you have saved for the marathon? ")[1:])
    us_savings_index=us_savings[1:]
    us_saving_into_float=float(us_savings_index)
    
    #miles to kilometers, 
    km_in_a_mile= METER_IN_MILE/M_IN_KM
    miles_to_kilometers=miles_in_10min * km_in_a_mile
    kilometers_per_min= miles_to_kilometers / 10
    pace=(kilometers_per_min)
    
    #Calculating conversions between dollars and yens
    dollars_to_yens= (us_saving_into_float * JAPANESE_YEN)
    lastname=runner_name.find(" ")
    
    print()
    print(f"Dear{runner_name[lastname:]}, you have a pace of {pace:.2f} km/min.")
    print(f"Additionally, you only have {dollars_to_yens:.2f}¥ to spend.")
    
if __name__ == "__main__":
    fitness()
