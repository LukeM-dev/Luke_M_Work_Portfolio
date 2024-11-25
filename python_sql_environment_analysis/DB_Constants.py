
DATABASE_NAMES = {
    'environ': 'EnvironmentalConditions'
}

TABLE_TEMPLATES = {
    'EnvironData': (
        """CREATE TABLE `{tb_name}` (
         `key` INT(10) NOT NULL AUTO_INCREMENT,
         `entry_no` INT(5) NOT NULL,
         `entry_datetime` DATETIME NOT NULL,
         `temp_F` FLOAT(10),
         `rh_percent` FLOAT(10),
         `dew_point_F` FLOAT(10),
         PRIMARY KEY (`key`), UNIQUE KEY (`key`)
        );"""
    ),
    'LocationMap': (
        """CREATE TABLE `{tb_name}` (
         `location_id` int(5) NOT NULL, 
         `location_description` text(100), 
         PRIMARY KEY (`location_id`), 
        );"""
    )
}

TABLE_NAMES = [
    'EnvironData',
    'LocationMap'
]

ENVIRON_TABLE_LOCATION_MAPPING = {
    '21999191': 'Outdoors – Courtyard Door Overhang',
    '21611332': 'Tub Room 2041',
    '21611333': 'Hallway 600 on Linen room door frame',
    '21611336': 'Resident Room 605 on Bathroom door frame',
    '21611334': 'Crawlspace - 900 Below occupied wing',
    '21611335': 'Crawlspace - 600 Below occupied wing',
    '21611337': 'Crawlspace - 500 Below occupied wing',
    '21611338': 'APc 2000 – Just inside access door on conduit'
}

USR_CONFIG = {
    'host': "localhost",  # Change if not using Localhost
    'user': "std",
    'password': "Fate_Panel_Kick",
}
