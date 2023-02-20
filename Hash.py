# numbers=[7,5,6,1,4,5,4,4,8,5,5,9,4,6,6,7,5,1,2,4]
#
# # print(len(numbers))
# #
# # print(sorted(numbers))
# #
# # print(sorted(numbers, reverse=True))
#
# number_set = set(numbers)
#
# print(number_set)
# #
# # print(len(number_set))
#
# rappers_real_name = {"Drake":"Aubrey Graham","The Weeknd":"Abel Tesfaye","21 savage":"Abraham Joseph","Travis Scott":"Jacques Bermon Webster","Kendrick Lamar":"Kendrick Lamar"}
# keys=rappers_real_name.keys()
#
# print(keys)
#
# values=rappers_real_name.values()
# print(values)
#
# items=rappers_real_name.items()
# print(items)
#
# drake_real_name = rappers_real_name["Drake"]
# print(drake_real_name)
# # print(len(rappers_real_name))

sports = {"Basketball" : 5, "Soccer" : 11, "Baseball" : 9, "Football" : 11, "Volleyball" : 6, "Golf" : 1, "Hockey" : 11, "Rugby" : 15}

# baseball = sports["Baseball"]
#
# print(baseball)

sports_list = list(sports.keys())

correct = False

while not correct:
    sports_name = input(f"Choose a sport from {sports_list} ")
    error_message = "Please select a correct key"

    if sports_name in sports:
        correct = True
        print(f"{sports_name} has {sports[sports_name]} players playing at a given time")
    else:
        print(error_message)