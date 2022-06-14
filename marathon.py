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
#    DESCRIPTION: {Your Description Here}
#
#  *****************************************************************************

def fitness():
    pass
keep_looping=True
while keep_looping == True:
  print("Tokyo Marathon Qualifier")
  runner_name=input("Please Enter Your Name:")
  miles_in_10min=float(input("How many miles can you run in 10 minutes?"))
  savings=float(input("How much U.S$ do you have saved for the marathon?"))
  #miles to kilometers
  meters_in_mile=1609.34
  one_kilometer=1000
  mile_kilometer=meters_in_mile / one_kilometer
  #print(mile_kilometer)
  miles_to_kilometers=miles_in_10min * mile_kilometer
  #print(miles_to_kilometers)
  kilometers_per_min= miles_to_kilometers / 10
  pace=(round(kilometers_per_min,2))
  #print(pace)
  #U.S $ to Japanese Yen
  japanese_Yen= 134.28
  dollars_to_yens= savings * japanese_Yen
  #print(dollars_to_yens)
  lastname=runner_name.find(" ")
  #print(lastname)
  #print(runner_name[lastname:])
  print(f"Dear{runner_name[lastname:]}, you have a pace of {pace} km/min.")
  print(f"Additionally, you only have {dollars_to_yens}¥ to spend.")
  question=input("Would you like to try again (Y/N)?")
  if question == "Y":
     keep_looping=True
  if question == "N":
    keep_looping=False
  print()
  if __name__ == "__main__":
      fitness()
