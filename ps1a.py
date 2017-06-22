###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name: Trinh Trung Dung
# Time: 6 hours

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================


def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    with open(filename) as file:
        read_data = file.read().split("\n")
        mapping_cow_weight = {}
        for data in read_data:
            cow, weight = data.split(",")
            weight = int(weight)
            mapping_cow_weight[cow] = weight
    file.close()
    return mapping_cow_weight


def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    trips = []
    duplicate_cows = dict(cows)
    for j in range(len(cows)):
        if len(duplicate_cows) != 0:
            x = []
            fit = []
            temp_limit = limit
            max1 = max(duplicate_cows.values())
            temp_limit -= max1
            name = list(duplicate_cows.keys())[list(duplicate_cows.values()).index(max1)]
            del duplicate_cows[name]
            x.append(name)
            for k in duplicate_cows:
                if temp_limit >= duplicate_cows[k]:
                    fit.append(duplicate_cows[k])
            if len(fit) == 0:
                trips.append(x)
                continue
            else:
                for c in fit:
                    max2 = max(fit)
                    if temp_limit - max2 >= 0:
                        temp_limit -= max2
                        name2 = list(duplicate_cows.keys())[list(duplicate_cows.values()).index(max2)]
                        x.append(name2)
                        del duplicate_cows[name2]
                    else:
                        continue
            trips.append(x)
    return trips


def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
     # generating a list contains all possible partitions of cows
    possible_partitions = list(get_partitions(cows.keys()))
    # sorting list by the length of all partitions
    possible_partitions.sort(key=len)
    # initializing the desired list of lists that has the fewest trips
    result_partition = possible_partitions[0]
    # iterating through each possible partition
    for partition in possible_partitions:
        # initializing the empty list which will contain the weight of each trip in a partition and satisfy the required limits
        # e.g. partition = [[1,2,3,4],[5]] <=> trip_weights = [10, 5] with default limit => this is result partition
        # e.g. partition = [[1,2,3],[4,5,6]] <=> trip_weights = [] with default limit cause sum of [4,5,6] > limit
        trip_weights = []
        for trips in partition:
            weight = 0
            for trip in trips:
                weight += cows[trip]
            if weight > limit:
                break
            else:
                trip_weights.append(weight)
        # this condition will immediately return the first desired partition in the possible partitions list
        if len(trip_weights) != 0 and len(trip_weights) == len(partition):
            result_partition = partition
            break
    return result_partition
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # starting time for measuring greedy_cow_transport function
    startGreedy = time.time()
    greedy_cow_transport(load_cows("ps1_cow_data.txt"))
    # end point of measuring greedy_cow_transport function
    endGreedy = time.time()
    # output the time that needs to run greedy_cow_transport and its partition
    print("Greedy algorithm measured: ", endGreedy - startGreedy)
    print(greedy_cow_transport(load_cows("ps1_cow_data.txt")))
    
    # starting time for measuring brute_force_cow_transport function
    startBruteForce = time.time()
    brute_force_cow_transport(load_cows("ps1_cow_data.txt"))
    # end point of measuring brute_force_cow_transport function
    endBruteForce = time.time()
    # output the time that needs to run brute_force_cow_transport and its partition
    print("Brute force algorithm measured: ", endBruteForce - startBruteForce)
    print(brute_force_cow_transport(load_cows("ps1_cow_data.txt")))
