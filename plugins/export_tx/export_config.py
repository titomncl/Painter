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
                    "srcMapName": "baseColor"
                },
                {
                    "destChannel": "G",
                    "srcChannel": "G",
                    "srcMapType": "documentMap",
                    "srcMapName": "baseColor"
                },
                {
                    "destChannel": "B",
                    "srcChannel": "B",
                    "srcMapType": "documentMap",
                    "srcMapName": "baseColor"
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
                        "srcMapName": "metalness"
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
                        "destChannel": "L",
                        "srcChannel": "L",
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
                        "srcMapType": "documentMap",
                        "srcMapName": "normal"
                    },
                        {
                            "destChannel": "G",
                            "srcChannel": "G",
                            "srcMapType": "documentMap",
                            "srcMapName": "normal"
                        },
                        {
                            "destChannel": "B",
                            "srcChannel": "B",
                            "srcMapType": "documentMap",
                            "srcMapName": "normal"
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
                        "destChannel": "L",
                        "srcChannel": "L",
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
