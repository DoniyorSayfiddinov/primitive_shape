class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def distance_from_Xcoordinate(self):
        """
        This method finds the distance between a point and its X coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return self.y

    def distance_from_Ycoordinate(self):
        """
        This method finds the distance between a point and its Y coordinates.

        Args:
            No
        Returns:
            float or int: distance.
        """
        return self.x

    def getQuadrant(self):
        """
        This method finds which quadrant the point is in.

        Args:
            No
        Returns:
            int: quadrant.
        """
        return "I" if self.x>0 and self.y>0 else "II" if self.x<0 and self.y>0 else "III" if self.x<0 and self.y<0 else "IV" if self.x>0 and self.y<0 else "Center" 


    def on_Xcoordinate(self):
        """
      

        Args:
            No
        Returns:
            bool: result.
        """
        return self.y==0
    def on_Ycoordinate(self):
        """
        This method checks for a point on the Y coordinate.

        Args:
            No
        Returns:
            bool: result.
        """
        return self.x==0
 