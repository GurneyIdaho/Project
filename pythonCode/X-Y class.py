import math

class Position:
    def __init__(self, initX, initY):
        """
        Initialize the position with starting angles in degrees.
        :param initX: Initial x angle.
        :param initY: Initial y angle.
        """
        self.x = initX 
        self.y = initY 

    def getX(self):
        """
        Get the current x angle.
        """
        return self.x

    def getY(self):
        """
        Get the current y angle.
        """
        return self.y

    def updateX(self, thetaX):
        """
        Increment the x angle by thetaX.
        :param thetaX: Change in x angle (degrees).
        """
        self.x = (self.x + thetaX) 

    def updateY(self, thetaY):
        """
        Increment the y angle by thetaY.
        :param thetaY: Change in y angle (degrees).
        """
        self.y = (self.y + thetaY) 


    """
    The things bellow are all extra fetures 
    """

    def setToTarget(self, targetX, targetY):
        """
        Set the pointer directly to the target angles.
        :param targetX: Target x angle.
        :param targetY: Target y angle.
        """
        self.x = targetX 
        self.y = targetY 

    def minDistZero(self):
        """
        Calculate the minimum angular distance from the current position to 0,0.
        """
        return math.sqrt(self.x**2 + self.y**2)



# Example usage (This could be somehow linked to wasd)
pointer = Position(0, 0)
pointer.updateX(1) # moves +1 degree 
pointer.updateX(-1) # moves +1 degree 
pointer.updateY(1) # moves +1 degree 
pointer.updateY(-1) # moves +1 degree 




# Directly set the pointer to a specific direction
pointer.setToTarget(180, 360)
print("X:", pointer.getX(), "Y:", pointer.getY())

# Calculate the minimum distance to (0,0)
print("Distance to (0, 0):", pointer.minDistZero())



