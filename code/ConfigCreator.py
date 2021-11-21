import configparser

config = configparser.ConfigParser()

config.add_section("Scheduling Parameters")
config.set("Scheduling Parameters", "bin_size", "20")
config.set("Scheduling Parameters", "mla", "9999")
config.set("Scheduling Parameters", "config_ratio", "0.0")
config.set("Scheduling Parameters", "n_tasks", "5")
config.set("Scheduling Parameters", "max_exec_time", "20")

with open(r"C:\Users\saiak\PycharmProjects\VimanTest\config.ini", 'w') as configfile:
    config.write(configfile)
