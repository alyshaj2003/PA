#Alysha Johnson, sqt6hx

player_info = input ("What player would you like to calculate statistics for? ")
team_info = input ("What team was the opponent in the game you would like to calculate statistics for? ")
three_attempt = input("How many 3's did "+ player_info + " attempt this game? ")
three_made = input("How many 3's did " + player_info + " make this game? ")
two_attempt = input("How many 2's did "+ player_info + " attempt this game? ")
two_made = input("How many 2's did "+ player_info + " make this game? ")
free_attempt = input("How many free throws did "+ player_info + " attempt this game? ")
free_made = input("How many free throws did "+ player_info + " make this game? ")

print(player_info,"had a", ((( str( ((int(two_made) + (int(three_made))) / ((int(two_attempt) + (int(three_attempt))))*100) ) ) + "%" )) , "field goal percentage and a", (str( (int(free_made) / (int(free_attempt)))*100)) + "%", "free throw percentage")
print(player_info,"scored",(int(two_made) * 2) + (int(three_made)*3) + (int(free_made)*1), "points against",team_info + ".","Wahoowa!")
