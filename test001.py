from configobj import ConfigObj

colorName = ["black","blue","brown","cyan","gray","green",
                                              "magenta","orange","pink","red","white","yellow",
                                              "color1","color2","color3","color4","color5"]
dataInfo = ['ID', "Name", "RenderColor_RGB","MinArea_pixels","H_max","H_Min","S_Max","S_Min","V_Max","V_Min"]

config = ConfigObj()
config.filename = "colorfile2.ini"
#
config['ColorDefinitions'] = {}
for i in colorName:
    config['ColorDefinitions'][i] = {}
    for j in dataInfo:
        config['ColorDefinitions'][i][j] = 0

# config['section1']['keyword3'] = 2
# config['section1']['keyword4'] = 3
# #
# section2 = {
#     'keyword5': 4,
#     'keyword6': 5,
#     'sub-section': {
#         'keyword7': 6
#         }
# }
# config['section2'] = section2
# #
# config['section3'] = {}
# config['section3']['keyword 8'] = [7, 8, 9]
# config['section3']['keyword 9'] = [10, 11, 12]
#
config.write()