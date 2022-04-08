from hashtable import HashTable


# new class for packages and their identifiers
# space-time complexity O(1)
class Package:
    def __init__(self, packageid, address, city, zipcode, weight, deadline, status, notes, timestamp, start_time):
        self.packageid = packageid
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.weight = weight
        self.deadline = deadline
        self.status = status
        self.notes = notes
        self.timestamp = timestamp
        self.start_time = start_time


# List of all 40 packages with all their identifiers
p1 = Package(1, "195 W Oakland Ave", "Salt Lake City", "84115", 21, "10:30 AM", "At the hub", '', '', '08:00:00')
p2 = Package(2, "2530 S 500 E", "Salt Lake City", "84106", 44, "EOD", "At the hub", '', '', '10:20:00')
p3 = Package(3, "233 Canyon Rd", "Salt Lake City", "84103", 2, "EOD", "At the hub", 'Can only be on truck 2', '',
             '09:05:00')
p4 = Package(4, "380 W 2880 S", "Salt Lake City", "84115", 4, "EOD", "At the hub", '', '', '10:20:00')
p5 = Package(5, "410 S State St", "Salt Lake City", "84111", 5, "EOD", "At the hub", '', '', '09:05:00')
p6 = Package(6, "3060 Lester St", "West Valley City", "84119", 88, "10:30 AM", "At the hub",
             'Delayed on flight -- will not arrive until 9:05 AM', '', '09:05:00')
p7 = Package(7, "1330 2100 S", "Salt Lake City", "84106", 8, "EOD", "At the hub", '', '', '09:05:00')
p8 = Package(8, "300 State St", "Salt Lake City", "84103", 9, "EOD", "At the hub", '', '', '09:05:00')
p9 = Package(9, "410 S State St", "Salt Lake City", "84111", 2, "EOD", "At the hub", 'Wrong address listed', '',
             '09:05:00')
p10 = Package(10, "600 E 900 South", "Salt Lake City", "84105", 1, "EOD", "At the hub", '', '', '10:20:00')
p11 = Package(11, "2600 Taylorsville Blvd", "Salt Lake City", "84118", 1, "EOD", "At the hub", '', '', '10:20:00')
p12 = Package(12, "3575 W Valley Central Station bus Loop", "West Valley City", "84119", 1, "EOD", "At the hub",
              '', '', '10:20:00')
p13 = Package(13, "2010 W 500 S", "Salt Lake City", "84104", 2, "10:30 AM", "At the hub", '', '', '08:00:00')
p14 = Package(14, "4300 S 1300 E", "Millcreek", "84117", 88, "10:30 AM", "At the hub", 'Must be delivered with 15, 19',
              '', '08:00:00')
p15 = Package(15, "4580 S 2300 E", "Holladay", "84117", 4, "9:30 AM", "At the hub", '', '', '08:00:00')
p16 = Package(16, "4580 S 2300 E", "Holladay", "84117", 88, "10:30 AM", "At the hub", 'Must be delivered with 13, 19',
              '', '08:00:00')
p17 = Package(17, "3148 S 1100 W", "Salt Lake City", "84119", 2, "EOD", "At the hub", '', '', '10:20:00')
p18 = Package(18, "1488 4800 S", "Salt Lake City", "84123", 6, "EOD", "At the hub", 'Can only be on truck 2', '',
              '09:05:00')
p19 = Package(19, "177 W Price Ave", "Salt Lake City", "84115", 37, "EOD", "At the hub", '', '', '10:20:00')
p20 = Package(20, "3595 Main St", "Salt Lake City", "84115", 37, "10:30 AM", "At the hub",
              'Must be delivered with 13, 15', '', '08:00:00')
p21 = Package(21, "3595 Main St", "Salt Lake City", "84115", 3, "EOD", "At the hub", '', '', '08:00:00')
p22 = Package(22, "6351 South 900 East", "Murray", "84121", 2, "EOD", "At the hub", '', '', '10:20:00')
p23 = Package(23, "5100 South 2700 West", "Salt Lake City", "84118", 5, "EOD", "At the hub", '', '', '10:20:00')
p24 = Package(24, "5025 State St", "Murray", "84107", 7, "EOD", "At the hub", '', '', '10:20:00')
p25 = Package(25, "5383 S 900 East #104", "Salt Lake City", "84117", 7, "10:30 AM", "At the hub",
              'Delayed on flight -- will not arrive to dept until 9:05 AM', '', '09:05:00')
p26 = Package(26, "5383 S 900 East #104", "Salt Lake City", "84117", 25, "EOD", "At the hub", '', '', '09:05:00')
p27 = Package(27, "1060 Dalton Ave S", "Salt Lake City", "84104", 5, "EOD", "At the hub", '', '', '08:00:00')
p28 = Package(28, "2835 Main St", "Salt Lake City", "84115", 7, "EOD", "At the hub",
              'Delayed on flight -- will not arrive to depot until 9:05 AM', '', '10:20:00')
p29 = Package(29, "1330 2100 S", "Salt Lake City", "84106", 2, "10:30 AM", "At the hub", '', '', '09:05:00')
p30 = Package(30, "300 State St", "Salt Lake City", "84103", 1, "10:30 AM", "At the hub", '', '', '09:05:00')
p31 = Package(31, "3365 S 900 W", "Salt Lake City", "84119", 1, "10:30 AM", "At the hub", '', '', '09:05:00')
p32 = Package(32, "3365 S 900 W", "Salt Lake City", "84119", 1, "EOD", "At the hub",
              'Delayed on flight -- will not arrive to depot until 9:05 AM', '', '09:05:00')
p33 = Package(33, "2530 S 500 E", "Salt Lake City", "84106", 1, "EOD", "At the hub", '', '', '10:20:00')
p34 = Package(34, "4580 S 2300 E", "Holladay", "84117", 2, "10:30 AM", "At the hub", '', '', '08:00:00')
p35 = Package(35, "1060 Dalton Ave S", "Salt Lake City", "84104", 88, "EOD", "At the hub", '', '', '08:00:00')
p36 = Package(36, "2300 Parkway Blvd", "West Valley City", "84119", 88, "EOD", "At the hub",
              'Can only be on truck 2', '', '09:05:00')
p37 = Package(37, "410 S State St", "Salt Lake City", "84111", 2, "10:30 AM", "At the hub", '', '', '09:05:00')
p38 = Package(38, "410 S State St", "Salt Lake City", "84111", 9, "EOD", "At the hub", 'Can only be on truck 2', '',
              '09:05:00')
p39 = Package(39, "2010 W 500 S", "Salt Lake City", "84104", 9, "EOD", "At the hub", '', '', '08:00:00')
p40 = Package(40, "380 W 2880 S", "Salt Lake City", "84115", 45, "10:30 AM", "At the hub", '', '', '08:00:00')

# initializing the myHash hashtable for packages to be inserted on
# inserting all packages into myHash for use in main and distance
myHash = HashTable()
myHash.insert(1, p1)
myHash.insert(2, p2)
myHash.insert(3, p3)
myHash.insert(4, p4)
myHash.insert(5, p5)
myHash.insert(6, p6)
myHash.insert(7, p7)
myHash.insert(8, p8)
myHash.insert(9, p9)
myHash.insert(10, p10)
myHash.insert(11, p11)
myHash.insert(12, p12)
myHash.insert(13, p13)
myHash.insert(14, p14)
myHash.insert(15, p15)
myHash.insert(16, p16)
myHash.insert(17, p17)
myHash.insert(18, p18)
myHash.insert(19, p19)
myHash.insert(20, p20)
myHash.insert(21, p21)
myHash.insert(22, p22)
myHash.insert(23, p23)
myHash.insert(24, p24)
myHash.insert(25, p25)
myHash.insert(26, p26)
myHash.insert(27, p27)
myHash.insert(28, p28)
myHash.insert(29, p29)
myHash.insert(30, p30)
myHash.insert(31, p31)
myHash.insert(32, p32)
myHash.insert(33, p33)
myHash.insert(34, p34)
myHash.insert(35, p35)
myHash.insert(36, p36)
myHash.insert(37, p37)
myHash.insert(38, p38)
myHash.insert(39, p39)
myHash.insert(40, p40)

# testing information
# print(p1.city)
# print(p30.zipcode)
# print(p14.notes)
# print(p38.status)
# # print(p22.weight)
# print(myHash.lookup(p40.packageid))
# print(myHash.table)
# print(myHash.table[1])
# print(myHash.table[0])
