#file we set the options for the game, such as colors, screen resolution, etc.
#we can use the name of this colors in all the oter files
# Config file used to set global variables and other settings

# COLORS
dark_red = (138, 0, 0)  # Dark red for buttons
deep_black = (19, 20, 20)  # Almost black for background
grey = (59, 60, 60)  # Dark grey for alternate buttons
white = (254, 255, 255)  # White for readable text
glowing_light_red = (239, 128, 128)  # Light red for brighter text
red = (255, 0, 0)  # Red for errors
green = (0, 255, 0)  # Green for success
blue = (0, 0, 255)  # Blue for info
yellow = (255, 255, 0)  # Yellow for warnings


# SCREEN DETAILS
resolution = (720, 720)
width, height = resolution[0], resolution[1] #for calculations
fps = 60

#SIZES
player_size = 64 #(50,100)
enemy_size = 64 #40
projectile_size = 6  #10