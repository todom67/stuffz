from tpQuest_scene_lib import * 
scene_dictionary = {
	'FrontParkingLot':{
		'descriptions':{'enter':"""\n%s\n\tThis is the front door!""",},
		'actions': ["enter","help"],
		'npcs': ["Smoke","Tim Callahan"],
	},
	'BackParkingLot':{
		'descriptions': {'enter':"""\n%s\n\tThis is the back door!""",},
		'actions': ["enter","help"],
		'npcs': ["Rami","Teh owner of the nail salon"],
	},
	'Finished':{
		'descriptions': {'enter':"""\n%s\n\tWE'RE THROUGH!!!!!""",},
		'actions': ["enter","help"],
		'npcs': ["Smoke","Tim Callahan"],
	}
}

def GetScenes():
	return scene_dictionary.keys().sort()
	
def GetScenesListForMap():
	scenes_list = {}
	for key in scene_dictionary.keys():
		print(key)
		scenes_list[key] = getattr(Scene(key),'enter')
	return scenes_list