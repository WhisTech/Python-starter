countries = [
    "India", "United States", "United Kingdom", "Canada",
    "Australia", "Japan", "China", "South Korea",
    "Germany", "France", "Italy", "Spain", "Portugal",
    "Brazil", "Argentina", "Mexico", "South Africa",
    "Nigeria", "Egypt", "Kenya", "Pakistan", "Bangladesh",
    "Nepal", "Sri Lanka", "Bhutan", "Thailand", "Vietnam",
    "Indonesia", "Malaysia", "Singapore", "Saudi Arabia",
    "United Arab Emirates", "Qatar", "Turkey", "Russia",
    "Ukraine", "Sweden", "Norway", "Switzerland", "New Zealand"
]

count =0  
list = []  
for i in countries:
    if i.startswith("I"):
        list.append(i)
        count = count+1

print(list)