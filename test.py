
import ingredient_slicer

slicer = ingredient_slicer.IngredientSlicer("3 tbsp unsalted butter, softened at room temperature")

print(slicer.food()) 

print(slicer.quantity()) 

print(slicer.unit()) 

print(slicer.standardized_unit()) 

print(slicer.prep()) 
