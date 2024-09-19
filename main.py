#find area of the space
space_length = float(input("Enter the length of the space: "))
space_width = float(input("Enter the width of the space: "))
area_space = space_length * space_width
print("The area of the space is", area_space, "inches")
print("")

#find the volume of the first object
object1_length = float(input("Enter the length of the first object: "))
object1_width = float(input("Enter the width of the first object: "))
object1_height = float(input("Enter the height of the first object: "))
object1_volume = object1_length * object1_width * object1_height
print("The volume of the first object is", object1_volume, "inches")
print("")

#find the volume of the second object
object2_length = float(input("Enter the length of the second object: "))
object2_width = float(input("Enter the width of the second object: "))
object2_height = float(input("Enter the height of the second object: "))
object2_volume = object2_length * object2_width * object2_height
print("The volume of the second object is", object1_volume, "inches")
print()

#find the volume of the third object
object3_length = float(input("Enter the length of third the object: "))
object3_width = float(input("Enter the width of the third object: "))
object3_height = float(input("Enter the height of the third object: "))
object3_volume = object3_length * object3_width * object3_height
print("The volume of the third object is", object1_volume, "inches")
print("")

#calaculate the leftover space
volume_total = object1_volume + object2_volume + object3_volume
final_value = volume_total - area_space
print("you will need a container" , final_value, "inches total.")
