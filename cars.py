Volkswagon={"braking_time":4,"pickup":7, "max_speed":150,  "Mileage":18}
Mercedes={"braking_time":5,"pickup":6,"max_speed":152, "Mileage":17}
BMW={"braking_time":8,"pickup":2, "max_speed":149,  "Mileage":20}
braking_points=[]
pickup_points=[]

def calculte_braking_points_and_pickup(a,b):
    a=100-a
    b=100-b
    braking_points.append(a)
    pickup_points.append(b)
    
    

calculte_braking_points_and_pickup(Volkswagon["braking_time"],Volkswagon["pickup"])
calculte_braking_points_and_pickup(Mercedes["braking_time"],Mercedes["pickup"])
calculte_braking_points_and_pickup(BMW["braking_time"],BMW["pickup"])


Volkswagon["braking_time"],Volkswagon["pickup"]=braking_points[0],pickup_points[0]
Mercedes["braking_time"],Mercedes["pickup"]=braking_points[1],pickup_points[1]
BMW["braking_time"],BMW["pickup"]=braking_points[2],pickup_points[2]
    
print(Volkswagon)
print(Mercedes)
print(BMW)

def calculate_sum(d):
    add=0
    for i in d:
        add=add+d[i]
    print(add)

    
calculate_sum(Volkswagon)
calculate_sum(Mercedes)
calculate_sum(BMW)


