myDictionary = {
    "one" : {
        "name" : "Mabel",
        "last name" : "Karani"
    },

    "two": {
        "career" : "DATA SCIENCE ENGINEER",
        "Position": "Lead data scientist"

    }
}
for i in myDictionary:
    for j in myDictionary[i]:
        print( j,":", myDictionary[i][j])