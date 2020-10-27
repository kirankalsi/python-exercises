file = open("teams.txt", "w")
teams = ['team1', 'team2', 'team3', 'team4', 'team5']
for team in teams:
        newline = team + "\n"
        file.write(newline)


file = open("teams.txt", "r")
lines = file.readlines()
print(lines[0])
print(lines[3])


original_lines = lines[1] + lines[2] + lines[3] + lines[4]
edited_line = "This is a new line \n"
file = open("teams.txt", "w")
file.write(edited_line + original_lines)


file = open("teams.txt", "r")
lines = file.readlines()
print(lines)