#Name :- Himansu Hati #Batch :- C6 #Mis No:- 612205022
import math
resultant_force = [0,0,0]
n = int(input("How many non concurrent forces you want to enter"))
for x in range(0,n):
    magnitude = float(input("Enter magnitude of force: "))
    angle1 = float(input("Enter angle 1 with xy plane"))
    angle2 = float(input("Enter angle 2 with yz plane"))
    fx = magnitude * math.sin(math.radians(angle1)) * math.cos(math.radians(angle2))
    fy = magnitude * math.sin(math.radians(angle1)) * math.sin(math.radians(angle2))
    fz = magnitude * math.cos(math.radians(angle1))
    resultant_force[0] += fx
    resultant_force[1] += fy
    resultant_force[2] += fz
print("Resultant force of given non concurrent force system is ",resultant_force[0],"i+",resultant_force[1],"j+",resultant_force[2],"k")
print("Magnitude of resultant force is ",math.sqrt((pow(resultant_force[0],2)+pow(resultant_force[1],2)+pow(resultant_force[2],2))))





