import sqlite3

from census_data import Cencus_data 

conn = sqlite3.connect(':memory:')

c = conn.cursor()

c.execute("""CREATE TABLE cencus_data (
			COMMUNITY_AREA_NUMBER integer,
			COMMUNITY_AREA_NAME text,
			PECENTAGE_HOUSING_CROWDED integer,
			PERCENTAGE_OF_HOUSEHOLD_BELOW_POVERTY integer,
			PERCENTAGE_AGE_16_UNEMPLOYED integer,
			PERCENTAGE_25_WITHOUT_HIGH_SCHOOL_DIPLOMA integer,
			PERCENTAGE_AGED_UNDER_18_OR_OVER_64 integer,
			PER_CAPITA_INCOME integer,
			HARDSHIP_INDEX integer
			)""")


def insert_cen(cen):
    with conn:
    	c.execute("INSERT INTO cencus_data VALUES (:COMMUNITY_AREA_NUMBER, :COMMUNITY_AREA_NAME, :PECENTAGE_HOUSING_CROWDED, :PERCENT_HOUSEHOLDS_BELOW_POVERTY, :PERCENT_AGED_16__UNEMPLOYED, :PERCENT_AGED_25__WITHOUT_HIGH_SCHOOL_DIPLOMA, :PERCENT_AGED_UNDER_18_OR_OVER_64, :PER_CAPITA_INCOME, :HARDSHIP_INDEX)", 
    		{
    		'community_area_number': cen.cummunity_area_number,
    		'community_area_name': cen.community_area_name, 
    		'percent_of_housing_crowded': cen.pencent_area_number,
    		'percent_households_below_poverty': cen.pecent_households_below_poverty,
    		'percent_aged_16_unemployed': cen.pecent_aged_16_unemployed,
    		'percent_aged_25_without_high_school_diploma': cen.pecent_aged_25_without_high_school_diploma,
    		'percent_aged_under_18_or_over_64': cen.pecent_aged_under_18_or_over_64,
    		'per_capita_income': cen.per_capital_income,
    		'hardship_index': cen.hardship_index
    		}
    		)

cen_1 = Cencus_data(1, 'Rogers Park', 7.7, 23.6, 8.7, 18.2, 27.5, 23939, 39)
cen_2 = Cencus_data(2, 'West Ridge', 7.8, 17.2, 8.8, 20.8, 38.5, 23040, 46)
cen_3 = Census_data(3, 'Uptown', 3.8, 24.0, 8.9, 11.8, 22.2, 35787, 20)
cen_4 = Census_data(4, 'Lincoln Square', 3.4, 10.9, 8.2, 13.4, 25.5, 37524, 17)
cen_5 = Census_data(5, 'North Center', 0.3, 7.5, 5.2, 4.5, 26.2, 57123, 6)
cen_6 = Census_data(6, 'Lake View', 1.1, 11.4, 4.7, 2.6, 17.0, 60058, 5)
cen_7 = Census_data(7, 'Lincoln Park', 0.8, 12.3, 5.1, 3.6, 21.5, 71551, 2)
cen_8 = Census_data(8, 'Near North Side', 1.9, 12.9, 7.0, 2.5, 22.6, 88669, 1)
cen_9 = Census_data(9, 'Edison Park', 1.1, 3.3, 6.5, 7.4, 35.3, 40959, 8)
cen_10 = Census_data(10, 'Norwood Park', 2.0, 5.4, 9.0, 11.5, 39.5, 32875, 21)
cen_11 = Census_data(11, 'Jefferson Park', 2.7, 8.6, 12.4, 13.4, 35.5, 27751, 25)
cen_12 = Census_data(12, 'Forest Glen', 1.1, 7.5, 6.8, 4.9, 40.5, 44164, 11)
cen_13 = Census_data(13, 'North Park', 3.9, 13.2, 9.9, 14.4, 39.0, 26576, 33)
cen_14 = Census_data(14, 'Albany Park', 11.3, 19.2, 10.0, 32.9, 32.0, 21323, 53)
cen_15 = Census_data(15, 'Portage Park', 4.1, 11.6, 12.6, 19.3, 34.0, 24336, 35)
cen_16 = Census_data(16, 'Irving Park', 6.3, 13.1, 10.0, 22.4, 31.6, 27249, 34)
cen_17 = Census_data(17, 'Dunning', 5.2, 10.6, 10.0, 16.2, 33.6, 26282, 28)
cen_18 = Census_data(18, 'Montclaire', 8.1, 15.3, 13.8, 23.5, 38.6, 22014, 50)
cen_19 = Census_data(19, 'Belmont Cragin', 10.8, 18.7, 14.6, 37.3, 37.3, 15461, 70)
cen_20 = Census_data(20,'Hermosa', 6.9, 20.5, 13.1, 41.6, 36.4, 15089, 71)
cen_21 = Census_data(21, 'Avondale', 6.0, 15.3, 9.2, 24.7, 31.0, 20039, 42)
cen_22 = Census_data(22, 'Logan Square', 3.2, 16.8, 8.2, 14.8, 26.2, 31908, 23)
cen_23 = Census_data(23, 'Humboldt park', 14.8, 33.9, 17.3, 35.4, 38.0, 13781, 85)
cen_24 = Census_data(24, 'West Town', 2.3, 14.7, 6.6, 12.9, 21.7, 43198, 10)
cen_25 = Census_data(25, 'Austin', 6.3, 28.6, 22.6, 24.4, 37.9, 15957, 73)
cen_26 = Census_data(26,'West Garfield Park',9.4, 41.7, 25.8, 24.5, 43.6, 10934, 92)
cen_27 = Census_data(27, 'East Garfield Park', 8.2, 42.4, 19.6, 21.3, 43.2, 12961, 83)
cen_28 = Census_data(28, 'Near West Side',3.8, 20.6, 10.7, 9.6, 22.2, 44689, 15)
cen_29 = Census_data(29, 'North Lawndale', 7.4, 43.1, 21.2, 27.6, 42.7, 12034, 87)
cen_30 = Census_data(30,'South Lawndale', 15.2, 30.7, 15.8, 54.8, 33.8, 10402, 96)
cen_31 = Census_data(31, 'Lower West Side', 9.6, 25.8, 15.8, 40.7, 32.6, 16444, 76)
cen_32 = Census_data(32, 'Loop',1.5, 14.7, 5.7, 3.1, 13.5, 65526, 3)
cen_33 = Census_data(33, 'Near South Side', 1.3, 13.8, 4.9, 7.4, 21.8, 59077, 7)
cen_34 = Census_data(34, 'Armour Square', 5.7, 40.1, 16.7, 34.5, 38.3, 16148, 82)
cen_35 = Census_data(35, 'Douglas', 1.8, 29.6, 18.2, 14.3, 30.7, 23791, 47)
cen_36 = Census_data(36, 'Oakland', 1.3, 39.7, 28.7, 18.4, 40.4, 19252, 78)
cen_37 = Census_data(37, 'Fuller Park', 3.2, 51.2, 33.9, 26.6, 44.9, 10432, 97)
cen_38 = Census_data(38, 'Grand Boulevard', 3.3, 29.3, 24.3, 15.9, 39.5, 23472, 57)
cen_39 = Census_data(39, 'Kenwood', 2.4, 21.7, 15.7, 11.3, 35.4, 35911, 26)
cen_40 = Census_data(40, 'Washington Park', 5.6, 42.1, 28.6, 25.4, 42.8, 13785, 88)
cen_41 = Census_data(41, 'Hyde Park', 1.5, 18.4, 8.4, 4.3, 26.2, 39056, 14)
cen_42 = Census_data(42, 'Woodlawn', 2.9, 30.7, 23.4, 16.5, 36.1, 18672, 58)
cen_43 = Census_data(43, 'South Shore', 2.8, 31.1, 20.0, 14.0, 35.7, 19398, 55)
cen_44 = Census_data(44, 'Chatham', 3.3, 27.8, 24.0, 14.5, 40.3, 18881, 60)
cen_45 = Census_data(45, 'Avalon Park', 1.4, 17.2, 21.1, 10.6, 39.3, 24454, 41)
cen_46 = Census_data(46, 'South Chicago', 4.7, 29.8, 19.7, 26.6, 41.1, 16579, 75)
cen_47 = Census_data(47, 'Burnside', 6.8, 33.0, 18.6, 19.3, 42.7, 12515, 79)
cen_48 = Census_data(48, 'Calumet Heights', 2.1, 11.5, 20.0, 11.0, 44.0, 28887, 38)
cen_49 = Census_data(49, 'Roseland', 2.5, 19.8, 20.3, 16.9, 41.2, 17949, 52)
cen_50 = Census_data(50, 'Pullman', 1.5, 21.6, 22.8, 13.1, 38.6, 20588, 51)
cen_51 = Census_data(51, 'South Deering', 4.0, 29.2, 16.3, 21.0, 39.5 ,14685, 65)
cen_52 = Census_data(52, 'East Side' ,6.8, 19.2, 12.1, 31.9, 42.8, 17104, 64)
cen_53 = Census_data(53, 'West Pullman', 3.3, 25.9, 19.4, 20.5, 42.1, 16563, 62)
cen_54 = Census_data(54, 'Riverdale', 5.8, 56.5, 34.6, 27.5, 51.5, 8201, 98)
cen_55 = Census_data(55, 'Hegewisch', 3.3, 17.1, 9.6, 19.2, 42.9, 22677, 44)
cen_56 = Census_data(56, 'Garfield Ridge', 2.6, 8.8, 11.3, 19.3, 38.1, 26353, 32)
cen_57 = Census_data(57, 'Archer Heights', 8.5, 14.1, 16.5, 35.9, 39.2, 16134, 67)
cen_58 = Census_data(58, 'Brighton Park', 14.4, 23.6, 13.9, 45.1, 39.3, 13089, 84)
cen_59 = Census_data(59, 'McKinley Park', 7.2, 18.7, 13.4, 32.9, 35.6, 16954, 61)
cen_60 = Census_data(60, 'Bridgeport', 4.5, 18.9, 13.7, 22.2, 31.3, 22694, 43)
cen_61 = Census_data(61, 'New City', 11.9, 29.0, 23.0, 41.5, 38.9, 12765, 91)
cen_62 = Census_data(62, 'West Elsdon', 11.1, 15.6, 16.7, 37.0, 37.7, 15754, 69)
cen_63 = Census_data(63, 'Gage Park', 15.8, 23.4, 18.2, 51.5, 38.8, 12171, 93)
cen_64 = Census_data(64, 'Clearing', 2.7, 8.9, 9.5, 18.8, 37.6, 25113, 29)
cen_65 = Census_data(65, 'West Lawn', 5.8, 14.9, 9.6, 33.6, 39.6, 16907, 56)
cen_66 = Census_data(66, 'Chicago Lawn', 7.6, 27.9, 17.1, 31.2, 40.6, 13231, 80)
cen_67 = Census_data(67, 'West Englewood', 4.8, 34.4, 35.9, 26.3, 40.7, 11317, 89)
cen_68 = Census_data(68, 'Englewood', 3.8, 46.6, 28.0, 28.5, 42.5, 11888, 94)
cen_69 = Census_data(69, 'Greater Grand Crossing', 3.6, 29.6, 23.0, 16.5, 41.0, 17285, 66)
cen_70 = Census_data(70, 'Ashburn' ,4.0, 10.4, 11.7, 17.7, 36.9, 23482, 37)
cen_71 = Census_data(71, 'Auburn Gresham', 4.0, 27.6, 28.3, 18.5, 41.9, 15528, 74)
cen_72 = Census_data(72, 'Beverly', 0.9, 5.1, 8.0, 3.7, 40.5, 39523, 12)
cen_73 = Census_data(73, 'Washington Height', 1.1, 16.9, 20.8, 13.7, 42.6, 19713, 48)
cen_74 = Census_data(74, 'Mount Greenwood', 1.0, 3.4, 8.7, 4.3, 36.8, 34381, 16)
cen_75 = Census_data(75, 'Morgan Park', 0.8, 13.2, 15.0, 10.8, 40.3, 27149, 30)
cen_76 = Census_data(76, 'O"Hare', 3.6, 15.4, 7.1, 10.9, 30.3, 25828, 24)
cen_77 = Census_data(77, 'Edgewater', 4.1, 18.2, 9.2, 9.7, 23.8, 33385, 19)


insert_cen(cen_1)
insert_cen(cen_2)
insert_cen(cen_3)
insert_cen(cen_4)
insert_cen(cen_5)
insert_cen(cen_6)
insert_cen(cen_7)
insert_cen(cen_8)
insert_cen(cen_8)
insert_cen(cen_9)
insert_cen(cen_10)
insert_cen(cen_11)
insert_cen(cen_12)
insert_cen(cen_13)
insert_cen(cen_14)
insert_cen(cen_15)
insert_cen(cen_16)
insert_cen(cen_17)
insert_cen(cen_18)
insert_cen(cen_19)
insert_cen(cen_20)
insert_cen(cen_21)
insert_cen(cen_22)
insert_cen(cen_23)
insert_cen(cen_24)
insert_cen(cen_25)
insert_cen(cen_26)
insert_cen(cen_27)
insert_cen(cen_28)
insert_cen(cen_29)
insert_cen(cen_30)
insert_cen(cen_31)
insert_cen(cen_32)
insert_cen(cen_33)
insert_cen(cen_34)
insert_cen(cen_35)
insert_cen(cen_36)
insert_cen(cen_37)
insert_cen(cen_38)
insert_cen(cen_39)
insert_cen(cen_40)
insert_cen(cen_41)
insert_cen(cen_42)
insert_cen(cen_43)
insert_cen(cen_44)
insert_cen(cen_45)
insert_cen(cen_46)
insert_cen(cen_47)
insert_cen(cen_48)
insert_cen(cen_49)
insert_cen(cen_50)
insert_cen(cen_51)
insert_cen(cen_52)
insert_cen(cen_54)
insert_cen(cen_55)
insert_cen(cen_56)
insert_cen(cen_57)
insert_cen(cen_58)
insert_cen(cen_59)
insert_cen(cen_60)
insert_cen(cen_61)
insert_cen(cen_62)
insert_cen(cen_63)
insert_cen(cen_64)
insert_cen(cen_65)
insert_cen(cen_66)
insert_cen(cen_67)
insert_cen(cen_68)
insert_cen(cen_69)
insert_cen(cen_70)
insert_cen(cen_71)
insert_cen(cen_72)
insert_cen(cen_73)
insert_cen(cen_74)
insert_cen(cen_75)
insert_cen(cen_76)
insert_cen(cen_77)
insert_cen(cen_78)
insert_cen(cen_79)
insert_cen(cen_80)
insert_cen(cen_81)
insert_cen(cen_11)
insert_cen(cen_12)
insert_cen(cen_13)





















