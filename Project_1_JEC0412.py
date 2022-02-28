print("+----------------------------------------------------+")
print("|      Computer Science and Engineering              | ")
print("|     CSCE 1035.001 - Computer Programming I         | ")
print("|  Jonathan Chen  jec0412  joanthanchen3@my.unt.edu  | ")
print("+----------------------------------------------------+ ")
# this show and define the displacment formula
def displacement_eq( vi, t, a):
    d = vi*t + .5*a*(t**2)
# this set he parameters for the variables in order to plug in 
vi = float(input('Enter the intial velocity in m/s:'))
a = float(input('Enter the accelration in m/s/s:'))
t = float(input("Enter the time in s:"))
d = vi*t + .5*a*(t**2)
# prints out the anwer after user has inputted the correct variable 
print("The object has traveled",d,"meters.")
