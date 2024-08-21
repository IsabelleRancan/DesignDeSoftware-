from abc import ABC, abstractmethod

class ShapeAreaCalculator(ABC):
    @abstractmethod
    def calculate_area(self, shape):
        pass

class CircleAreaCalculator(ShapeAreaCalculator):
        def calculate_area(self, shape):
             return 3.14 * shape ['radius'] **2 
        
class RectangleAreaCalculator(ShapeAreaCalculator):
        def calculate_area(self, shape):
             return shape['width'] * shape['height']
                
#ex de uso 
rectangle = {'type' : 'rectangle', 'width' : 5, 'height' : 1}
circle = {'type' : 'circle', 'radius': 7}

calculator = RectangleAreaCalculator()
print(calculator.calculate_area(rectangle))
calculator = CircleAreaCalculator()
print(calculator.calculate_area(circle))