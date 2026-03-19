# dictionary in python
dctnry={ 
    "name": "urwa",
    "subjects": {
        "maths": "nice",
        "othes": "flop",
    },
    "age":21,
}
print(dctnry)
print(dctnry["subjects"])
print(list(dctnry.keys()))
print(dctnry.values())
print(list(dctnry.values()))
pairs=(list(dctnry.items()))
print(pairs[0])
print(dctnry.get("name"))
dctnry.update({"city":"isl","age":23})
print(dctnry)