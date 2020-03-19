print "Selamat Datang di Mata Kuliah Network Programming"
print "Ini adalah program pertama anda."

x = raw_input("Masukkan Nama: ")
# y = raw_input("Masukkan NIM: ")

num = 0
for huruf in x:
    print huruf, " --> index[", num, "]"
    num = num + 1


data = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

d = set([x for x in data.keys()])
d

data = {'trends':[{'name': '#BeratKandili',
  'url': 'http://twitter.com/search?q=%23BeratKandili',
  'promoted_content': None,
  'query': '%23BeratKandili',
  'tweet_volume': 46373},
 {'name': '#GoodFriday',
  'url': 'http://twitter.com/search?q=%23GoodFriday',
  'promoted_content': None,
  'query': '%23GoodFriday',
  'tweet_volume': 81891}
]}

d = set([x for x in data['trends'][0]])
d

new_val = 100
def square(x):
  global new_val
  print(new_val)
  new_val = new_val + 10
  print()
  print(new_val)
  return new_val

square(5)

for n in range(2, 10):
  for x in range(2, n):
    if n % x == 0:
      print(n, 'equals', x, '*', n/x)
      break
  else:
    print(n, 'is a prime number')

for letter in 'Python':
  if letter == 'h':
    pass
    print('This is pass block')
  print('Current letter: {}'.format(letter))

list_a = range(1, 10, 2)
x = [[a**2, a**3] for a in list_a]
print(x)

print("Hello World") print("Welcome to Python")

a = 5.5
print(a, "is of type", type(a))

a=3; print(float(a))

animal = ['cat', 'rabbit', 'tiger', 'wolf']
del animal[1]
print(animal)

x = [10,15,20,25,30]
print(x[-3:])

for letter in 'Dicoding':
    if letter == 'd':
       break
          print('Current letter: {}'.format(letter))


class Building:
    def __init__(self, number):
        self.number = number

num = Building(100)
print(num.number)