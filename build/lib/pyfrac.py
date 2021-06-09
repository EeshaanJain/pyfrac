import re
from math import gcd, isclose, floor, ceil

"""Template: If any is None, omit it

Args:

Returns:

Raises:

"""

        
class Fraction(object):
    """Implementation of the Fraction Class to deal with fractions"""
    __version__ = '0.0.1'
    __author__ = "Eeshaan Jain"


    def __init__(self, numerator: int, denominator: int = 1, simplify: bool = True):

        if not isinstance(numerator, int):
            raise TypeError(f"numerator should be of type int, found {type(numerator).__name__}")
        if not isinstance(denominator, int):
            raise TypeError(f"denominator should be of type int, found {type(denominator).__name__}")
        if not isinstance(simplify, bool):
            raise TypeError(f"simplify should be of type bool, found {type(simplify).__name__}")
        if denominator == 0:
            raise ZeroDivisionError(f"denominator cannot be zero")

        self._numerator = numerator
        if denominator < 0:
            self.numerator = - numerator

        self._denominator = abs(denominator)

        if simplify:
            self._simplify()

    @property
    def numerator(self):
        return self._numerator

    @numerator.setter
    def numerator(self, value):
        if isinstance(value, int):
            self._numerator = value
        else:
            raise TypeError(f"numerator should be of type int, found {type(numerator).__name__}")

    @property
    def denominator(self):
        return self._denominator

    @denominator.setter
    def denominator(self, value):
        if isinstance(value, int):
            if value == 0:
                raise ZeroDivisionError(f"denominator cannot be zero")
            else:    
                self._denominator = value
        else:
            raise TypeError(f"numerator should be of type int, found {type(numerator).__name__}")

    def _simplify(self):
        """ Simplifies the fraction to the lowest form
        """
        _gcd = gcd(self.numerator, self.denominator)
        self.numerator = int(self.numerator / _gcd)
        self.denominator = int(self.denominator / _gcd)

    def __decimal(self, num_decimals):
        decimal_value = self.numerator / self.denominator
        return f'{decimal_value:.{num_decimals}f}'

    def decimal(self, num_decimals=5):
        """ Converts the fraction to the decimal counterpart
        Args:
            num_decimals: Number of decimal places for the floating number (default:= 2)
        Returns: 
            A floating point number with the appropriate decimal numbers
        """
        return self.__decimal(num_decimals)

    def __get_number_length(self, numerator_bool, denominator_bool):
        if numerator_bool and not denominator_bool:
                return (len(str(abs(self.numerator))),)

        elif denominator_bool and not numerator_bool:
            return (len(str(abs(self.denominator))),)
        
        elif numerator_bool and denominator_bool:
            return (len(str(abs(self.numerator))), len(str(abs(self.denominator))))

        else:
            raise ValueError(f"At least one of numerator and denominator should be True")

    def get_number_length(self, numerator_bool = True, denominator_bool = False):
            return self.__get_number_length(numerator_bool, denominator_bool)

    def __pretty_print(self):
        num_length, den_length = self.__get_number_length(True, True)
        s = str(self.numerator) + '\n'
        s += '-' * max(num_length, den_length) + '\n'
        s += str(self.denominator)
        return s

    def pretty_print(self):
        """Pretty print the fraction
        Returns:
            The string with the fraction in a pretty format
        
        """
        return self.__pretty_print()


    def __reciprocal(self):

        if self.numerator == 0:
            raise ZeroDivisionError(f"Cannot find reciprocal if numerator is 0")

        return self.__class__(self.denominator, self.numerator)

    def reciprocal(self):
        """To return the reciprocal of the Fraction
        Returns: 
            The reciprocal, i.e a/b -> b/a

        Raises: 
            ZeroDivisionError: If the numerator is zero 
        """
        return self.__reciprocal()

    def __to_mixed(self, pretty):
        if not pretty:
            if(abs(self.numerator) <= self.denominator):
                raise ValueError(f'The absolute value of the fraction {self.__str__()} is less than or equal to 1')
            else:
                quo = abs(self.numerator) // self.denominator
                rem = abs(self.numerator) % self.denominator
                if self.numerator >= 0:
                    return f"{quo} {rem}/{self.denominator}"
                else:
                    return f"-{quo} {rem}/{self.denominator}"
    
    def to_mixed(self, pretty=False):
        """Prints the mixed fraction (if absolute value > 1) 
        Args:
            pretty: If we want to pretty print the mixed fraction (default:= False)
        Returns:
            A string denoting the mixed fraction (calls pretty_print() if pretty = True)
        Raises:
            ValueError if the abs(fraction) <= 1
        
        """
        return self.__to_mixed(pretty)

    @classmethod
    def from_string(cls, frac_string: str, simplify: bool = True):
        """ Alternative constructor to create a Fraction from a string. The format is supposed to be
            `numerator / denominator` (Number of spaces don't matter)
            Args:
                frac_string: Input string
                simplify: If the fraction should be simplified to the lowest form (default:= True)
            Returns:
                Instance of Fraction
            Raises:
                TypeError: If the input is not a string
        """

        if not isinstance(frac_string, str):
            raise TypeError(f"frac_string should be of type str, found {type(frac_string).__name__}")
        num, den = re.findall(r"\d+\d*", frac_string)
        return cls(int(num), int(den), simplify)

    @classmethod
    def from_tuple(cls, frac_tuple: tuple, simplify: bool = True):
        """ Alternative constructor to create a Fraction from a tuple. The format is supposed to be
            `(numerator)` if the denominator is supposed to be 1
            `(numerator, denominator)` if a fraction is supplied
            `(quotient, remainder, denominator)` if mixed fraction is supplied

            Args:
                frac_tuple: Input tuple
                simplify: If the fraction should be simplified to the lowest form (default:= True)
            Returns:
                Instance of Fraction
            Raises:
                TypeError: If the input is not a tuple
        """

        if not isinstance(frac_tuple, tuple):
            raise TypeError(f"frac_tuple should be of type tuple, found {type(frac_tuple).__name__}")

        if (len(frac_tuple) > 3) or (len(frac_tuple) < 1):
            raise TypeError(f"from_tuple expected between 1 to 3 elements in the tuple, received {len(frac_tuple)}")

        else:
            for num in frac_tuple:
                if not isinstance(num, int):
                    raise TypeError(f"expected int in definition, found {type(num).__name__}")

            if len(frac_tuple) == 1:
                return cls(frac_tuple[0], 1)

            elif len(frac_tuple) == 2:
                return cls(frac_tuple[0], frac_tuple[1])
            else:
                return cls(frac_tuple[0] * frac_tuple[2] + frac_tuple[1], frac_tuple[2])

    @classmethod
    def from_dict(cls, frac_dict: dict, simplify: bool = True):
        """ Alternative constructor to create a Fraction from a dictionary. The format is supposed to be
            {num: numerator, den: denominator}
            Args:
                frac_dict: Input dictionary
                simplify: If the fraction should be simplified to the lowest form (default:= True)
            Returns:
                Instance of Fraction
            Raises:
                TypeError: If the input is not a dictionary
                ValueError: If the key num or den doesn't exist
        """
        if not isinstance(frac_dict, dict):
            raise TypeError(f"frac_dict should be of type dict, found {type(frac_dict).__name__}")

        if (len(frac_dict) > 2) or (len(frac_dict) < 1):
            raise TypeError(f"from_dict expected between 1 to 2 keys in the dictionary, received {len(frac_dict)}")

        else:
            if("num" not in frac_dict.keys()):
                raise ValueError(f"key num doesn't exist")
            elif("den" not in frac_dict.keys()):
                raise ValueError(f"key den doesn't exist")
            else:
                return cls(frac_dict['num'], frac_dict['den'])

    @classmethod
    def from_repeating_decimal(cls, frac_repeating: str):
        """Create a Fraction from a repeating decimal, often represented by a bar over the repeating decimal portion
        The input is expected as a string of the form: `abc.d|efg...` where the decimals after | are repeating
        """
        if not isinstance(frac_repeating, str):
            raise TypeError(f"frac_repeating should be of type str, found {type(frac_repeating).__name__}")
        else:
            first, other = frac_repeating.split('.')
            second, third = other.split('|')
            num = int(first+second+third) - int(first+second)
            den = int(10**len(str(second)) * (10**len(str(third)) - 1))
            return cls(num, den)


        
    def __repr__(self):
        """Represents the fraction in the form: Fraction(numerator: numerator, denominator: denominator)"""
        return f"{self.__class__.__name__}(numerator: {self.numerator}, denominator: {self.denominator})"

    def __str__(self):
        """Prints the fraction in the form: numerator / denominator"""
        return f"{self.numerator} / {self.denominator}"

    def __abs__(self):
        """Returns an instance with the absolute fraction"""
        return self.__class__(abs(self.numerator), abs(self.denominator))

    def __floor__(self):
        """Returns the integer just lower than the Fraction"""
        return floor(float(self.decimal()))

    def __neg__(self):
        """Implements negation of a Fraction"""
        return self.__class__(-1 * self.numerator, self.denominator)

    def __ceil__(self):
        """Returns the integer just lower than the Fraction"""
        return ceil(float(self.decimal()))

    def __pow__(self, other):
        """"Raises a Fraction to a power"""
        if other >= 0:
            return self.__class__(self.numerator**other, self.denominator**other)
        else:
            return self.__class__(self.denominator**abs(other), self.numerator**abs(other))

    def __eq__(self, other):
        """Check if two Fractions, or a Fraction and int, or a Fraction and float are equal"""
        if isinstance(other, self.__class__):
            return self.numerator * other.denominator == other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return isclose(float(self.decimal(20)), other)
        else:
            raise TypeError(f"Cannot compare type Fraction with type {other.__class__.__name__}")

    def __ne__(self, other):
        """Check if two Fractions, or a Fraction and int, or a Fraction and float are not equal"""
        if isinstance(other, self.__class__):
            return self.numerator * other.denominator != other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return not isclose(float(self.decimal(20)), other)
        else:
            raise TypeError(f"Cannot compare type Fraction with type {other.__class__.__name__}")

    def __lt__(self, other):
        """Check if a Fraction is less than another Fraction, an integer or a float"""
        if isinstance(other, self.__class__):
            return self.numerator * other.denominator < other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return float(self.decimal()) < other and not self == other
        else:
            raise TypeError(f"Cannot compare type Fraction with type {other.__class__.__name__}")

    def __le__(self, other):
        """Check if a Fraction is less than or equal to another Fraction, an integer or a float"""
        if isinstance(other, self.__class__):
            return self.numerator * other.denominator <= other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return float(self.decimal()) <= other and not self == other
        else:
            raise TypeError(f"Cannot compare type Fraction with type {other.__class__.__name__}")

    def __gt__(self, other):
        """Check if a Fraction is greater than another Fraction, an integer or a float"""
        if isinstance(other, self.__class__):
            return self.numerator * other.denominator > other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return float(self.decimal()) > other and not self == other
        else:
            raise TypeError(f"Cannot compare type Fraction with type {other.__class__.__name__}")

    def __ge__(self, other):
        """Check if a Fraction is greater than or equal to another Fraction, an integer or a float"""
        if isinstance(other, self.__class__):
            return self.numerator * other.denominator >= other.numerator * self.denominator
        elif isinstance(other, (int, float)):
            return float(self.decimal()) >= other and not self == other
        else:
            raise TypeError(f"Cannot compare type Fraction with type {other.__class__.__name__}")

    def __add__(self, other):
        """Adds a Fraction to another Fraction or integer"""
        if isinstance(other, self.__class__):
            num = self.numerator * other.denominator + self.denominator * other.numerator
            den = self.denominator * other.denominator
            return self.__class__(num, den)

        elif isinstance(other, int):
            return self.__class__(self.numerator + other*self.denominator, self.denominator)
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in addition, received {other.__class__.__name__}")

    def __sub__(self, other):
        """Subtracts a Fraction or integer from the Fraction"""
        if isinstance(other, self.__class__):
            num = self.numerator * other.denominator - self.denominator * other.numerator
            den = self.denominator * other.denominator
            return self.__class__(num, den)

        elif isinstance(other, int):
            return self.__class__(self.numerator - other*self.denominator, self.denominator)
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in subtraction, received {other.__class__.__name__}")

    def __mul__(self, other):
        """Adds a Fraction to another Fraction or integer"""
        if isinstance(other, self.__class__):
            num = self.numerator *  other.numerator
            den = self.denominator * other.denominator
            return self.__class__(num, den)

        elif isinstance(other, int):
            return self.__class__(self.numerator * other, self.denominator)
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in multiplication, received {other.__class__.__name__}")

    def __truediv__(self, other):
        """Adds a Fraction to another Fraction or integer"""
        if isinstance(other, self.__class__):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            return self.__class__(num, den)

        elif isinstance(other, int):
            return self.__class__(self.numerator, self.denominator * other)
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in division, received {other.__class__.__name__}")

    def __floordiv__(self, other):
        """Adds a Fraction to another Fraction or integer"""
        if isinstance(other, self.__class__):
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            return floor(self.__class__(num, den))

        elif isinstance(other, int):
            return floor(self.__class__(self.numerator, self.denominator * other))
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in floordivision, received {other.__class__.__name__}")

    def __and__(self, other):
        """Ands a Fraction to another Fraction or integer"""
        if isinstance(other, self.__class__):
            num = self.numerator & other.numerator
            den = self.denominator & other.denominator
            return self.__class__(num, den)

        elif isinstance(other, int):
            return self.__class__(self.numerator & other, self.denominator)
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in bitwise and, received {other.__class__.__name__}")

    def __or__(self, other):
        """Ors a Fraction to another Fraction or integer"""
        if isinstance(other, self.__class__):
            num = self.numerator | other.numerator
            den = self.denominator | other.denominator
            return self.__class__(num, den)

        elif isinstance(other, int):
            return self.__class__(self.numerator | other, self.denominator)
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in bitwise or, received {other.__class__.__name__}")

    def __xor__(self, other):
        """Xors a Fraction to another Fraction or integer"""
        if isinstance(other, self.__class__):
            num = self.numerator ^ other.numerator
            den = self.denominator ^ other.denominator
            return self.__class__(num, den)

        elif isinstance(other, int):
            return self.__class__(self.numerator ^ other, self.denominator)
        
        else:
            raise TypeError(f"Expected type {self.__class__.__name__} or int in bitwise xor, received {other.__class__.__name__}")

