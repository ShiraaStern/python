import json
def ex1(file):
    with open(file, 'r') as f:
      content = f.read()
      arr= content.split()
      return len(arr)



print(ex1('Z:\יד תשפז\קלרמן טובה\python\lesson 4\one.txt'))


def ex3(dict):
    with open('data.json','w') as jsn:
        json.dump(dict,jsn)
    with open('data.json', 'r') as jsn:
        data=json.load(jsn)
        print(data)


dict = {'name': 'asd',
           'age': 12}
ex3(dict)
