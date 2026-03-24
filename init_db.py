import sqlite3

# Connect to the database file
connection = sqlite3.connect('database.db')

# Run the schema.sql script to create the table structure
with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# The 5 Indian Legends - Wrapped in triple quotes to allow for apostrophes and special characters
legends = [
    (
        'Jagadish Chandra Bose: A Beacon of Scientific Renaissance in India', 
        """In 1885, young J.C. Bose completed his undergraduate degree at the University of Cambridge and returned to India. In the late 19th century, while scientific advancement was limited to countries like the United Kingdom, Germany, France, and the United States, Jagadish Chandra Bose brought it to India through his groundbreaking research breakthroughs and numerous scientific inventions. His research paper "On a new electro-polariscope," published in The Electrician in December 1895, was the first paper published by an Indian in Western scientific periodicals. He was a pioneer in the exploration of radio microwave optics and made notable contributions to the field of botany. He played a crucial role in advancing experimental science on the Indian subcontinent. He established the Bose Institute, which is recognized as a premier research institution in India and is one of the nation’s oldest. Founded in 1917, the institute holds the distinction of being the first interdisciplinary research center in Asia. Sir Nevill Mott (Nobel Laureate of 1977) remarked that "J.C. Bose was at least 60 years ahead of his time.\""""
    ),
    (
        'Satyendra Nath Bose: Bridging Mathematics and Physics for a New Era', 
        """In 1915, after completing his MSc degree from Rajabazar Science College, young Satyendra Nath Bose immersed himself in the study of the theory of relativity. During the early 20th century, when Germany was at the forefront of theoretical physics, Bose's contributions to quantum mechanics, particularly in establishing the foundation for Bose-Einstein statistics and the theory of the Bose-Einstein condensate, positioned India as an emerging contender in the field of theoretical physics. In collaboration with Meghnad Saha, Bose developed the first English book derived from German and French translations of original papers on Einstein's theories of relativity. His 1924 research article, which deduced Planck's quantum radiation law without relying on classical physics, was instrumental in establishing the significant discipline of quantum statistics. Although initially not accepted for publication, Albert Einstein, acknowledging the significance of the paper, personally translated it into German and submitted it on Bose's behalf to the Zeitschrift für Physik. He inspired students to create their own equipment using locally sourced materials and skilled technicians. His contributions were vital in laying the groundwork for theoretical physics in India."""
    ),
    (
        'Prafulla Chandra Ray: The Father of Indian Chemistry', 
        """In 1888, young Prafulla Chandra Ray returned to India after receiving his PhD from the University of Edinburgh in Scotland, UK. He was one of the first modern chemical researchers in India. In 1896, he discovered the stable compound 'mercurous nitrite.' This discovery laid the groundwork for extensive research in inorganic chemistry. He founded Bengal Chemicals, the first pharmaceutical company in India to promote self-reliance in India’s pharmaceutical industry during British colonial rule. In his lifetime, he authored more than 150 original research articles across all fields of chemistry. Highlighting the contributions of ancient Indian scholars to the field of chemistry and alchemy, he wrote 'A History of Hindu Chemistry from the Earliest Times to the Middle of the Sixteenth Century.' The book played a crucial role in introducing Western audiences to Indian alchemical traditions, which were largely unknown prior to its publication. He established the Indian Chemical Society. Founded in 1924, the society took a significant role in promoting chemical research and education in India. The Royal Society of Chemistry honored his life and work with the first ever Chemical Landmark Plaque outside Europe."""
    ),
    (
        'B. R. Ambedkar: The Champion of Justice & The Architect of Equality', 
        """In 1927, after earning PhD from Columbia University, B.R. Ambedkar returned to India as one of the first Indians to earn a doctorate in economics abroad. His thesis, The Problem of the Rupee: Its Origin and Solution, analyzed India's economic stability and currency issues. He advocated for industrialization and agricultural development as key components of economic growth. He founded Bahishkrit Hitakarini Sabha to advocate for the rights of the untouchables and later established the All India Scheduled Castes Federation to represent marginalized communities. His leadership in events like the Mahad Satyagraha in 1927 and the Kalaram Temple entry movement in 1930 were pivotal in mobilizing 'Dalits' for their rights. He chaired the committee that drafted the Constitution of India based on the debates of the Constituent Assembly of India and the first draft of Sir Benegal Narsing Rau. He championed women's education and worked towards legal reforms that would grant women equal rights in marriage, inheritance, and property ownership through initiatives like the Hindu Code Bill. His contributions have profoundly shaped modern India and continue to inspire movements against caste discrimination and advocate for human rights across the nation."""
    ),
    (
        'Ishwar Chandra Vidyasagar: Pioneering Education and Social Reform in India', 
        """In 1839, after successfully passing his Law Examination, young Ishwar Chandra Bandopadhyay committed himself to improving the status of women in India. He went door to door, urging family heads to allow their daughters to enroll in schools. Throughout Bengal, he established 35 schools for girls, successfully enrolling 1,300 students. He also organized a fund called Nari Siksha Bhandar. In 1849, he supported John Elliot Bethune in founding the Bethune School, which became the first permanent school for girls in India. To keep his mother's promise and to alleviate the pain and helplessness experienced by Hindu widows, in 1854, he launched a campaign for the remarriage of widows. Vidyasagar presented his arguments to the British authorities, and his efforts culminated in the enactment of the Hindu Widows' Remarriage Act on July 26, 1856. He campaigned against child remarriage, which led to the Age of Consent Act in 1891. Vidyasagar dedicated over 18 years of his life to the "Santhals," an old tribe community in Karmatar, Jharkhand. He established a girls' school and a night school for adults on the grounds of his home, which he named Nandan Kanan. Additionally, he launched a free homeopathy clinic to provide essential medical care for the underprivileged tribal population in the area. Rabindranath Tagore reverently wrote about him: "One wonders how God, in the process of producing forty million Bengalis, produced a man!\""""
    )
]

# Insert the data into the table
cur.executemany("INSERT INTO posts (title, content) VALUES (?, ?)", legends)

# Save (commit) the changes and close
connection.commit()
connection.close()

print("Success! Table recreated and 5 legends added.")