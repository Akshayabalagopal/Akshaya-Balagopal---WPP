'''Write a class called Converter. The user will pass a length and a unit when declaring an object
from the class—for example, c = Converter(9,'inches'). The possible units are inches, feet,
yards, miles, kilometers, meters, centimeters, and millimeters. For each of these units there
should be a method that returns the length converted into those units. For example, using the
Converter object created above, the user could call c.feet() and should get 0.75 as the result.
'''

class Converter():
    conversion_factors={
        'inches': 1,
        'feet': 1 / 12,
        'yards': 1 / 36,
        'miles': 1 / 63360,
        'kilometers': 1 / 39370.1,
        'meters': 1 / 39.3701,
        'centimeters': 2.54,
        'millimeters': 25.4}
    
    def __init__(self, length, unit):
        self.length=length
        self.unit=unit.lower()

        if self.unit not in Converter.conversion_factors:
            raise ValueError(f"Invalid unit: {','.join(Converter.conversion_factors.keys())}")
    
    def convert_to_inches(self):
        return self.length*Converter.conversion_factors[self.unit]
    
    def inches(self):
        return self.convert_to_inches()
    
    def feet(self):
        return self.convert_to_inches()/Converter.conversion_factors['feet']
    
    def yards(self):
        return self.convert_to_inches()/Converter.conversion_factors['yards']
    
    def miles(self):
        return self.convert_to_inches()/Converter.conversion_factors['miles']
    
    def kilometers(self):
        return self.convert_to_inches()/Converter.conversion_factors['kilometers']
    
    def meters(self):
        return self.convert_to_inches()/Converter.conversion_factors['meters']
    
    def centimeters(self):
        return self.convert_to_inches()/Converter.conversion_factors['centimeters']
    
    def millimeters(self):
        return self.convert_to_inches()/Converter.conversion_factors['millimeters']
    
def main():
    length=float(input("Enter the length: "))
    unit=input("Enter the unit: ")
    c=Converter(length, unit)

    print(f"{length} {unit} is equivalent to:")
    print(f"{c.inches()} inches")
    print(f"{c.feet()} feet")
    print(f"{c.yards()} yards")
    print(f"{c.miles()} miles")
    print(f"{c.kilometers()} kilometers")
    print(f"{c.meters()} meters")
    print(f"{c.centimeters()} centimeters")
    print(f"{c.millimeters()} millimeters")

if __name__=="__main__":
    main()