def config(path, asset_name, root_path):
    e_config = {
        "exportShaderParams": False,
        "exportPath": path,
        "defaultExportPreset" : "Guerilla",
        "exportPresets": [{
            "name": "Guerilla",
            "maps": [{
                "fileName": f"{asset_name}_BaseColor(.$udim)",
                "channels": [{
                    "destChannel": "R",
                    "srcChannel": "R",
                    "srcMapType": "documentMap",
                    "srcMapName": "basecolor"
                },
                {
                    "destChannel": "G",
                    "srcChannel": "G",
                    "srcMapType": "documentMap",
                    "srcMapName": "basecolor"
                },
                {
                    "destChannel": "B",
                    "srcChannel": "B",
                    "srcMapType": "documentMap",
                    "srcMapName": "basecolor"
                },
                ],
                "parameters": {
                    "fileFormat" : "png",
                    "bitDepth" : "16",
                    "dithering": True,
                    "paddingAlgorithm": "infinite"
                }
            },
                {
                    "fileName": f"{asset_name}_Metalness(.$udim)",
                    "channels": [{
                        "destChannel": "L",
                        "srcChannel": "L",
                        "srcMapType": "documentMap",
                        "srcMapName": "metallic"
                    }],
                    "parameters": {
                        "fileFormat" : "png",
                        "bitDepth" : "16",
                        "dithering": True,
                        "paddingAlgorithm": "infinite"
                    }
                },
                {
                    "fileName": f"{asset_name}_Roughness(.$udim)",
                    "channels": [{
                        "destChannel": "R",
                        "srcChannel": "R",
                        "srcMapType": "documentMap",
                        "srcMapName": "roughness"
                    }],
                    "parameters": {
                        "fileFormat" : "png",
                        "bitDepth" : "16",
                        "dithering": True,
                        "paddingAlgorithm": "infinite"
                    }
                },
                {
                    "fileName": f"{asset_name}_Normal(.$udim)",
                    "channels": [{
                        "destChannel": "R",
                        "srcChannel": "R",
                        "srcMapType": "virtualMap",
                        "srcMapName": "Normal_OpenGL"
                    },
                        {
                            "destChannel": "G",
                            "srcChannel": "G",
                            "srcMapType": "virtualMap",
                            "srcMapName": "Normal_OpenGL"
                        },
                        {
                            "destChannel": "B",
                            "srcChannel": "B",
                            "srcMapType": "virtualMap",
                            "srcMapName": "Normal_OpenGL"
                        },
                    ],
                    "parameters": {
                        "fileFormat" : "png",
                        "bitDepth" : "16",
                        "dithering": True,
                        "paddingAlgorithm": "infinite"
                    }
                },
                {
                    "fileName": f"{asset_name}_Height(.$udim)",
                    "channels": [{
                        "destChannel": "R",
                        "srcChannel": "R",
                        "srcMapType": "documentMap",
                        "srcMapName": "height"
                    }],
                    "parameters":{
                        "fileFormat" : "png",
                        "bitDepth" : "16",
                        "dithering": True,
                        "paddingAlgorithm": "infinite"
                    }
                }]
        }],
        "exportList": [{
            "rootPath": root_path,
        }],
        "exportParameters": []
    }

    return e_config
