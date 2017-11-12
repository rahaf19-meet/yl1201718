import random
class Person(object):
	def __init__(self,name,age,city,gender):
		self.name=name
		self.age=age
		self.city=city
		self.gender=gender
	def eat(self,breakfast):
		print(self.name + " is enjoying eating "+ breakfast)
	def sing(self,song):
		print("alice is singing " +song)
alice=Person("Alice","15","jerusalem","female")
alice.eat("pancakes")
alice.sing("Let it go ")

class Song(object):
	def __init__(self,lyrics):
		self.lyrics=lyrics
	def sing_me_a_song(self):
		for value in range(len(self.lyrics)):

			a=random.randint(0,len(self.lyrics))
			if a==0:
				print(self.lyrics[a])
			if a==1:
				print(self.lyrics[a])
			if a==2:
				print(self.lyrics[a])



flower= Song(["Roses are red, ","Violets are blue, ", "I wrote this poem for you. "])
flower.sing_me_a_song()