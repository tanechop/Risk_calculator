
from datetime import datetime
town_list={"Douala":82,"Yaounde":89,"Limbe":56,"Kribi":70,"Bamenda":60,"Nkongsamba":53,"Buea":71 ,"Bafoussam":61}
result_dictionary={}  
def get_safety_status(location_name:str) -> str:
    
    score = town_list[location_name]#the score represent the key
    if score > 60:
        return "safe"
    else:
        return"high Risk"

try:
    with open("locations.txt","r") as file:
        locations=file.readlines()
    for location in locations:
        location  =location.strip()
        print(location)
        if  location in town_list:
            risk_status = get_safety_status(location)
            print(risk_status)
            current_time=datetime.now() 
            with open ("safety_log.txt","a") as log_file:
                log_file.write(f"{current_time} | {location} | {risk_status}\n")  
                print(f"{current_time} | {location} | {risk_status}\n") 
        else:
            print("Not in the data base")
except FileNotFoundError: 
    print("location not found") 


       

    