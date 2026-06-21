location_list = []
result_dictionary={}
town_list={"Douala":82,"Yaounde":89,"Limbe":56,"Kribi":70,"Bamenda":60,"Nkongsamba":53,"Buea":71 ,"Bafoussam":61}

for i in range(5):#the user input 5 values
    Location= input("Enter your Location : ")
    location_list.append(Location)
    if  Location in town_list:
        score = town_list[Location]#the score represent the key
        if score > 60:
            rist_status="safe"
        else:
            rist_status="high Risk"
        result_dictionary[Location]=rist_status
        print(rist_status)

    else:
        print("Not in the data base")# if the user enter a value that is not in the our list
       
print(result_dictionary)