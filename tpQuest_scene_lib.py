from sys import exit
from tpQuest_scene_dict import scene_dictionary
class Scene(object):
	def __init__(self):
		pass
		
	def enter(self):
		print("NOT IMPLEMENTED IN THE BASE CLASS - YOUR HEAD ASPLODE!")
		exit(1)
		
def getObjectName(obj):
	return str(type(obj)).split('.')[1][:-2]
		
class FrontParkingLot(Scene):
	def enter(self):
		descriptions = scene_dictionary[getObjectName(self)]['descriptions']
		actions = scene_dictionary[getObjectName(self)]['actions']
		npcs = scene_dictionary[getObjectName(self)]['npcs']
		
		print(descriptions['enter']% getObjectName(self))
		input("\tpress any key")
		return 'finished'
		
class BackParkingLot(Scene):
	def enter(self):
		descriptions = scene_dictionary[getObjectName(self)]['descriptions']
		actions = scene_dictionary[getObjectName(self)]['actions']
		npcs = scene_dictionary[getObjectName(self)]['npcs']
		
		print(descriptions['enter']% getObjectName(self))
		input("\tpress any key")
		return 'finished'
		
class Finished(Scene):
	def enter(self):
		descriptions = scene_dictionary[getObjectName(self)]['descriptions']
		actions = scene_dictionary[getObjectName(self)]['actions']
		npcs = scene_dictionary[getObjectName(self)]['npcs']
		
		print(descriptions['enter']% getObjectName(self))
		exit(1)
	
	