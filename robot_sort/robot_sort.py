class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        #keep the none, go all the way to the end, swap it, go all the way to the beginning and THEN start the process
    #[11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18]
        for self._position in range(0, len(self._list)):

            if self._item == None:#self._position != 0 and
                self.swap_item()
                self.move_right()
                print(self._list)
            print(self.compare_item() == 1)
            while self.can_move_right():
                #self.move_right()
                print("right")
                if ((self.compare_item() == 1) or (self.compare_item() == 0)):
                    self.swap_item()
                    self.move_right()
                    continue
                elif (self.compare_item() == -1):
                    self.move_right()
                    # self.swap_item()  
                    print(self._list)  
                    continue

            #otherwise it can't move right so it reached the end, if the end is smaller then swap it
            if (self.compare_item() == 1):
                    self.swap_item()
                    print(self._list)
            
                        
            while self.can_move_left() and self._list[self._position] != None: # and i < self._position
                self.move_left()
                    #i+=1
            self.swap_item()
            print(self._list)
        # if None in self._list:           
        #     self.swap_item()
        
        print(self._position)
        print(self._list)

        return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)


    #hierarchy of functions
        # if compare_item() == None: #none (also can show none if not holding any item)*****
        # swap_item  needs to be initialized because the robot isn't holding any item at first, grab the first item


        # if compare_item() == 1: #greater than
        # if compare_item() == -1: #less than current held item
        # if compare_item() == 0: #equal to
        # if compare_item() == None: #none (also can show none if not holding any item)*****
        #     swap_item() can always be done, so it needs a condition to tell it when to (that would be compare_item)

        # if can_move_left():
        #     move_left() is posssible

        # if can_move_right(self):
        #     move_right() is possible

    
        # we can control the state of the robot with the light
        # if it is on we should end the sorting and return the value
        # else we should continue sorting



    # what needs to happen, bubble sort approach
        # have the robot hold an item
        # compare that item to the one next to it
        # if the item is greater, swap the items, return to the start and swap again
        # do this until it reaches the right most edge, then do it again but start from the next index higher,
        #      BUT if the current index equals the length of the list minus 1 then just return the list


    #psuedocode
        #initialize to first indexed item
    #         swap_item(self)
    #     #establish that we will be checking every position
    #         for i in range(0, len(self._list) - 1): 
    #             #if it has reached the end and the index equals the list minus 1
    #             if can_move_right(self) == False and i == len(self._list) - 1:
    #                 #check the list once more using recursion???
    #                 sort(self)
    #                 #return the completed result
    #                 return self._list
    #            #if it hasn't reached the end
    #             elif can_move_right(self):
    #                 #move to the right
    #                 move_right(self)
    #                 #compare the held item to the item at that position
    #                 if compare_item(self) == 1:
    #                     #the held item has a greater value so swap it with the item at this position
    #                     swap_item(self)
    #                     #if the robot can move left then it should move left until it can't anymore (while would be for selection sort- always returning to the beginning, we are just swapping neighbors)
    #                     if can_move_left(self): #changed from while
    #                         move_left(self)
    #                     #once it has reached the 0th index it should swap the held smaller item to place it at the beginning
    #                     swap_item(self)
    #                     continue
    #                 elif compare(self) == 0 or compare_item(self)== -1:
    #                     if can_move_right(self):
    #                         move_right(self)
    #                         #compare the items in the same way...should this be a helper function then instead?
    #                         #does this break this rule :You may NOT access any instance variables directly. (`self._anything`)
    #                         sort(self._list[self._position:])
    # #damn, I think actually selection sort would be better for this but I can't capture i+1 as a different variable


#attempt at selection sort

        # self.swap_item()
        # #establish that we will be checking every position
        # #for i in range(0, len(self._list) - 1): 
        # for element in self._list:
        #     if self.compare_item() == 1 and self.can_move_right():
        #         self.swap_item()
        #         self.move_right
        #     elif self.compare_item() == 0 and self.can_move_right(): 
        #         self.move_right
        #     elif self.compare_item() == -1 and self.can_move_right(): 
        #         self.move_right
        #     else:
        #         while self.can_move_left():
        #             self.move_left()
        #         self.swap_item()    
        #         continue #to next element
        #     return self._list

        # # helper function
        # # continue moving right and checking, swapping only smaller values until reaching the end then start at the next element

        # if self.compare_item() == 1 and self.can_move_right():
        #     self.swap_item()
        #     self.move_right
        # elif self.compare_item() == 0 and self.can_move_right(): 
        #     self.move_right
        # elif self.compare_item() == -1 and self.can_move_right(): 
        #     self.move_right
        # else:
        #     while self.can_move_left():
        #         self.move_left()
        #     self.swap_item()    
        #     continue #to next element


#there seems to be a problem with starting from 0 because compare_item think position zero is None so going to try from the other direction

        # self.swap_item()
        # # self._position += 1
        # #establish that we will be checking every position
        # for i in range((len(self._list) - 1):0): 
        # #for position in self._list:
        #     #self.swap_item()
        #     print("here0")
        #     print(self._item)
            
        #     if (self.compare_item() == -1) and (self.can_move_left()):
        #         self.swap_item()
        #         self.move_left
        #         print("here")
        #         print(self._item)
        #     elif (self.compare_item() == 0) and (self.can_move_left()): 
        #         self.move_left
        #         print("here2")
        #         print(self._item)
        #     elif (self.compare_item() == 1) and (self.can_move_left()): 
        #         self.move_left
        #         print("here3")
        #         print(self._item)
        #     else:
        #         while self.can_move_right():
        #             self.move_right()
        #         self.swap_item()  
        #         print("here4")
        #         print(self._item)  
        #         continue #to next element
        #     # return self._list
        # return self._list

        # WORKS FOR SMALL ARRAYS
        
        # for self._position in range(0, len(self._list)):

        #     if self._item == None:#self._position != 0 and
        #         self.swap_item()
        #         self.move_right()
        #         print(self._list)
        #     print(self.compare_item() == 1)
        #     while self.can_move_right() and ((self.compare_item() == 1) or (self.compare_item() == 0)):
        #         self.move_right()
        #         print("right")

        #     if (self.compare_item() == -1):
        #         self.move_left()
        #         self.swap_item()  
        #         print(self._list)   

        #     if (self.compare_item() == 1):
        #         self.swap_item()
        #         print(self._list)
            
                        
        #     while self.can_move_left() and self._list[self._position] != None: # and i < self._position
        #         self.move_left()
        #             #i+=1
        #     self.swap_item()
        #     print(self._list)
        # # if None in self._list:           
        # #     self.swap_item()
        
        # print(self._position)
        # print(self._list)

        # return self._list