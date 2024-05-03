from collections import defaultdict

parking_space = defaultdict(int)
parking_space[1]="as21f853"
parking_space[18]="mn12345"
parking_space[15] ="388hafd"
print(parking_space)
def draw_space(parking_space):
    count = 1
    for i in range(1, 2):
        for j in range(1, 21):
            if parking_space[count] == 0:
                print("  0^0", end ="")
                print("_", end ="|")
            else:
                print("X", end ="")
                print("_", end ="|")
            count+=1
        print()

draw_space(parking_space)
                


while True:
    print("Would you like to park your car or take your car:")
    print("1.Parking\n2.Checkout")
    opt = int(input())
    if opt==1:
        available_space = []
        for i in range(1,21):
            if parking_space[i]== 0:
                available_space.append(i)
        if available_space ==[]:
            print("Sorry we dont have any available spaces")
            break

        else:
            print("The available spaces are")
            print(available_space)
        
        while True:
            space_opt = int(input("Please select one of the spots: "))
            if space_opt in available_space:
                break
            else:
                print("Sorry we dont have this slot available, try somewhere else")
        car_number = input("Please Enter your car number: ")
        parking_space[space_opt]=car_number
        print(f"Your car has been parked in slot {space_opt}")
        
    elif opt == 2:
        print("Welcome back, your car is safely parked here")
        while True:

            car_no = input("Please enter your car number: ")
            if car_no in parking_space.values():
                for slot, car  in parking_space.items():
                    if car==car_no:
                        parking_space[slot] =0
                print("Thank you for parking in our space, visit us again")
                break
            else:
                print("Sorry we couldn't find your car, pherhaps your entered the plate number wrong")
    
    else:
        break
