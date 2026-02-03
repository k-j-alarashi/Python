university = {
    100:{
        "name":"Khaled",
        "age":24,
        "subjects":{
            1:"python",
            2:"c++"
            }
        },
    200:{
        "name":"Ahmed",
        "age":23,
        "subjects":{
            1:"html",
            2:"css"
            }
        },
    }

print(university) # طباعة كل dict
print("===============================")
print(university.get(100)) # طباعة dict الداخلي الذي قيمة key الخاص به 100
print("===============================")
print(university.get(100).get("name"))
print("===============================")
print(university.get(100).get("subjects"))
print("===============================")
print(university.get(100).get("subjects").get(1))
print("===============================")