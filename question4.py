#making the array of youtubers
yt_list = ["Pewdipie", "Wallibear", "Markiplier", "MrsOki", "MrBeats", "Belle Deplhine", "KSI", "Vikkstar123", "Manny",
           "Zerkaa", "Pokimane","CarryMinati2","Total Gaming","Ashish Chanchlani Vines","BB Ki Vines","Round2Hell","Amit Bhadana"]
#taking strings input from the user to generate a suitable yt name
x = input("Enter your first string")
y = input("Enter your second string")
z = input("Enter your third string")

x = x[0]
y = y[0]
z = z[0]
i = 0
#printing the ytber name
for i in range(len(yt_list)):
    if x in yt_list[i] and y in yt_list[i] and z in yt_list[i]:
        print(yt_list[i])

