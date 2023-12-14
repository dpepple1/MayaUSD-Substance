from pxr import Usd, UsdShade

stage = Usd.Stage.CreateNew("demoMaterial.usda")

material = UsdShade.Material.Define(stage, '/mtl/demoMat')
shader = UsdShade.Shader.Define(stage, "/mtl/demoMat/demoSurface")
shader.CreateIdAttr('UsdPreviewSurface')

material.CreateSurfaceOutput().ConnectToSource(shader.ConnectableAPI(), "surface")

stage.Save()