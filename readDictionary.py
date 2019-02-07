import pickle
import operator

Country_Dictionary = pickle.load(open("Countries_.p", "rb"))

for key, value in sorted(Country_Dictionary.items(), key=operator.itemgetter(0)):
    print(key, value)

print(sum(Country_Dictionary.values()))