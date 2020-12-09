class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : November 2020
    This class allows fraction manipulations through several operations.
    """

    def __init__(num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : ?
        POST : ?
        """
        pass

    @property
    def numerator(self):
        pass
    @property
    def denominator(self):
        pass

    def __str__(self) :
        """Return a textual representation of the reduced form of the fraction

        PRE : ?
        POST : ?
        """
        pass

    def as_mixed_number(self) :
        """Return a textual representation of the reduced form of the fraction as a mixed number

        A mixed number is the sum of an integer and a proper fraction

        PRE : ?
        POST : ?
        """
        pass


    def __add__(self, other):
        """Overloading of the + operator for pyfractions

         PRE : ?
         POST : ?
         """
        pass


    def __sub__(self, other):
        """Overloading of the - operator for pyfractions

        PRE : ?
        POST : ?
        """
        pass


    def __mul__(self, other):
        """Overloading of the * operator for pyfractions

        PRE : ?
        POST : ?
        """
        pass


    def __truediv__(self, other):
        """Overloading of the / operator for pyfractions

        PRE : ?
        POST : ?
        """
        pass


    def __pow__(self, other):
        """Overloading of the ** operator for pyfractions

        PRE : ?
        POST : ?
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fraction comparison

        PRE : ?
        POST : ?
        """
        pass


        # TODO : [BONUS] You can overload other operators if you wish


    def isZero(self):
        """Check if a fraction's value is 0

        PRE : ?
        POST : ?
        """
        pass


    def isInteger(self):
        """Check if a fraction is integer (ex : 8/4, 3, 2/2, ...)

        PRE : ?
        POST : ?
        """
        pass

    def isProper(self):
        """Check if the absolute value of the fraction is < 1

        PRE : ?
        POST : ?
        """

    def isUnit(self):
        """Check if a fraction's numerator is 1 in its reduced form

        PRE : ?
        POST : ?
        """
        pass

    def isAdjacentTo(self, other) :
        """Check if two pyfractions differ by a unit fraction

        Two pyfractions are adjacents if the absolute value of the difference them is a unit fraction

        PRE : ?
        POST : ?
        """
        pass

    def __double__(self) :
        """Returns the decimal value of the fraction

        PRE : ?
        POST : ?
        """
        pass