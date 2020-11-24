class CellFinder:

    """ 'Gift wrapping' algorithm, also known as 'Jarvis march' """

    def __init__(self):
        self.search_poll = []                                   # List of point which include in cell search
        self.cell = []                                          # Result list of coords of cell
        self.n = 0                                              # Length of input coords list

    def init_search_poll(self, coord_array):                    # Initialization of 'n' and 'search_poll'
        self.n = len(coord_array)                               # Write length of input coords list in 'n'
        self.search_poll = list(range(self.n))                  # Init 'search_poll' as indexes of 'coord_array'

    def find_most_left_point(self, coord_array):                # Finding the most-left point in 'coord_array'
        for i in range(1, self.n):                              # Loop throw all indexes of 'coord_array'
            first_coord = coord_array[self.search_poll[0]]      # Get the current the most-left point
            current_coord = coord_array[self.search_poll[i]]    # Get the current point for match

            if first_coord[1] > current_coord[1]:               # If current point is 'lefter' than current most-left
                self.search_poll[0], self.search_poll[i] = \
                    self.search_poll[i], self.search_poll[0]    # Swap the current point and current most-left point

        self.cell = [self.search_poll[0]]                       # Set the real most-left point in head of result cell
        self.search_poll.pop(0)                                 # Delete point which we already processed
        self.search_poll.append(self.cell[0])                   # Add processed point in to end of 'search_poll'

    @staticmethod
    def rotate(a, b, c):                                        # "Rotate" stuff using Linear Algebra (scalar dot)
        return (b[0] - a[0]) * (c[1] - b[1]) - \
               (b[1] - a[1]) * (c[0] - b[0])

    def process(self, coord_array):                             # Main loop
        self.init_search_poll(coord_array)                      # Init of 'search_poll'
        self.find_most_left_point(coord_array)                  # Finding the most-left point

        flag = True                                             # Set the end-flag
        while flag:                                             # While loop
            right = 0                                           # Init right as 0

            for i in range(1, len(self.search_poll)):           # For throw all indexes in 'search_poll'
                last_p = coord_array[self.cell[-1]]             # Choose the last point for match
                right_p = coord_array[self.search_poll[right]]  # Choose the right point for match
                cur_p = coord_array[self.search_poll[i]]        # Choose the current point for match

                if self.rotate(last_p, right_p, cur_p) < 0:     # Check position of point relate to last_point
                    right = i                                   # Set current index as 'right'

            if self.search_poll[right] == self.cell[0]:         # If current right point same as first point of cell
                flag = False                                    # Stop the while loop

            else:                                               # Otherwise
                self.cell.append(self.search_poll[right])       # Append this "right" point to result cell
                self.search_poll.pop(right)                     # And delete this point from 'search_poll'

        return self.cell                                        # Return result cell
