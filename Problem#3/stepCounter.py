"""
Name: Henry Holman 
Lab time: Thursday 2 pm
"""

def feet_to_steps(user_feet):
    steps = user_feet / 2.5
    return steps
   

if __name__ == '__main__':

    user_feet = float(input())
    #take input feet steps here
    #store it into the function
    print(int(feet_to_steps(user_feet)))
    