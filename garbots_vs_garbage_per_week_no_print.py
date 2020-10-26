import matplotlib.pyplot as plt

def main():

    #variables
    garbage = 0
    garbage_max = 0
    garbage_values = []
    #garbage_values[0] = 0
    resources = 0
    garbots = 1
    garbots_time = []
    run = 1
    week = 1

    print("HOW LONG TO CLEAN THE PLANET??\n")
    garbage_rate = int(input("Please enter the garbage added per week.\n"))
    garbot_collection_rate = int(input("Please enter the Garbot collection rate per week.\n"))
    garbot_cost = int(input("Please enter the cost of a Garbot in resource units.\n"))
    print("__________________________________________________________________\n")                   
    
    while(run == 1):

        #add garbage
        garbage = garbage + garbage_rate

        #garbage max
        if garbage > garbage_max:
                garbage_max = garbage
                
        #print("______________________________________________________________\n")
        #print("Week:", week, "\n")
        #print("GARBAGE DROP!\n")
        #print("There are", garbage, "cubic meters of garbage now on the planet.\n")

        #add garbots
        #print("There are", garbots, "Garbots on the team.\n")
        #print("There are", resources, "resource units available in stock.\n")
        more_garbots = int(resources/garbot_cost)
        #print("Adding", more_garbots, "Garbots to the team from resource units.\n")
        resources = int(resources%garbot_cost)
        #print(resources, "resource units remaining.\n")
        garbots = garbots + more_garbots

        #convert garbage to resources with garbots
        less_garbage = garbots * (garbot_collection_rate)
        garbage = garbage - less_garbage
        resources = resources + less_garbage
        #print(less_garbage, "cubic meters converted from garbage to resources.\n")
        #print("There are", garbage, "cubic meters of garbage left on the planet this week.\n")

        garbage_values.append(garbage)
        garbots_time.append(garbots)
        
        #check if garbage reduced to zero
        if garbage <= 0:
            run = 0
            print("weeks to reduce garbage to zero:", week)
            print("garbots on the team:", garbots)
            print("The maximum garbage accumulated on the planet was:", max(garbage_values), "cubic meters")

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
