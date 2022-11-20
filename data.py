import random

from word import Word

animals = [
    Word("Cat", "Mačka"),
    Word("Dog", "Pas"),
    Word("Duck", "Patka"),
    Word("Swan", "Lubad"),
    Word("Bear", "Medved"),
    Word("Cow", "Krava"),
    Word("Mouse", "Miš"),
    Word("Rat", "Pacov"),
    Word("Horse", "Konj"),
    Word("Wolf", "Vuk"),

    Word("Pig", "Svinja"),
    Word("Goose", "Guska"),
    Word("Chicken", "Pile"),
    Word("Rooster", "Petao"),
    Word("Parrot", "Papagaj"),
    Word("Donkey", "Magarac"),
    Word("Hamster", "Hrčak"),
    Word("Fish", "Riba"),
    Word("Monkey", "Majmun"),
    Word("Fox", "Fok"),

    Word("Bird", "Ptica"),
    Word("Raven", "Vrana"),
    Word("Pigeon", "Golub"),
    Word("Seagull", "Galeb"),
    Word("Eagle", "Orao"),
    Word("Sheep", "Ovce"),
    Word("Goat", "Koza"),
    Word("Giraffe", "Žirafa"),
    Word("Lion", "Lav"),
    Word("Tiger", "Tigar"),
]
greetings = [
    Word('Hi', 'Ćao'),
    Word('Good morning!', 'Dobro jutro!'),
    Word('Good afternoon!', 'Dobar dan!'),
    Word('Good evening!', 'Dobro veče!'),
    Word('Good night!', 'Laku noć!'),
    Word('How are you?', 'Kako si?'),
    Word('Fine', 'Dobro'),
    Word('Thank you', 'Hvala'),
    Word('I’m sorry', 'Žao mi je'),
    Word('Goodbye', 'Doviđenja'),
    Word('Never mind', 'Nema veze'),
    Word('Do you speak English?', 'Da li govoriš engleski?'),
    Word('Do you speak Thai?', 'Da li govoriš tajlandski?'),
    Word('Do you speak German?', 'Da li govoriš nemački?'),
    Word('Yes, I speak English', 'Da, govorim engleski'),
    Word('No, I don’t speak English', 'Ne, ne govorim engleski'),
    Word('I don’t understand', 'Ne razumem'),
    Word('Please speak more slowly', 'Molim te, pričaj sporije'),
    Word('You’re welcome', 'Nema na čemu!'),
    Word('Yes', 'Da'),
    Word('No', 'Ne'),
    Word('Okay', 'Okej'),
    Word('Right', 'Tačno'),
    Word('Wrong', 'Netačno'),
    Word('Excuse me', 'Izvini'),
    Word('I see', 'Vidim'),
    Word('I don’t know', 'Ne znam'),
    Word('No problem', 'Nema problema'),
    Word('Good luck!', 'Srećno!'),
    Word('Take care!', 'Čuvaj se!'),
    Word('Cheers!', 'Živeli!'),
    Word('Cute', 'Slatko'),
    Word('Beautiful', 'Lepo'),
    Word('Please', 'Molim te'),
    Word('See you', 'Vidimo se)'),
    Word('Goodbye', 'Doviđenja'),
    Word('Sweet dreams', 'Lepo spavaj'),
    Word('Good night', 'Laku noć'),
]
days_of_week = [
    Word('Monday', 'Ponedeljak'),
    Word('Tuesday', 'Utorak'),
    Word('Wednesday', 'Sreda'),
    Word('Thursday', 'Četvrtak'),
    Word('Friday', 'Petak'),
    Word('Saturday', 'Subota'),
    Word('Sunday', 'Nedelja'),
]
calendar = [
    Word('Weekday', 'Radni dan'),
    Word('Weekend', 'Vikend'),
    Word('January', 'Januar'),
    Word('February', 'Februar'),
    Word('March', 'Mart'),
    Word('April', 'April'),
    Word('May', 'Maj'),
    Word('June', 'Jun'),
    Word('July', 'Jul'),
    Word('August', 'Avgust'),
    Word('September', 'Septembar'),
    Word('October', 'Oktobar'),
    Word('November', 'Novembar'),
    Word('December', 'Decembar'),
    Word('Morning', 'Jutro'),
    Word('Noon', 'Podne'),
    Word('Afternoon', 'Posle podne'),
    Word('Evening', 'Veče'),
    Word('Night', 'Noć'),
    Word('Midnight', 'Ponoć'),
    Word('Day', 'Dan'),
    Word('Hour', 'Sat'),
    Word('Minute', 'Minut'),
    Word('Second', 'Sekunda'),
    Word('O’clock', 'Sati'),
    Word('O’clock', 'Sati'),
    Word('Time', 'Vreme'),
    Word('2:00 AM', '2 sata ujutru'),
    Word('6:00 AM', '6 sati ujutru'),
    Word('3:00 PM', '3 sata popodne'),
    Word('6:00 PM', '6 sati popodne'),
    Word('7:00 PM', '7 sati popodne'),
    Word('9:15 AM', '9:15 prepodne'),
    Word('10:30 AM', '10:30 prepodne'),
    Word('1:45 PM', '1:45 popodne'),
    Word('What time is it?', 'Koliko je sati?'),
    Word('What day is today?', 'Koji je danas dan?'),
    Word('What is the date today?', 'Koji je danas datum?'),
    Word('What time do you get up?', 'U koliko sati ustaješ?'),
    Word('It’s… (time)', 'Sada je…(sati)'),
    Word('What time does the bus leave?', 'Kada polazi autobus?'),
    Word('When will the plane arrive?', 'Kada će stići avion?'),
    Word('When is your birthday?', 'Kada je tvoj rođendan?'),
    Word('I got up early as usual', 'Ustala sam rano kao i obično'),
    Word('What time do you go home?', 'U koliko sati ideš kući?'),
    Word('I have class tomorrow', 'Imam čas sutra'),
    Word('Can you tell me the time?', 'Možeš li mi reći koliko je sati?'),
    Word('I was born on October 10th, 1972', 'Rođena sam 10. oktobra 1972'),
    Word('It’s Monday today', 'Danas je ponedeljak'),
]
conversation = [
    Word('What’s your name?', 'Kako se zoveš?'),
    Word('My name is…', 'Zovem se…'),
    Word('Where do you come from?', 'Odakle dolaziš?'),
    Word('I come from…(country)', 'Dolazim iz…(država)'),
    Word('How old are you?', 'Koliko imaš godina?'),
    Word('I’m 25 years old', 'Imam 25 godina'),
    Word('How many siblings do you have?', 'Koliko braće/sestara imaš?'),
    Word('I have one younger brother', 'Imam jednog mlađeg brata'),
    Word('I have two older sisters', 'Imam dve starije sestre'),
    Word('Where do you work?', 'Gde radiš?'),
    Word('I work at Yandex', 'Radim u Yandexu'),
    Word('Where do you study?', 'Gde studiraš?'),
    Word('I study at…', 'Studiram na…'),
    Word('Can I have your name card?', 'Mogu li da dobijem tvoju vizit kartu?'),
    Word('Nice to meet you', 'Drago mi je da smo se upoznali'),
    Word('I’m a college student', 'Ja sam student'),
    Word('Are you students?', 'Da li ste vi studenti?'),
    Word('Keep in touch!', 'Čujemo se!'),
]
numbers = [
    Word('Zero', 'Nula'),
    Word('One', 'Jedan'),
    Word('Two', 'Dva'),
    Word('Three', 'Tri'),
    Word('Four', 'Četiri'),
    Word('Five', 'Pet'),
    Word('Six', 'Šest'),
    Word('Seven', 'Sedam'),
    Word('Eight', 'Osam'),
    Word('Nine', 'Devet'),
    Word('Ten', 'Deset'),
    Word('Eleven', 'Jedanaest'),
    Word('Twelve', 'Dvanaest'),
    Word('Thirteen', 'Trinaest'),
    Word('Fourteen', 'Četrnaest'),
    Word('Fifteen', 'Petnaest'),
    Word('Sixteen', 'Šesnaest'),
    Word('Seventeen', 'Sedamnaest'),
    Word('Eighteen', 'Osamnaest'),
    Word('Nineteen', 'Devetnaest'),
    Word('Twenty', 'Dvadeset'),
    Word('Twenty One', 'Dvadeset jedan'),
    Word('Twenty Two', 'Dvadeset dva'),
    Word('Twenty Three', 'Dvadeset tri'),
    Word('Twenty Four', 'Dvadeset četiri'),
    Word('Twenty Five', 'Dvadeset pet'),
    Word('Twenty Six', 'Dvadeset šest'),
    Word('Twenty Seven', 'Dvadeset sedam'),
    Word('Twenty Eight', 'Dvadeset osam'),
    Word('Twenty Nine', 'Dvadeset devet'),
    Word('Thirty', 'Trideset'),
    Word('Forty', 'Četrdeset'),
    Word('Fifty', 'Pedeset'),
    Word('Sixty', 'Šezdeset'),
    Word('Seventy', 'Sedamdeset'),
    Word('Eighty', 'Osamdeset'),
    Word('Ninety', 'Devedeset'),
    Word('One hundred', 'Sto'),
    Word('One thousand', 'Hiljadu'),
    Word('Ten thousand', 'Deset hiljada'),
    Word('Hundred thousand', 'Sto hiljada'),
    Word('One million', 'Milion'),
]
questions = [
    Word('What?', 'Šta?'),
    Word('Who?', 'Ko?'),
    Word('Where?', 'Gde?'),
    Word('Why?', 'Zašto?'),
    Word('When?', 'Kada?'),
    Word('How?', 'Kako?'),
    Word('How far?', 'Koliko daleko?'),
    Word('How often?', 'Koliko često?'),
    Word('How much?', 'Koliko?'),
    Word('Which one (thing)?', 'Koja (stvar)?'),
    Word('Which one (person)?', 'Koja (osoba)?'),
    Word('Which?', 'Koja?'),
    Word('Whose?', 'Čija?'),
]
eating = [
    Word('I’m hungry', 'Gladna sam'),
    Word('I’m full', 'Sita sam'),
    Word('I’ve already reserved a table', 'Već sam rezervisala sto'),
    Word('What dishes do you recommend?', 'Koja jela preporučuješ?'),
    Word('May I have a menu?', 'Mogu li da dobijem meni?'),
    Word('May I order some food?', 'Mogu li da poručim hranu?'),
    Word('I would like to order…', 'Želela bih bih da poručim…'),
    Word('May I have a glass of water?', 'Mogu li da dobijem čašu vode?'),
    Word('I’d like to have a bottle of beer', 'Želela bih flašu piva'),
    Word('I’d like to have a cocktail', 'Želela bih koktel'),
    Word('May I have a knife?', 'Mogu li da dobijem nož?'),
    Word('I’m vegetarian', 'Vegetarijanac sam'),
    Word('I’m allergic to…', 'Alergična sam na…'),
    Word('Does the food contain nuts?', 'Da li hrana sadrži orahe?'),
    Word('I like spicy food', 'Volim začinjenu hranu'),
    Word('A little spicy, please', 'Malo začinjeno, molim'),
    Word('Not spicy, please', 'Nezačinjeno, molim'),
    Word('I cannot eat spicy food', 'Ne mogu da jedem začinjenu hranu'),
    Word('Enjoy your meal', 'Uživaj u jelu'),
    Word('It is very delicious', 'Veoma je ukusno'),
    Word('I like Thai food', 'Volim tajlandsku hranu'),
    Word('I like German food', 'Volim nemačku hranu'),
    Word('May I have the bill?', 'Mogu li da dobijem račun?'),
    Word('Can I pay with a credit card?', 'Mogu li da platim kreditnom karticom?'),
    Word('You’re invited', 'Pozvani ste'),
    Word('Keep the change', 'Zadržite kusur'),
    Word('What do you like to eat?', 'Šta voliš da jedeš?'),
    Word('I will pay the bill', 'Ja ću platiti'),
    Word('Could you recommend a nice restaurant near here?', 'Možeš li da mi preporučiš dobar restoran u blizini?'),
    Word('I don’t like chocolate', 'Ne volim čokoladu'),
]
shopping = [
    Word('Where’s a shopping center?', 'Gde je šoping centar?'),
    Word('When does it open?', 'Kada se otvara?'),
    Word('When does it close?', 'Kada se zatvara?'),
    Word('I’d like to buy…', 'Želela bih da kupim …'),
    Word('May I try it on?', 'Mogu li da probam?'),
    Word('It doesn’t fit', 'Ne odgovara mi'),
    Word('Do you have this in a smaller size?', 'Da li imate ovo u manjoj veličini?'),
    Word('Do you have this in a bigger size?', 'Da li imate ovo u većoj veličini?'),
    Word('Do you have another color?', 'Da li imate drugu boju?'),
    Word('I want to buy this', 'Želim da kupim ovo'),
    Word('How much is it?', 'Koliko košta?'),
    Word('I’m just looking', 'Samo gledam'),
    Word('Can I have a receipt please?', 'Mogu li da dobijem račun, molim Vas?'),
    Word('Where is a handmade goods shop?', 'Gde je prodavnica ručnih radova?'),
    Word('Is there a duty free shop?', 'Ima li negde bescarinska radnja?'),
    Word('Where can I find…?', 'Gde mogu da nađem…?'),
    Word('This is very beautiful', 'Ovo je veoma lepo'),
    Word('I like it', 'Sviđa mi se'),
    Word('I would like to return this', 'Želela bih da vratim ovo'),
    Word('Is it real leather?', 'Da li je prava koža?'),
    Word('Can you give a discount?', 'Možete li da date popust?'),
    Word('Where can I find toothpaste?', 'Gde mogu da nađem pastu za zube?'),
    Word('How much for half a kilo?', 'Koliko košta pola kilograma?'),
    Word('I like this shirt. May I try it on?', 'Sviđa mi se ova košulja. Mogu li da je probam?'),
    Word('How much is that mountain bike?', 'Koliko košta taj planinski bicikl?'),
    Word('What is this jacket made of?', 'Od čega je ova jakna?'),
]
direction_words = [
    Word('Go straight', 'Idi pravo'),
    Word('Turn left', 'Skreni levo'),
    Word('Turn right', 'Skreni desno'),
    Word('Get in/on', 'Ući'),
    Word('Get off', 'Sići/izaći'),
    Word('Transfer', 'Presedanje'),
    Word('Taxi', 'Taksi'),
    Word('Direction', 'Pravac'),
    Word('Boat', 'Čamac'),
    Word('Station', 'Stanica'),
    Word('Return', 'Povratak'),
    Word('Subway', 'Podzemna železnica'),
    Word('Train', 'Voz'),
    Word('Bus', 'Autobus'),
    Word('Van', 'Kombi'),
    Word('By car', 'Autom'),
    Word('By plane', 'Avionom'),
    Word('Roundabout', 'Kružni tok'),
    Word('One way', 'Jedan smer'),
    Word('Round trip', 'Povratno putovanje'),
    Word('Group ticket', 'Grupna karta'),
    Word('Child ticket', 'Karta za dete'),
    Word('Family ticket', 'Porodična karta'),
    Word('By foot', 'Peške'),
    Word('East', 'Istok'),
    Word('West', 'Zapad'),
    Word('South', 'Jug'),
    Word('North', 'Sever'),
    Word('There', 'Tamo'),
    Word('Far away', 'Daleko'),
    Word('Here', 'Ovde'),
    Word('At the corner', 'Na uglu'),
    Word('Opposite of/across from', 'Suprotno/preko puta'),
    Word('Next to', 'Pored'),
    Word('Behind', 'Iza'),
    Word('In front of', 'Ispred'),
    Word('Straight ahead', 'Samo pravo'),
    Word('Up', 'Gore'),
    Word('Down', 'Dole'),
    Word('Bridge', 'Most'),
    Word('Footbridge', 'Pešački most'),
    Word('Pedestrian crossing', 'Pešački prelaz'),
    Word('Road', 'Put'),
    Word('Traffic lights', 'Semafor'),
    Word('Tunnel', 'Tunel'),
    Word('Crossing', 'Prelaz'),
    Word('Motorcycle', 'Motocikl'),
    Word('Bicycle', 'Bicikl'),
    Word('Ferry boat', 'Trajekt'),
]
direction_phrases = [
    Word('Where is the train station?', 'Gde je železnička stanica?'),
    Word('I want to go to the train station', 'Želim da idem do železničke stanice'),
    Word('How can I get there?', 'Kako mogu da stignem tamo?'),
    Word('Where are you?', 'Gde si?'),
    Word('I’m at…', 'Ja sam na…'),
    Word('What is the name of this place?', 'Kako se zove ovo mesto?'),
    Word('Where is the nearest bus stop?', 'Gde je najbliža autobuska stanica?'),
    Word('Where is the nearest train station?', 'Gde je najbliža železnička stanica?'),
    Word('What is the name of this station?', 'Kako se zove ova stanica?'),
    Word('Where should I transfer?', 'Gde bi trebalo da presedam?'),
    Word('How long does it take?', 'Koliko mi je vremena potrebno?'),
    Word('It takes about…', 'Potrebno je oko…'),
    Word('Where can I buy a ticket?', 'Gde mogu da kupim kartu?'),
    Word('I want to buy a ticket to…', 'Želim da kupim kartu do…'),
    Word('How much is this ticket?', 'Koliko košta ova karta?'),
    Word('The ticket costs … baht', 'Karta košta … baht(a)'),
    Word('The ticket costs …', 'Karta košta …'),
    Word('Does the bus have air condition?', 'Da li autobus ima klimu?'),
    Word('Does the bus have a toilet?', 'Da li autobus ima toalet?'),
    Word('When does the train leave?', 'Kada polazi voz?'),
    Word('When will the train arrive?', 'Kada će stići voz?'),
    Word('Please take me to…', 'Molim te, odvedi me do…'),
    Word('Please stop here', 'Molim te, stani ovde'),
    Word('Please use the meter', 'Molim te, koristi taksimetar'),
    Word('Where is the restroom?', 'Gde je toalet?'),
    Word('Where are we?', 'Gde smo?'),
    Word('Where should we go?', 'Gde bi trebalo da idemo?'),
    Word('Where is the cafeteria?', 'Gde je kafeterija?'),
    Word('The shop is just in front of the train station', 'Radnja je baš ispred železničke stanice'),
    Word('Fasten your seat belt, please', 'Veži pojas, molim te'),
    Word('The brakes stopped working', 'Kočnice su prestale da rade'),
    Word('Don’t exceed the speed limit', 'Ne prekoračujte dozvoljenu brzinu'),
    Word('Can I park my car here?', 'Mogu li da parkiram auto ovde?'),
    Word('Could you show me the way to the bus stop?', 'Možeš li da mi pokažeš put do autobuske stanice?'),
    Word('The bus leaves in five minutes', 'Autobus polazi za pet minuta'),
    Word('The bus hasn’t come yet', 'Autobus još nije stigao'),
    Word('The train leaves in ten minutes', 'Voz polazi za deset minuta'),
    Word('Will the train leave on time?', 'Da li će voz krenuti na vreme?'),
    Word('The last train has already gone', 'Poslednji voz je već otišao'),
]
emergency = [
    Word('Help!', 'Pomoć!'),
    Word('Can you help me?', 'Možeš li da mi pomogneš?'),
    Word('I lost my wallet', 'Izgubila sam novčanik'),
    Word('My bag got stolen', 'Ukradena mi je torba'),
    Word('I lost my passport', 'Izgubila sam pasoš'),
    Word('I want to go to the embassy', 'Želim da idem u ambasadu'),
    Word('I have some trouble', 'Imam neke probleme'),
    Word('I want a translator', 'Želim prevodioca'),
    Word('I want to go to the police office', 'Želim da idem u policijsku stanicu'),
    Word('I dont have money', 'Nemam para'),
    Word('Fire!', 'Vatra!'),
    Word('Someone needs help', 'Nekome je potrebna pomoć'),
    Word('I missed my flight', 'Propustila sam let'),
    Word('My luggage is lost', 'Izgubljen mi je prtljag'),
    Word('I lost my phone', 'Izgubila sam telefon'),
    Word('I lost the key', 'Izgubila sam ključeve'),
    Word('Please come as soon as possible', 'Molim te, dođi što pre'),
    Word('Is there a gas station around here?', 'Da li ima benzinska stanica negde u blizini?'),
    Word('Please call the fire department', 'Molim Vas, pozovite vatrogasce'),
]
health = [
    Word('I want to see a doctor', 'Želim da vidim doktora'),
    Word('I need an ambulance', 'Potrebna mi je hitna pomoć'),
    Word('I want to go to the hospital', 'Želim da idem u bolnicu'),
    Word('Where is the nearest pharmacy?', 'Gde je najbliža apoteka?'),
    Word('I feel sick', 'Osećam se bolesno'),
    Word('I would like medicine for…', 'Želela bih lek za…'),
    Word('It hurts', 'Boli'),
    Word('I had an accident', 'Imala sam nesreću'),
    Word('Please call a doctor', 'Molim Vas, pozovite doktora'),
    Word('I have health insurance', 'Imam zdravstveno osiguranje'),
    Word('How much is the treatment?', 'Koliko košta lečenje?'),
    Word('How should I take the medicine?', 'Kako bi trebalo da uzimam lek?'),
    Word('I’m allergic to…', 'Alergična sam na…'),
    Word('It hurts here', 'Boli me ovde'),
    Word('I have a headache', 'Imam glavobolju'),
    Word('I have back pain', 'Imam bol u leđima'),
    Word('I have a stomach ache', 'Boli me stomak'),
    Word('I have food poisoning', 'Imam trovanje hranom'),
    Word('I have a toothache', 'Imam zubobolju'),
    Word('I need penicillin', 'Potreban mi je penicilin'),
    Word('I need paracetamol', 'Potreban mi je paracetamol'),
    Word('I threw up', 'Povratila sam'),
    Word('I have a cold', 'Imam prehladu'),
    Word('I’m an asthmatic', 'Astmatičar sam'),
    Word('I’m diabetic', 'Dijabetičar sam'),
    Word('I’m a smoker', 'Pušač sam'),
    Word('My nephew is allergic to eggs', 'Moj nećak je alergičan na jaja'),
    Word('This medicine should be taken every three hours', 'Ovaj lek bi trebalo da se uzima na svaka tri sata'),
    Word('I have a high temperature', 'Imam visoku temperaturu'),
    Word('I have to take medicine', 'Treba da uzmem lek'),
    Word('Do you have any cough medicine?', 'Da li imate neki lek protiv kašlja?'),
    Word('I feel well today', 'Dobro se osećam danas'),
    Word('I’m sick', 'Bolesna sam'),
    Word('I have a bad cold', 'Imam strašnu prehladu'),
    Word('Your tooth must be extracted', 'Moraš da izvadiš zub'),
    Word('Burn', 'Opekotina'),
    Word('Abnormal', 'Nenormalno'),
    Word('Ache', 'Bol'),
    Word('Acute', 'Akutno'),
    Word('Ambulance', 'Ambulanta'),
    Word('Antibiotics', 'Antibiotici'),
    Word('Asthma (Attack)', 'Astma (napad)'),
    Word('Bacteria', 'Bakterija'),
    Word('Cough', 'Kašalj'),
    Word('Headache', 'Glavobolja'),
    Word('Blood Pressure', 'Krvni pritisak'),
    Word('Runny Nose', 'Curenje iz nosa'),
    Word('Sore Throat', 'Upaljeno grlo'),
    Word('Stomach Ache', 'Bol u stomaku'),
    Word('Breath', 'Disanje'),
    Word('Broken', 'Polomljeno'),
    Word('Cancer', 'Rak'),
    Word('Dentist', 'Zubar'),
    Word('Chickenpox', 'Boginje'),
    Word('Diabetes', 'Dijabetes'),
    Word('Diagnosis', 'Dijagnoza'),
    Word('Disease', 'Bolest'),
    Word('Emergency', 'Hitno'),
    Word('Fever', 'Groznica'),
    Word('Feverish', 'Grozničav'),
    Word('Heart Attack', 'Infarkt'),
    Word('Immune System', 'Imuni sistem'),
    Word('Infected', 'Zaražen'),
    Word('Injury', 'Povreda'),
    Word('Pain', 'Bol'),
    Word('Pain Killer', 'Lek protiv bolova'),
    Word('Patient', 'Pacijent'),
    Word('Pharmacy', 'Apoteka'),
    Word('Swollen', 'Otečeno'),
    Word('Temperature', 'Temperatura'),
    Word('Therapy', 'Terapija'),
    Word('Vomit', 'Povraćanje'),
    Word('Wound', 'Rana'),
]
sightseeing = [
    Word('Where is the tourist center?', 'Gde je turistički centar?'),
    Word('When does the tourist center open?', 'Kada se otvara turistički centar?'),
    Word('When does the tourist center close?', 'Kada se zatvara turistički centar?'),
    Word('Can I get a free map?', 'Mogu li da dobijem besplatnu mapu?'),
    Word('Where can I find a gift shop?', 'Gde mogu da nađem prodavnicu suvenira/poklona?'),
    Word('What places should I visit?', 'Koje mesta bi trebalo da posetim?'),
    Word('What should I be aware of?', 'Čega bi trebalo da se pazim?'),
    Word('What am I not allowed to do here?', 'Šta nije dozvoljeno da radim ovde?'),
    Word('How long does it take to go there?', 'Koliko mi je potrebno da odem do tamo?'),
    Word('Can I take photos here?', 'Mogu li da slikam ovde?'),
    Word('How much is the entrance ticket?', 'Koliko košta ulaznica?'),
    Word('I want to go to the national museum', 'Želim da idem u narodni muzej'),
    Word('Where is the most popular museum?', 'Koji je najpopularniji muzej?'),
    Word('I want to take a city tour', 'Želim da idem u obilazak grada'),
    Word('Where can I buy a city tour ticket?', 'Gde mogu da kupim kartu za obilazak grada?'),
    Word('Could you take a photo for me?', 'Možeš li da slikaš za mene?'),
    Word('Where is the post office?', 'Gde se nalazi pošta?'),
    Word('Where is the most beautiful beach?', 'Gde je najlepša plaža?'),
    Word('I would like to book a trip', 'Želim da rezervišem putovanje'),
    Word('I would like to have a map', 'Volela bih da imam mapu'),
    Word('I would like to do a one day trip', 'Želim da odem na jednodnevno putovanje'),
    Word('What trip do you recommend?', 'Koje putovanje preporučuješ?'),
    Word('Is there a park near here?', 'Da li ima park u blizini?'),
    Word('Do you have a map?', 'Da li imaš mapu?'),
]
hotels = [
    Word('Can you recommend a hotel?', 'Možeš li da mi preporučiš hotel?'),
    Word('I’d like to make reservation', 'Želela bih da rezervišem'),
    Word('Are there rooms available?', 'Ima li slobodnih soba?'),
    Word('Can I have a look?', 'Mogu li da pogledam?'),
    Word('Is internet included?', 'Da li je internet uračunat?'),
    Word('Is breakfast included?', 'Da li je doručak uračunat?'),
    Word('Is the hotel located near the center?', 'Da li se hotel nalazi blizu centra?'),
    Word('Where can I find the laundry?', 'Gde mogu da nađem perionicu?'),
    Word('Do you have a safe?', 'Da li imate sef?'),
    Word('How can I get to the hotel?', 'Kako mogu da stignem do hotela?'),
    Word('How much does the room cost?', 'Koliko košta soba?'),
    Word('I’d like to stay for … nights', 'Želela bih da ostanem…noći'),
    Word('I want a single room', 'Želim jednokrevetnu sobu'),
    Word('I want a double room', 'Želim dvokrevetnu sobu'),
    Word('I have a reservation', 'Imam rezervaciju'),
    Word('I will arrive at … (time)', 'Stići ću u … (vreme)'),
    Word('I will leave at … (time)', 'Otići ću u … (vreme)'),
    Word('I forgot the room key', 'Zaboravila sam ključ od sobe'),
    Word('Can I leave my luggage here?', 'Mogu li da ostavim svoj prtljag ovde?'),
    Word('How long is it from the hotel to the airport?', 'Koliko treba od hotela do aerodroma?'),
    Word('Do you have a baby bed?', 'Da li imate krevetac?'),
    Word('I would like to reserve a single room', 'Želim da rezervišem jednokrevetnu sobu'),
    Word('Could you bring my breakfast to room 305?', 'Možete li da donesete moj doručak u sobu 305?'),
    Word('We’ve just finished breakfast', 'Upravo smo završili doručak'),
    Word('I would like a hotel reservation', 'Želeo bih rezervaciju hotela'),
    Word('I canceled my hotel reservation', 'Otkazala sam rezervaciju u hotelu'),
]
food = [
    Word('Rice', 'Pirinač'),
    Word('Noodles', 'Rezanci'),
    Word('Beef', 'Govedina'),
    Word('Bitter', 'Gorko'),
    Word('Chicken', 'Piletina'),
    Word('Crab', 'Kraba'),
    Word('Duck', 'Patka'),
    Word('Fish', 'Riba'),
    Word('Hot', 'Ljuto'),
    Word('Meat', 'Meso'),
    Word('Mussel', 'Školjka'),
    Word('Pork', 'Svinjetina'),
    Word('Salty', 'Slano'),
    Word('Seafood', 'Morski plodovi'),
    Word('Shrimp', 'Škamp'),
    Word('Sour', 'Kiselo'),
    Word('Spicy', 'Začinjeno'),
    Word('Sticky Rice', 'Lepljivi pirinač'),
    Word('Sweet', 'Slatko'),
    Word('Tofu', 'Tofu'),
    Word('Water', 'Voda'),
    Word('Hot Water', 'Vruća voda'),
    Word('Coffee', 'Kafa'),
    Word('Coffee with milk', 'Kafa sa mlekom'),
    Word('Milk', 'Mleko'),
    Word('Hot chocolate', 'Topla čokolada'),
    Word('Tea', 'Čaj'),
    Word('Green Tea', 'Zeleni čaj'),
    Word('Beer', 'Pivo'),
    Word('Wine', 'Vino'),
    Word('Juice', 'Sok'),
    Word('Orange juice', 'Sok od narandže'),

    Word('Honey', 'Med'),
    Word('Pepper', 'Biber'),
    Word('Ice cream', 'Sladoled'),
    Word('Donut', 'Krofna'),
    Word('Flour', 'Brašno'),

    Word("Milk", "Mleko"),
    Word("Bread", "Hleb"),
    Word("water", "voda"),
    Word("Meat", "Meso"),
    Word("Fruit", "Voće"),
    Word("Vegetable", "Povrće"),
    Word("Egg", "Jaje"),
    Word("Pasta", "Testenina"),
    Word("Rice", "Pirinač"),
    Word("Cheese", "Sir"),

    Word("Candy", "Bombone"),
    Word("Beer", "Pivo"),
    Word("Wine", "Vino"),
    Word("Potato", "Krompir"),
    Word("Sausage", "Kobasica"),
    Word("Tomato", "Paradajz"),
    Word("Sugar", "Šećer"),
    Word("Salt", "So"),
]
fruit = [
    Word('Banana', 'Banana'),
    Word('Coconut', 'Kokos'),
    Word('Dragon fruit', 'Zmajevo voće'),
    Word('Durian', 'Durijan'),
    Word('Guava', 'Guava'),
    Word('Jackfruit', 'Nangka'),
    Word('Lychee', 'Liči'),
    Word('Mango', 'Mango'),
    Word('Mangosteen', 'Mangostin'),
    Word('Orange', 'Pomorandža'),
    Word('Papaya', 'Papaja'),
    Word('Pineapple', 'Ananas'),
    Word("Apple", "Jabuko"),
]
sport = [
    Word('Ball', 'Lopta'),
    Word('Football', 'Fudbal'),
    Word('Basketball', 'Košarka'),
    Word('Volleyball', 'Otbojka'),
    Word('Bowling', 'Kuglanje'),
    Word('Sailing', 'Jedrenje'),
    Word('Wrestling', 'Rvanje'),
]

words = [greetings, calendar, conversation, numbers, questions, eating, shopping, direction_words, direction_phrases,
         emergency, health, sightseeing, hotels, food, fruit, animals, days_of_week, sport]

idx = []
for i, w in enumerate(words):
    idx.extend([i]*len(w))


def get4():
    topic = words[random.choice(idx)]
    random.shuffle(topic)
    return topic[:4]


def count():
    return sum([len(i) for i in words])
