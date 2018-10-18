import json
from difflib import get_close_matches,SequenceMatcher
import pdb


def dictionary(search):
    data = json.load(open("data.json"))
    try:
        if search.upper() in data:
            str = data[search.upper()]
        else:
            str = data[search]
        for item in str:
            print(item)
    except:
        word = predict(search,data)
        value = similar(word[0],search)
        # pdb.set_trace()
        if value > 0.5:
            answer = input("Did you mean " + word[0] + " instead? Enter Y for yes and N for N :" + "\n")
            if answer == 'Y':
                str = data[word[0]]
                for item in str:
                    print(item)
        else:
            print("Word doesn't exsist. Please double check")

def predict(word,data):
    return get_close_matches(word,data.keys(),1)

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def main():
    search = input("Enter word: ")
    if search.isupper() != 1:
        search = search.lower()

    dictionary(search)


if __name__=="__main__":
	main()
