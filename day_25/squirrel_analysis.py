import pandas

data= pandas.read_csv("C:\\pyt\\day_25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")



c1 = data[data["Primary Fur Color"]  == "Gray"]["Unique Squirrel ID"].count()
c2 = data[data["Primary Fur Color"]  == "Cinnamon"]["Unique Squirrel ID"].count()
c3 = data[data["Primary Fur Color"]  == "Black"]["Unique Squirrel ID"].count()
# jj=c["Unique Squirrel ID"].count()


print(c1)
print(c2)
print(c3)


dict = {"fur_color" : ["Gray","Cinnamon", "Black"] ,
        "Count" : [c1,c2,c3]  }

print(pandas.DataFrame(dict))
