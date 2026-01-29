

-- Drop the table if it exists
DROP TABLE IF EXISTS simpsons_data.simpsons_quotes;

-- Create the table
CREATE TABLE simpsons_data.simpsons_quotes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    person VARCHAR(50) NOT NULL,
    quote TEXT NOT NULL
);

-- Populate with 20+ Simpsons quotes
INSERT INTO simpsons_data.simpsons_quotes (person, quote) VALUES
('Homer', 'D\'oh!'),
('Homer', 'Mmm... donuts.'),
('Homer', 'Trying is the first step towards failure.'),
('Bart', 'Eat my shorts!'),
('Bart', 'Cowabunga!'),
('Bart', 'Don’t have a cow, man.'),
('Lisa', 'If anyone wants me, I’ll be in my room.'),
('Lisa', 'I’m proud of you, dad.'),
('Marge', 'Homer!'),
('Marge', 'I just think they’re neat.'),
('Mr. Burns', 'Excellent...'),
('Mr. Burns', 'Release the hounds.'),
('Milhouse', 'Everything’s coming up Milhouse!'),
('Ralph', 'My cat’s breath smells like cat food.'),
('Ralph', 'I choo-choo-choose you.'),
('Chief Wiggum', 'Bake him away, toys.'),
('Comic Book Guy', 'Worst episode ever.'),
('Grandpa Simpson', 'I used to be with it, but then they changed what “it” was.'),
('Ned Flanders', 'Okily dokily!'),
('Krusty', 'Hey hey!'),
('Moe', 'I’m better than dirt. Well, most kinds of dirt.'),
('Apu', 'Thank you, come again!'),
('Nelson', 'Ha-ha!');


commit;
