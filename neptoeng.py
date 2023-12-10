from nepali.date_converter import converter

# Open the input text file in read mode
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Process each line of input
for line in lines:
    parts = line.strip().split('/')
    year, month, date = map(int, parts)
    
    # Perform date conversion
    en_year, en_month, en_date = converter.nepali_to_english(year, month, date)
    
    # Print the converted date
    print(en_year,"/",en_month,"/",en_date)

#Input should be in the format below
#2069,10,01
#2069,10,01