SHIP_TYPES = ["corvette", "destroyer", "cruiser", "battleship", "titan","platform", "starbase"]
REACTOR_TYPES = ["fission", "fusion", "cold_fusion", "antimatter", "zero_point", "dark_matter"]
SIZE_RESTRICTIONS = {"corvette"    : "corvette colonizer lithoid_colonizer sponsored_colonizer constructor science transport crisis_corvette",
                     "destroyer"   : "destroyer crisis_destroyer", 
                     "cruiser"     : "destroyer crisis_destroyer",
                     "battleship"  : "battleship", 
                     "titan"       : "titan",
                     "platform"    : "military_station_small military_station_medium military_station_large",
                     "starbase"    : "starbase_outpost starbase_starport starbase_starhold starbase_starfortress starbase_citadel juggernaut"}

pwr = {"corvette"    :  {"fission" : 75,   "fusion" : 100,  "cold_fusion" : 130,  "antimatter" : 170,  "zero_point" : 220,  "dark_matter" : 285},
       "destroyer"   :  {"fission" : 140,  "fusion" : 180,  "cold_fusion" : 240,  "antimatter" : 320,  "zero_point" : 430,  "dark_matter" : 550},
       "cruiser"     :  {"fission" : 280,  "fusion" : 360,  "cold_fusion" : 480,  "antimatter" : 620,  "zero_point" : 800,  "dark_matter" : 1030},
       "battleship"  :  {"fission" : 550,  "fusion" : 720,  "cold_fusion" : 950,  "antimatter" : 1250, "zero_point" : 1550, "dark_matter" : 2000},
       "titan"       :  {"fission" : 1100, "fusion" : 1450, "cold_fusion" : 1900, "antimatter" : 2500, "zero_point" : 3200, "dark_matter" : 4200},
       "starbase"    :  {"fission" : 1650, "fusion" : 2170, "cold_fusion" : 2850, "antimatter" : 3570, "zero_point" : 4550, "dark_matter" : 6200},
       "platform"    :  {"fission" : 200,  "fusion" : 260,  "cold_fusion" : 340,  "antimatter" : 440,  "zero_point" : 575,  "dark_matter" : 750}}      

cost = {"corvette"   : {"fission"  : 10,  "fusion"  : 13,  "cold_fusion"  : 17,  "antimatter"  : 22,  "zero_point"  : 28,  "dark_matter"  : 37},
        "destroyer"  : {"fission"  : 20,  "fusion"  : 26,  "cold_fusion"  : 34,  "antimatter"  : 44,  "zero_point"  : 56,  "dark_matter"  : 74},
        "cruiser"    : {"fission"  : 40,  "fusion"  : 52,  "cold_fusion"  : 68,  "antimatter"  : 88,  "zero_point"  : 112, "dark_matter"  : 148},
        "battleship" : {"fission"  : 80,  "fusion"  : 104, "cold_fusion"  : 136, "antimatter"  : 176, "zero_point"  : 224, "dark_matter"  : 296},
        "titan"      : {"fission"  : 160, "fusion"  : 208, "cold_fusion"  : 272, "antimatter"  : 352, "zero_point"  : 448, "dark_matter"  : 592},
        "starbase"   : {"fission"  : 0,   "fusion"  : 0,   "cold_fusion"  : 0,   "antimatter"  : 0,   "zero_point"  : 0,   "dark_matter"  : 0},
        "platform"   : {"fission"  : 20,  "fusion"  : 26,  "cold_fusion"  : 34,  "antimatter"  : 44,  "zero_point"  : 56,  "dark_matter"  : 74}} 

class Reactor:

     def __init__(self, reactor_type, ship_type):
        self.key = ship_type.upper() + "_" + reactor_type.upper() + "_REACTOR"
        self.size = "small" if ship_type != "platform" or ship_type != "starbase" else "large"
        self.icon = "GFX_ship_part_reactor_" + reactor_type
        self.power = pwr[ship_type][reactor_type]
        self.cost_alloys = cost[ship_type][reactor_type]
        self.upkeep_alloys = self.cost_alloys * 0.01
        self.upkeep_energy = self.cost_alloys * 0.10
        self.prerequisites = "tech_" + reactor_type + "_power"
        self.size_restriction = SIZE_RESTRICTIONS[ship_type]
        try:
            self.upgrades_to = ship_type.upper() + "_" + REACTOR_TYPES[REACTOR_TYPES.index(reactor_type)+1]
        except:
            self.upgrades_to = None
        
    def __str__(self):
        
        ret = ""
        ret += f"utility_component_template = {{\n"
        ret += f"\tkey = {self.key} \n" #	key = self.key
        ret += f"\tsize = {self.size} \n"
        ret += f"\ticon = {self.icon} \n"
        ret += f"\ticon_frame = 1\n"
        ret += f"\tpower = {self.power} \n"
        ret += f"\tresources = {{\n"
        ret += f"\t\tcategory = ship_components \n"
        ret += f"\t\tcost = {{\n"
        ret += f"\t\t\talloys = {self.power} \n"
        ret += f"\t\t}}\n"
        ret += f"\t\tupkeep = {{\n"
        ret += f"\t\t\tenergy = {self.upkeep_energy} \n"
        ret += f"\t\t\talloys = {self.upkeep_alloys} \n"
        ret += f"\t\t}}\n"
        ret += f"\t}}\n"
        ret += f"\n"
        ret += f"\tprerequisites = {{{ self.prerequisites}}} \n"
        ret += f"\tcomponent_set = 'power_core'\n"
        ret += f"\tsize_restriction = {{{ self.size_restriction }}} \n"
        ret += f"\tupgrades_to = {self.upgrades_to} \n"
        ret += f"\n"
        ret += f"\tai_weight = {{\n"
        ret += f"\t\tweight = 2\n"
        ret += f"\t	}}\n"
        ret += f"}}\n\n"
        return ret

with open("pw_reactors.txt", "w") as file:
    for reactor in REACTOR_TYPES:
        for ship in SHIP_TYPES:
                file.write(str(Reactor(reactor, ship)))
