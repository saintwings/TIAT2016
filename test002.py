from configobj import ConfigObj

colorName = ["black","blue","brown","cyan","gray","green",
                                              "magenta","orange","pink","red","white","yellow",
                                              "color1","color2","color3","color4","color5"]
dataInfo = ['ID', "Name", "RenderColor_RGB","MinArea_pixels","H_max","H_Min","S_Max","S_Min","V_Max","V_Min"]

config = ConfigObj("colorfile2.ini")


print config['ColorDefinitions']['black']['Name']