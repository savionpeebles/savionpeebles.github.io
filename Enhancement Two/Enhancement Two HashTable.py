#Savion Peebles
#Professor Alesso
#CS-499
#11/22/2024



# imported tools
from enum import Enum
import math

class csv: #this class replaces the original namespace 'csv'
    class Error(RuntimeError):

        def __init__(self, msg):
            super().__init__(str("CSVparser : ").append(msg))

    class Row:


        def getValue(self, pos):
            if pos < len(self._values):
                res = None
                ss = std.stringstream()
                ss << self._values[pos]
                ss >> res
                return res
            raise Error("can't return this value (doesn't exist)")

    class DataType(Enum):
        EFILE = 0
        EPURE = 1

    class Parser:
            pass


# define a structure to hold bid information
class Bid:
    def __init__(self):

        self.bidId = ""
        self.title = ""
        self.fund = ""
        self.amount = 0

        self.amount = 0.0


# Hash Table class definition

#*
# * Define a class containing data members and methods to
# * implement a hash table with chaining.
#
class HashTable:

    def _initialize_instance_fields(self):

        self._nodes = []
        self._tableSize = Globals.DEFAULT_SIZE



    class Node:

        def _initialize_instance_fields(self):

            self.bid = Bid()
            self.key = 0
            self.next = None




        def __init__(self):
            self._initialize_instance_fields()

            self.key = numeric_limits.max()
            self.next = None

        #initialize with a bid

        def __init__(self, aBid):
            self._initialize_instance_fields()

            self()

            self.bid.copy_from(aBid)

        #initialize with a bid and a key

        def __init__(self, aBid, aKey):
            self._initialize_instance_fields()

            self(aBid)
            self.key = aKey




    #*
    # * Calculate the hash value of a given key.
    # * Note that key is specifically defined as
    # * unsigned int to prevent undefined results
    # * of a negative list index.
    # *
    # * @param key The key to hash
    # * @return The calculated hash
    #
    def _hash(self, key):

        return int(math.fmod(key, self._tableSize))


    #*
    # * default funtion initialization
    #

    def __init__(self):
        self._initialize_instance_fields()


        self._nodes.resize(self._tableSize)


    def __init__(self, size):
        self._initialize_instance_fields()

        self._tableSize = size
        self._nodes.resize(self._tableSize)


    # closing node functions
    def close(self):

        self._nodes.erase(self._nodes.begin())

    def Insert(self, bid):

        #calculate the key for this bid
        key = self._hash(int(bid.bidId))

        #try and retrieve node using the key
        oldNode = (self._nodes[key])

        #if no entry found for this key
        if oldNode is None:
            newNode = Node(bid, key)

            self._nodes.insert(self._nodes.begin() + key, newNode)
        else:
            #node found
            if oldNode.key == numeric_limits.max():
                oldNode.key = key

                oldNode.bid.copy_from(bid)
                oldNode.next = None
            else:
                #find the next open node (last)
                while oldNode.next is not None:
                    oldNode = oldNode.next
                oldNode.next = Node(bid, key)


    #*
    # * Print all bids
    #
    def PrintAll(self):
        i = 0
        while i < len(self._nodes):
            bid = self._nodes[i].bid
            print(bid.bidId, end = '')
            print(": ", end = '')
            print(bid.title, end = '')
            print(" | ", end = '')
            print(bid.amount, end = '')
            print(" | ", end = '')
            print(bid.fund, end = '')
            print("\n", end = '')
            i += 1


    #*
    # * Removes a bid
    # *
    # * @param bidId The bid id to search for
    #
    def Remove(self, bidId):

        key = self._hash(int(bidId))
        self._nodes.pop(key)

    def Search(self, bidId):
        bid = Bid()



        #calculates the key for this bid
        key = self._hash(int(bidId))

        #try and retrieve node using the key
        node = (self._nodes[key])

        #if no entry found
        if node is None or node.key == numeric_limits.max():

            return Bid(bid)

        #if node found that matches key
        if node is not None and node.key != numeric_limits.max() and node.bid.bidId.compare(bidId) == 0:

            return Bid(node.bid)

        #searchs for matches in the linked list
        while node is not None:
            if node.key != numeric_limits.max() and node.bid.bidId.compare(bidId) == 0:

                return Bid(node.bid)
            node = node.next

        return Bid(bid)


def main(argc, args):

    # process command line arguments
    csvPath = ""
    searchValue = ""
    if argc == 2:
        csvPath = args[1]
        searchValue = "98109"
    elif argc == 3:
        csvPath = args[1]
        searchValue = args[2]
    else:
        csvPath = "eBid_Monthly_Sales_Dec_2016.csv"
        searchValue = "98109"

    # timer variable
    ticks = clock_t()

    # Define a hash table to hold all the bids and give it an empty(None) initialization
    bidTable = None

    bid = Bid()

    choice = 0
    while choice != 9:
        print("Menu:", end = '')
        print("\n", end = '')
        print("  1. Load Bids", end = '')
        print("\n", end = '')
        print("  2. Display All Bids", end = '')
        print("\n", end = '')
        print("  3. Find Bid", end = '')
        print("\n", end = '')
        print("  4. Remove Bid", end = '')
        print("\n", end = '')
        print("  9. Exit", end = '')
        print("\n", end = '')
        print("Enter choice: ", end = '')
        cin >> choice


        if choice == 1:
            bidTable = HashTable()

            # Initialize a timer variable before loading bids
            ticks = clock()

            # Completes the funtion call to load the bids
            Globals.loadBids(csvPath, bidTable)

            # Calculate elapsed time and displays result
            ticks = clock() - ticks # current clock ticks minus starting clock ticks
            print("time: ", end = '')
            print(ticks, end = '')
            print(" clock ticks", end = '')
            print("\n", end = '')
            print("time: ", end = '')
            print(ticks * 1.0 / CLOCKS_PER_SEC, end = '')
            print(" seconds", end = '')
            print("\n", end = '')

        elif choice == 2:
            bidTable.PrintAll()

        elif choice == 3:
            ticks = clock()

            bid.copy_from(bidTable.Search(searchValue))

            ticks = clock() - ticks # current clock ticks minus starting clock ticks

            if (not len(bid.bidId)) == 0:
                Globals.displayBid(Bid(bid))
            else:
                print("Bid Id ", end = '')
                print(searchValue, end = '')
                print(" not found.", end = '')
                print("\n", end = '')

            print("time: ", end = '')
            print(ticks, end = '')
            print(" clock ticks", end = '')
            print("\n", end = '')
            print("time: ", end = '')
            print(ticks * 1.0 / CLOCKS_PER_SEC, end = '')
            print(" seconds", end = '')
            print("\n", end = '')

        elif choice == 4:
            bidTable.Remove(searchValue)

    print("Good bye.", end = '')
    print("\n", end = '')


class Globals:
    #============================================================================
    # Global definitions visible to all Functions and classes
    #============================================================================

    DEFAULT_SIZE = 179



    # forward declarations
    @staticmethod
    def strToDouble(str, ch):
        str = str[0:remove(str.begin(), str.end(), ch)] + str[remove(str.begin(), str.end(), ch) + str.end():]
        return float(str)

    #============================================================================
    # Functions used for testing
    #============================================================================

    #*
    # * Display the bid information to the console (print)
    # *
    # * @param bid struct containing the bid info
    #

    def displayBid(bid):
        print(bid.bidId, end = '')
        print(": ", end = '')
        print(bid.title, end = '')
        print(" | ", end = '')
        print(bid.amount, end = '')
        print(" | ", end = '')
        print(bid.fund, end = '')
        print("\n", end = '')
        return

    #*
    # * Load a CSV file containing bids into a container
    # *
    # * @param csvPath the path to the CSV file to load
    # * @return a container holding all the bids read
    #

    def loadBids(csvPath, hashTable):
        print("Loading CSV file ", end = '')
        print(csvPath, end = '')
        print("\n", end = '')

        # initialize the CSV Parser using the given path
        file = csv.Parser(csvPath, eFILE, ',')

        # reads and displays header row
        header = file.getHeader()
        for c in header:
            print(c, end = '')
            print(" | ", end = '')
        print("", end = '')
        print("\n", end = '')

        try:
            # loop to read rows of a CSV file
            i = 0
            while i < file.rowCount():

                # This is the data structure which adds the bidds to the collection
                bid = Bid()
                bid.bidId = file[i][1]
                bid.title = file[i][0]
                bid.fund = file[i][8]
                bid.amount = Globals.strToDouble(file[i][4], '$')


                # moves the bid to the end of the table
                hashTable.Insert(Bid(bid))
                i += 1
        except csv.Error as e:
            std.cerr << e.what() << std.endl