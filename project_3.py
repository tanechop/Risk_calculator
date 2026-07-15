

town_list={"Douala":82,"Yaounde":89,"Limbe":56,"Kribi":70,"Bamenda":60,"Nkongsamba":53,"Buea":71 ,"Bafoussam":61}
def get_safety_status(location_name:str) -> str:
    score = town_list[location_name]#the score represent the key
    if score > 60:
        return "safe"
    else:
        return"high Risk"
def main():
    location_list = []
    result_dictionary={}            
    for i in range(5):#the user input 5 values
        Location= input("Enter your Location : ")
        location_list.append(Location)
        if  Location in town_list:
            risk_status = get_safety_status(Location)
            result_dictionary[Location]=risk_status
            print(risk_status)
        else:
            print("Not in the data base")# if the user enter a value that is not in the our list
       
    print(result_dictionary)
    
if __name__ == "__main__":
    main()