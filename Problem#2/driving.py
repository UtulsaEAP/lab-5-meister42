"""
Name: Henry Holman
Lab time: Thursday 2 pm
"""


def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    
   cost = miles_driven / miles_per_gallon * dollars_per_gallon
   return cost

   #write your code here

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 10.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 50.0):.2f}')
    print(f'{driving_cost(miles_per_gallon, dollars_per_gallon, 400.0):.2f}')