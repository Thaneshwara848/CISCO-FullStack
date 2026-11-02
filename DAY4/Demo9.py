names=["Aachal","Brahmaiah","Darshan","Pavitra","Vijaylaskhmi","Darshan"];

print(names);

names.append("Danveer");        # append : it will add at last 
print(names);

names.insert(3,"Renukswamy");
print(names);

names.pop();
print(names );

names.remove("Renukswamy");
print(names)

names.sort();
print(names);

names.reverse();
print(names);

print("Teams Players / total Players  :" , len(names));

names.extend(["Ajith","Ranganath"]);
print(names);

print("Teams Players / total Players  :" , len(names));


