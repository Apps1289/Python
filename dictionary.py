# Now, lets crave for dictionary in Python
# >> Dictionary: unordered and mutable
# >> comes in {key:value} pair

dict1 = {
    "Name":"abhi",
    "Age":19,
    "Branch":"CSE"
}
print(dict1)
print(dict1["Age"]) # can access values using keys
dict1["Name"] = "Rahul" # can change the value 
dict1["Surname"] = "Uranw" # can add new key value pairs

print(dict1)

# nested dictionary

info = {
    "Name" : "abc",
    "Subject" : {
        "Math": 90,
        "Science":85,
        "Social":80
    }
}
print(info)
print(info["Subject"])
print(info["Subject"]["Math"])

# Methods in Dictionary
# dict.keys() >> prints only key values
print(info.keys())
print(list(info.keys())) # typecasting> converting dict into list

# dict.values() >> prints only values
print(info.values())

#dict.items() > it gives tuples of key value pair
print(dict1.items())

#dict.get("key_name") > for accesing value same as dict["key_name"] but this way it doesn't give error if key is not available in the dictionary
#it gives none value
print(info.get("gender"))

# dict.update("key_value_pair") > for adding new key value pairs

