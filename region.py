"""
Miguel Oyler-Castrillo
CS1103 Project 4: Purple America
Region Class
"""

class Region:
    """
    A region (represented by a list of long/lat coordinates) along with
    republican, democrat, and other vote counts.
    """

    def __init__(self, coords, r_votes, d_votes, o_votes):
        self.coordinates = coords
        self.republican_votes = float(r_votes)
        self.democrat_votes = float(d_votes)
        self.other_votes = float(o_votes)

    def lats(self):
        """Return a list of the latitudes of all the coordinates in the region"""
        lat_list = []
        for i in self.coordinates:
            lat_list.append(i[1])
        return [float(k) for k in lat_list]

    def longs(self):
        """Return a list of the longitudes of all the coordinates in the region"""
        longitude_list = []
        for i in self.coordinates:
            longitude_list.append(i[0])
        return [float(k) for k in longitude_list]

    def min_lat(self):
        """Return the minimum latitude of the region"""
        return min(self.lats())

    def min_long(self):
        """Return the minimum longitude of the region"""
        return min(self.longs())
    

    def max_lat(self):
        """Return the maximum latitude of the region"""
        return max(self.lats())

    def max_long(self):
        """Return the maximum longitude of the region"""
        return max(self.longs())


    def plurality(self):
        """return 'REPUBLICAN','DEMOCRAT', or 'OTHER'
        depending on plurality of votes"""
        votes_list = [self.republican_votes, self.democrat_votes,
                      self.other_votes]
        if self.republican_votes is max(votes_list):
            return "REPUBLICAN"
        elif self.democrat_votes is max(votes_list):
            return "DEMOCRAT"
        else:
            return 'OTHER'
        

    def total_votes(self):
        """The total number of votes cast in this region"""
        votes_list = [self.republican_votes, self.democrat_votes,
                      self.other_votes]
        return sum(votes_list)

    def republican_percentage(self):
        """The precentage of republication votes cast in this region"""
        votes_list = [self.republican_votes, self.democrat_votes,
                      self.other_votes]
        return votes_list[0] / sum(votes_list)

    def democrat_percentage(self):
        """The precentage of democrat votes cast in this region"""
        votes_list = [self.republican_votes, self.democrat_votes,
                      self.other_votes]
        return votes_list[1] / sum(votes_list)

    def other_percentage(self):
        """The precentage of other votes cast in this region"""
        votes_list = [self.republican_votes, self.democrat_votes,
                      self.other_votes]
        return votes_list[2] / sum(votes_list)

