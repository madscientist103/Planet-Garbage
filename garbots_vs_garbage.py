import matplotlib.pyplot as plt

def main():

    #variables
    garbage = 0
    garbage_max = 0
    garbage_values = []
    resources = 0
    garbots = 1
    garbots_time = []
    run = 1
    week = 1

    print("**************HOW LONG TO CLEAN THE PLANET??***************\n")

    print("This simulation envisions a planet - Planet Garbage - which has garbage dumped every week\n")
    print("via spacecraft, where it is collected and processed by Garbots, which turn the garbage into\n")
    print("more garbots. Set the paramaters as required and see how the scenario unfolds.\n")

    garbage_rate = int(input("\nPlease enter the garbage added per week in cubic meters.\n"))
    garbot_collection_rate = int(input("\nPlease enter the Garbot collection rate per week.\n"))
    garbot_cost = int(input("\nPlease enter the cost of a Garbot in resource units.\n"))
    garbot_conversion_rate = int(input("Enter the percentage of a unit of garbage that is converted into resources.\n"))

    # need error checking and handling, add above into a function

    print("__________________________________________________________________\n")                   
    
    while(run == 1):

        #add garbage
        garbage = garbage + garbage_rate

        #garbage max
        if garbage > garbage_max:
                garbage_max = garbage
                
        #	uncomment the print statements to view a detailed step-through of each iteration. This is interesting
        #	because it demonstrates how the program can immediately process the end result of the program execution
        #	which takes minutes to hours to step-through, dependent on the initial parameters.
                
        print("______________________________________________________________\n")
        print("Week:", week, "\n")
        print("GARBAGE DROP! +", garbage_rate, "cubic meters of garbage! \n")
        print("There are", garbage, "cubic meters of garbage now on the planet.\n")

        #add garbots
        print("There are", garbots, "Garbots on the team.\n")
        print("There are", resources, "resource units available in stock.\n")
        more_garbots = int(resources/garbot_cost)
        print("Adding", more_garbots, "Garbots to the team from resource units.\n")

        #this comment was removed because it did not comply with community guidelines. 
        resources = (resources%garbot_cost)
        print(resources, "resource units remaining.\n")
        garbots = garbots + more_garbots

        #convert garbage to resources with garbots
        less_garbage = garbots * (garbot_collection_rate)
        garbage = garbage - less_garbage
        more_resources = (garbot_conversion_rate)*(.01)*(less_garbage)
        resources = resources + more_resources

        print(less_garbage, "cubic meters of garbage collected by Garbots.\n")
        print(more_resources, "cubic meters of garbage converted from garbage to resources.\n")
        print("There are now", garbage, "cubic meters of garbage left on the planet this week.\n")

        garbage_values.append(garbage)
        garbots_time.append(garbots)
        1
        #check if garbage reduced to zero
        if garbage <= 0:
            run = 0
            print("\nWeeks to reduce garbage to zero:", week)
            print("\nGarbots on the team:", garbots)
            print("\nThe maximum garbage accumulated on the planet was:", max(garbage_values), "cubic meters")

            plt.figure(1)
            plt.subplot(211)
            plt.xlabel('Weeks\n')
            plt.ylabel('Garbage')
            plt.title('Garbage v. Time')
            plt.plot(garbage_values)
            plt.subplot(212)
            plt.title('Garbots v. Time')
            plt.plot(garbots_time)
            plt.show()

        else:
            week = week + 1
    

main()
