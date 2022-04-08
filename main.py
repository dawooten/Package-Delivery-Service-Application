# Derek Wooten 000897998

import package
import distance

# looping function to find distance between packages on trucks
# Nearest Neighbor Algorithm
# space-time complexity O(N^2)
def truck_route(truck, truck_start_time):

    # get initial starting location and set initial variables
    truck_index = distance.DistanceTable.address_lookup["4001 South 700 E"]
    minimum = 0.0
    en_route_status = "en route"
    delivered_status = "Delivered"
    min_pkg_id = 0
    truck_distance = 0.0
    actual_time = truck_start_time
    run = 0

    # update all packages' status on truck to en route
    for i in truck:
        pkg = package.myHash.lookup(i)
        pkg.status = en_route_status

    # use while there are packages on the truck
    while len(truck) > 0:
        run = 0
        min_pkg_id = 0
        minimum = 0.0

        # loop through the packages on truck to find next closest package to current location
        for i in truck:
            pkg = package.myHash.lookup(i)

            # add 1 to run for every loop through the packages
            run += 1

            if pkg is not None:

                # get the address
                pkg_address = pkg.address

                # get the list index for the address
                package_index = distance.DistanceTable.address_lookup[pkg_address]

                # find distance from starting point for all packages
                distance_between_packages = distance.DistanceTable.listofdistances[truck_index][package_index]

                # making the first distance the starting minimum value
                if run == 1:
                    minimum = distance_between_packages
                    min_pkg_id = pkg.packageid

                # update the minimum value when necessary
                if distance_between_packages < minimum:
                    minimum = distance_between_packages
                    min_pkg_id = pkg.packageid

        # add min. distance to total
        truck_distance += minimum

        # time truck traveled in hours (psuedo time)
        time_traveled = minimum / 18.0
        actual_time += time_traveled
        time_hour = int(actual_time)
        if time_hour < 10:
            time_minute = int((actual_time - float(time_hour)) * 60)
            time_hour = str("0" + str(time_hour))
            if time_minute < 10:
                time_minute = str(time_minute)
                time_minute = str("0" + time_minute)
                timestamp = (time_hour + ":" + time_minute + ":00")
            else:
                time_minute = str(int((actual_time - float(time_hour)) * 60))
                timestamp = (time_hour + ":" + time_minute + ":00")
        else:
            time_hour = str(int(actual_time))
            time_minute = int((actual_time - float(time_hour)) * 60)
            if time_minute < 10:
                time_minute = str(time_minute)
                time_minute = str("0" + time_minute)
                timestamp = (time_hour + ":" + time_minute + ":00")
            else:
                time_minute = str(int((actual_time - float(time_hour)) * 60))
                timestamp = (time_hour + ":" + time_minute + ":00")

        # timestamping the package
        pkg = package.myHash.lookup(min_pkg_id)
        pkg.timestamp = timestamp

        #update package status to delivered
        pkg = package.myHash.lookup(min_pkg_id)
        pkg.status = delivered_status

        # set current location for the next loop
        truck_index = distance.DistanceTable.address_lookup[package.myHash.lookup(min_pkg_id).address]

        # remove pkg from truck
        truck.remove(min_pkg_id)

    # truck returns to hub after all packages are delivered and updates total distance for truck
    # get truck to the hub
    hub_index = distance.DistanceTable.address_lookup["4001 South 700 E"]
    distance_to_hub = distance.DistanceTable.listofdistances[truck_index][hub_index]
    truck_distance += distance_to_hub
    return truck_distance

# loading of trucks
truck1 = [15, 16, 34, 14, 13, 39, 20, 21, 27, 35, 40, 1]
truck2 = [3, 18, 36, 38, 37, 5, 6, 25, 26, 29, 7, 30, 8, 31, 32]
truck3 = [4, 28, 2, 33, 9, 10, 11, 12, 17, 19, 22, 23, 24]

# computing total truck distance traveled by calling truck function
truck1_distance = truck_route(truck1, 8.0)
truck2_distance = truck_route(truck2, 9.083)
truck3_distance = truck_route(truck3, 10.33)
total_distance_traveled = truck1_distance + truck2_distance + truck3_distance

# command line interface at the start of the program
print('*******************************************')
print('Welcome to the WGUPS Routing Program')
print('*******************************************\n')

# printout of individual truck distances and total distances of all trucks
print(f"Truck 1 Distance: {truck1_distance:.1f}\n"
        f"Truck 2 Distance: {truck2_distance:.1f}\n"
        f"Truck 3 Distance: {truck3_distance:.1f}\n"
        f"Total Distance: {total_distance_traveled:.1f}\n")

# print(package.myHash.lookup(1).packageid)
# print(package.myHash.lookup(1).address)
# print(package.myHash.lookup(3).timestamp)
# print(package.myHash.lookup(9).timestamp)
# print(package.myHash.lookup(40).timestamp)
# print(package.myHash.lookup(29).timestamp)
# print(package.myHash.lookup(1).status)
# print(package.myHash.lookup(15).status)
# print(package.myHash.lookup(4).status)
# print(package.myHash.lookup(22).status)
# print(package.myHash.lookup(36).status)

# have user select which option they want to use
user_input = input("Select '1' or '2' to begin program or type 'quit' to quit:\n"
                   "1. Gather information for all packages at a certain time\n"
                   "2. Gather information for one package at a certain time\n")

# after user selects 1, 2, or quit
while user_input != 'quit':

    # if user selects 1 and enters a specific time
    # space-time complexity O(N)
    if user_input == '1':
        try:
            user_time_input = input('Please enter a time in (HH:MM:SS) format: ')

            # loop through packages 1-40 to lookup each package's start time and delivery time
            # and prints out each package with the status at the time entered
            # space-time complexity O(N)
            for i in range(1, 41):
                try:
                    time_1 = package.myHash.lookup(i).start_time
                    time_2 = package.myHash.lookup(i).timestamp

                except ValueError:
                    pass
                # used if package is still at the hub at the time entered and when the package will leave
                # prints out package id and delivery status
                if time_1 >= user_time_input:
                    package.myHash.lookup(i).status = "At the hub"
                    package.myHash.lookup(i).notes = "Package leaves at " + time_1

                    print(f'Package ID: {package.myHash.lookup(i).packageid}, '
                          f'Delivery Status: {package.myHash.lookup(i).status}')

                # used if package is en route at the time entered and when the package left
                # prints out package id and delivery status
                elif time_1 <= user_time_input:
                    if user_time_input < time_2:
                        package.myHash.lookup(i).status = "En Route"
                        package.myHash.lookup(i).notes = "Package left at " + time_1

                        print(f'Package ID: {package.myHash.lookup(i).packageid}, '
                              f'Delivery Status: {package.myHash.lookup(i).status}')

                    # used if package has been delivered at the time entered and when package left
                    # prints out package id and delivery status
                    else:
                        package.myHash.lookup(i).status = "Delivered at " + time_2
                        package.myHash.lookup(i).notes = "Package left at " + time_1

                        print(f'Package ID: {package.myHash.lookup(i).packageid}, '
                              f'Delivery Status: {package.myHash.lookup(i).status}')
            exit()

        except IndexError:
            print(IndexError)
            exit()
        except ValueError:
            print("Please use the correct format")
            exit()

    # if user selects 1 and enters a specific package id and time
    # and prints out the package id, address, deadline, city, zip code, weight, status,
    # and delivery time
    # space-time complexity O(N)
    elif user_input == '2':
        try:
            i = int(input("Please enter a Package ID (1-40): "))
            time_1 = package.myHash.lookup(i).start_time
            time_2 = package.myHash.lookup(i).timestamp
            user_time_input = input("Please enter a time in (HH:MM:SS) format: ")

            # prints package info if package is still at the hub at time entered
            if time_1 >= user_time_input:
                package.myHash.lookup(i).status = "At the hub"
                package.myHash.lookup(i).start_time = "Package leaves at " + time_1

                print(f'Package ID: {package.myHash.lookup(i).packageid}\n'
                      f'Address: {package.myHash.lookup(i).address}\n'
                      f'Delivery Deadline: {package.myHash.lookup(i).deadline}\n'
                      f'City: {package.myHash.lookup(i).city}\n'
                      f'Zip Code: {package.myHash.lookup(i).zipcode}\n'
                      f'Package Weight: {package.myHash.lookup(i).weight}\n'
                      f'Delivery Status: {package.myHash.lookup(i).status}, '
                      f'will be delivered at {package.myHash.lookup(i).timestamp}\n')
                exit()

            # prints package info if package is en route at time entered
            elif time_1 <= user_time_input:
                if user_time_input < time_2:
                    package.myHash.lookup(i).status = "En Route"
                    package.myHash.lookup(i).start_time = "Package left at " + time_1

                    print(f'Package ID: {package.myHash.lookup(i).packageid}\n'
                          f'Address: {package.myHash.lookup(i).address}\n'
                          f'Delivery Deadline: {package.myHash.lookup(i).deadline}\n'
                          f'City: {package.myHash.lookup(i).city}\n'
                          f'Zip Code: {package.myHash.lookup(i).zipcode}\n'
                          f'Package Weight: {package.myHash.lookup(i).weight}\n'
                          f'Delivery Status: {package.myHash.lookup(i).status}, '
                          f'will be delivered at {package.myHash.lookup(i).timestamp}\n')
                    exit()
                # prints package info if package is delivered at time entered
                else:
                    package.myHash.lookup(i).status = "Delivered at " + time_2
                    package.myHash.lookup(i).start_time = "Package left at " + time_1

                    print(f'Package ID: {package.myHash.lookup(i).packageid}\n'
                         f'Address: {package.myHash.lookup(i).address}\n'
                         f'Delivery Deadline: {package.myHash.lookup(i).deadline}\n'
                         f'City: {package.myHash.lookup(i).city}\n'
                         f'Zip Code: {package.myHash.lookup(i).zipcode}\n'
                         f'Package Weight: {package.myHash.lookup(i).weight}\n'
                         f'Delivery Status: {package.myHash.lookup(i).status}')
                    exit()

        except ValueError:
            print("Please use the correct format")
            exit()

    elif user_input == 'quit':
        exit()

    else:
        print("Error! Please use 1, 2, or 'quit'.")
        exit()



















