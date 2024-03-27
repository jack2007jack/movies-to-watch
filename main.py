
import json


def myfunc(thislist):
  return thislist["rating"]


f = open('movies.json',)
movies = json.load(f)
f.close()



movies = []

# read movies file into variable
with open('movies.json', 'r') as openfile:
    # Reading from json file
    movies = json.load(openfile)

while True:
    print("\nMovie Tracker Menu:")
    print("1. Pievienot filmu")
    print("2. Rādīt visas pievienotas filmas sakartotas pēc reitinga")
    print("3. Rādīt vēl neskatītās filmas")
    print("4. Atzimēt filmu kā skatītu")
    print("5. Dzēst filmu no saraksta")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        movies_top= {}
        movies_top["title"]=input("Enter movie title: ") 
        movies_top["rating"]=float(input("Enter movie rating:"))
        movies_top["watched"]= False
        movies.append(movies_top)     
        print(movies)
        pass
    elif choice == "2":
        thislist = movies.copy()
        thislist.sort(key=myfunc, reverse = True)
        print(thislist)
        pass
    elif choice == "3":
        newlist = [x for x in movies if x["watched"]== False]
        print(newlist)
        pass
    elif choice == "4":
        id = int(input("Enter the index of the movie to mark: "))
        movies[id]["watched"] = True
    elif choice == "5":
        id = int(input("Enter the index of the movie to remove: "))
        movies.pop(id)
        print(movies)
    elif choice == "6":
        print("Exiting...")
        with open("movies.json", "w") as outfile:
            json.dump(movies, outfile)
        break
    else:
        print("Invalid choice. Please try again.")

# writing movies to file
with open("movies.json", "w") as movies_file:
    json.dump(movies, movies_file)