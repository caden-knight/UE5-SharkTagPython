import unreal

AssetTools = unreal.AssetToolsHelpers.get_asset_tools()
MaterialEditLibrary = unreal.MaterialEditingLibrary
EditorAssetLibrary = unreal.EditorAssetLibrary

# Create 2D texture param and connect to BASE COLOR
masterMaterial = AssetTools.create_asset("M_Master", "/Game/Py_MasterMaterials", unreal.Material, unreal.MaterialFactoryNew())

baseColorTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, -200)
MaterialEditLibrary.connect_material_property(baseColorTextureParam, "RGB", unreal.MaterialProperty.MP_BASE_COLOR)

# Create 2D texture param and connect to ROUGHNESS
roughnessTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -384, -200)
MaterialEditLibrary.connect_material_property(roughnessTextureParam, "RGB", unreal.MaterialProperty.MP_ROUGHNESS)

# Create constant value and connect to SPECULAR
specularTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionConstant, -125, 70)
specularTextureParam.set_editor_property("R", 0.3)
MaterialEditLibrary.connect_material_property(specularTextureParam, "", unreal.MaterialProperty.MP_SPECULAR)

# Create 2D texture param and connect to NORMAL
normalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, -25)
MaterialEditLibrary.connect_material_property(normalTextureParam, "RGB", unreal.MaterialProperty.MP_NORMAL)

# Create 2D texture param and connect to METALLIC
metalTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, -25)
MaterialEditLibrary.connect_material_property(metalTextureParam, "RGB", unreal.MaterialProperty.MP_METALLIC)

# Create 2D texture param and connect to AO
aoTextureParam = MaterialEditLibrary.create_material_expression(masterMaterial, unreal.MaterialExpressionTextureSampleParameter, -125, -25)
MaterialEditLibrary.connect_material_property(aoTextureParam, "RGB", unreal.MaterialProperty.MP_AMBIENT_OCCLUSION)

EditorAssetLibrary.save_asset("/Game/Py_MasterMaterials/M_Master", True)

