__author__ = 'Avi'
from Database import *
import tableFunctions.Battle as battle
import tableFunctions.Character as character
import tableFunctions.Movie as movie

get_all()

'''Adding 1'''
battle.add_battle(1,'New York', 'Avengers vs Loki', 'kkgysv2')
character.add_character('Iron Man', 'Avenger', 1, 'Robert Downey Jr.')
character.add_character('Thor', 'Avenger', 1, 'Chris Hemsworth')
character.add_character('Captain America', 'Avenger', 1, 'Chris Evans (actor)')
character.add_character('Hulk', 'Avenger', 1, 'Mark Ruffalo')
character.add_character('Loki', 'Asgardian', 1, 'Tom Hiddleston')
character.add_character('Hawkeye', 'Avenger', 1, 'Jeremy Renner')
movie.add_movie('The Avengers', 2012, 4,1 )
'''Adding 2'''
battle.add_battle(2,'Washington DC', 'John McClane vs Thomas Gabriel', 'l7ah6fa')
character.add_character('John McClane', 'NYPD Detective', 2, 'Bruce Willis')
character.add_character('Matt Farrell', 'Computer Hacker', 2, 'Justin Long')
character.add_character('Thomas Gabriel', 'Cyber-Terrorist', 2, 'Timothy Olyphant')
movie.add_movie('Die Hard 4', 2007, '3.5',2)
'''Adding 3'''
battle.add_battle(3,'Normandy, France', 'Allies vs Axis', 'm74sor6')
character.add_character('John H. Miller', 'Allied Commander', 3, 'Tom Hanks')
character.add_character('James Ryan', 'Allied Paratrooper', 3, 'Matt Damon')
movie.add_movie('Saving Private Ryan', 1998, '4.5',3)
'''Adding 4'''
battle.add_battle(4,'Thermopylae, Greece', 'Spartans vs Persians', 'bk36dhl')
character.add_character('Leonidas I', 'Spartan', 4, 'Gerard Butler ')
character.add_character('King Xerxes', 'Persian', 4, 'Rodrigo Santoro')
character.add_character('Queen Gorgo', 'Spartan', 4, 'Lena Headey')
movie.add_movie('300', 2007, 4,4 )
'''Adding 5'''
battle.add_battle(5,'Sydney, Australia', 'Ethan Hunt vs Sean Ambrose', 'kcgkjvw')
character.add_character('Ethan Hunt', 'IMF Agent', 5, 'Tom Cruise')
character.add_character('Sean Ambrose', 'Rogue IMF Agent', 5, 'Dougray Scott')
character.add_character('Luther Stickell', 'IMF Computer Hacker', 5, 'Ving Rhames')
character.add_character('Nyah Nordoff-Hall', 'Professional Thief', 5, 'Thandie Newton')
movie.add_movie('Mission: Impossible II', 2000, 3,5 )
'''Adding 6'''
battle.add_battle(6,'Anatolia, Turkey', 'Trojans vs Spartans', 'lxkya5l')
character.add_character('Hector', 'Trojan', 6, 'Eric Bana')
character.add_character('Achilles', 'Spartan', 6, 'Brad Pitt')
movie.add_movie('Troy', 2004, 3.5,6)
'''Adding 7'''
battle.add_battle(7,'Little Italy, New York', 'Leon vs NYPD', 'nqhq8qg')
character.add_character('Leon', 'Hitman', 7, 'Jean Reno')
character.add_character('Norman Stansfield', 'Corrupt DEA Agent', 7, 'Gary Oldman')
character.add_character('Mathilda', 'Leon\'s Protegee', 7, 'Natalie Portman')
movie.add_movie('Leon: The Professional', 1994, 4.5,7)
'''Adding 8'''
battle.add_battle(8,'Caribbean Sea', 'Pirate Lord\'s vs East India Trading Company', 'qclxo7o')
character.add_character('Captain Jack Sparrow', 'Pirate Lord', 8, 'Johnny Depp')
character.add_character('Will Turner', 'Pirate', 8, 'Orlando Bloom')
character.add_character('Davy Jones', 'Malevolent Ruler', 8, 'Bill Nighy')
character.add_character('Captain Elizabeth Swann', 'Pirate Lord', 8, 'Keira Knightley')
movie.add_movie('Pirates of the Caribbean : At World\'s End', 2007, 3.5,8)
'''Adding 9'''
battle.add_battle(9,'Pride Rock, Kisumu, Kenya, Africa', 'Simba vs Scar', 'pj3df3w')
character.add_character('Simba', 'Lion King', 9, 'Matthew Broderick')
character.add_character('Mufasa', 'Deceased Lion King', 9, 'James Earl Jones')
character.add_character('Scar', 'Mufasa\s Brother', 9, 'Jeremy Irons')
movie.add_movie('The Lion King', 1994, 4.0,9)
'''Adding 10'''
battle.add_battle(10,'Bolivia', 'James Bond vs Dominic Greene & General Medrano', 'lzekd3l')
character.add_character('James Bond', 'Agent 007', 10, 'Daniel Craig')
character.add_character('Camille Montes', 'Bolivian Agent', 10, 'Olga Kurylenko')
character.add_character('Dominic Greene', 'Head of The Quantum', 10, 'Mathieu Amalric')
movie.add_movie('Quantum of Solace', 2008, 3.5,10)
'''Adding 11'''
battle.add_battle(11,'Washington D.C.', 'X-Men vs Magneto', 'mr7frko')
character.add_character('Wolverine', 'Mutant', 11, 'Hugh Jackman')
character.add_character('Magneto', 'Mutant', 11, 'Michael Fassbender')
character.add_character('Boliver Trask', 'Military Scientist', 11, 'Peter Dinklage')
movie.add_movie('X-Men : Days of Future Past', 2014, 4.0 ,11)
'''Adding 12'''
battle.add_battle(12,'Pearl Harbor', 'Allies vs Axis', 'mytjwuh')
character.add_character('Rafe McCawley', 'Captain', 12, 'Ben Affleck')
character.add_character('Franklin D. Roosevelt', 'POTUS', 12, 'Jon Voight')
character.add_character('Danny Walker', 'Captain', 12, 'Josh Hartnett ')
movie.add_movie('Pearl Harbor', 2001, 3.0 ,12)
'''Adding 13'''
battle.add_battle(13,'Las Vegas', 'Rocky vs Mason Dixon', 'n578al4')
character.add_character('Rocky Balboa', 'Retired Boxer', 13, 'Sylvester Stallone')
character.add_character('Mason Dixon', 'Heavyweight Champion', 13, 'Antonio Tarver')
movie.add_movie('Rocky Balboa', 2006, 3.5 ,13)
'''Adding 14'''
battle.add_battle(14,'Rio de Janeiro', 'Dominic Toretto vs Luke Hobbs', 'mrb5b3v')
character.add_character('Dominic Toretto', 'Professional Criminal', 14, 'Vin Diesel')
character.add_character('Luke Hobbs', 'Security Service Agent', 14, 'Dwayne Johnson')
character.add_character('Brian O\'Connor', 'Professional Criminal', 14, 'Paul Walker')
movie.add_movie('Fast Five', 2011, 3.5 ,14)
'''Adding 15'''
battle.add_battle(15,'Greenville, MI', 'Django vs Slave Owners', 'otp5e23')
character.add_character('Django', 'Freed Slave', 15, 'Jamie Foxx')
character.add_character('Dr. King Schultz', 'Bounty Hunter', 15, 'Christoph Waltz')
character.add_character('Calvin Candie', 'Slave Owner', 15, 'Leonardo DiCaprio')
movie.add_movie('Django Unchained', 2012, 4.0 ,15)
'''Adding 16'''
battle.add_battle(16,'Beijing', 'Dre Parker vs Cheng', 'olqr9q9')
character.add_character('Dre Parker', 'Kung Fu Student', 16, 'Jaden Smith')
character.add_character('Mr. Han', 'Kung Fu Master', 16, 'Jackie Chan')
character.add_character('Sherry Parker', 'Dre\'s Mother', 16, 'Taraji P. Henson')
movie.add_movie('The Karate Kid', 2010, 3.0, 16)

reset()