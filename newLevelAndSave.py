import unreal

levelTools = unreal.Level
editorLevelLibrary = unreal.EditorLevelLibrary
levelSubsys = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)

# init new level
newLevel = "myNewLevel"

# create new level
myNewLevel = levelSubsys.new_level("/Game/PyLevels/newLevel")

# save level
levelSubsys.save_current_level()