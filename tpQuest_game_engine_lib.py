from tpQuest_scene_lib import *
from tpQuest_scene_dict import GetScenesListForMap
from random import randint

def GetStartScene():
	if randint(0,9) < 5:
		start_scene = 'FrontParkingLot'
	else:
		start_scene = 'BackParkingLot'
	return start_scene
	
class Map(object):
	scenes = GetScenesListForMap()
	print(scenes)
	def __init__(self,start_scene):
		self.start_scene = start_scene
		intro = """\n\tIt's %d:00 and you have a hankerin' for some high quality, hand rolled, 
	Dominican goodness. What better venue to sate this proclivity for all things 
	Nicotiana tabacum than the paragon of <insert assinine noun here>, Tobacco Plus? \n"""
		start_time=randint(9,12)
		print(intro % start_time)
		
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)
		
	def opening_scene(self):
		return self.next_scene(self.start_scene)
		
class Game(object):
	def __init__(self, scene_map):
		self.scene_map = scene_map
		
	def play(self):
		# Get opening scene, and set winning condition
		current_scene = self.scene_map.opening_scene()
		last_scene = self.scene_map.next_scene('finished')
		
		while current_scene != last_scene:
			next_scene_name = current_scene.enter()
			current_scene = self.scene_map.next_scene(next_scene_name)

		# be sure to print out the last scene
		current_scene.enter()
