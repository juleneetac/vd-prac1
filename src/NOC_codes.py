import pandas as pd
from io import StringIO

# Raw multiline string of the data
raw_data = """
Region,Country,NOC
Africa,Algeria,ALG
Africa,Angola,ANG
Africa,Benin,BEN
Africa,Botswana,BOT
Africa,Burkina Faso,BUR
Africa,Burundi,BDI
Africa,Cameroon,CMR
Africa,Cabo Verde,CPV
Africa,Central African Republic,CAF
Africa,Chad,CHA
Africa,Comoros,COM
Africa,Congo,CGO
Africa,Democratic Republic of the Congo,COD
Africa,Côte d’Ivoire,CIV
Africa,Djibouti,DJI
Africa,Egypt,EGY
Africa,Eritrea,ERI
Africa,Eswatini,SWZ
Africa,Ethiopia,ETH
Africa,Gabon,GAB
Africa,Gambia,GAM
Africa,Ghana,GHA
Africa,Guinea,GUI
Africa,Guinea-Bissau,GBS
Africa,Equatorial Guinea,GEQ
Africa,Kenya,KEN
Africa,Lesotho,LES
Africa,Liberia,LBR
Africa,Libya,LBA
Africa,Madagascar,MAD
Africa,Malawi,MAW
Africa,Mali,MLI
Africa,Morocco,MAR
Africa,Mauritius,MRI
Africa,Mauritania,MTN
Africa,Mozambique,MOZ
Africa,Namibia,NAM
Africa,Niger,NIG
Africa,Nigeria,NGR
Africa,Uganda,UGA
Africa,Rwanda,RWA
Africa,Sao Tome and Principe,STP
Africa,Senegal,SEN
Africa,Seychelles,SEY
Africa,Sierra Leone,SLE
Africa,Somalia,SOM
Africa,South Africa,RSA
Africa,South Sudan,SSD
Africa,Sudan,SUD
Africa,Tanzania,TAN
Africa,Togo,TOG
Africa,Tunisia,TUN
Africa,Zambia,ZAM
Africa,Zimbabwe,ZIM
The Americas,Antigua and Barbuda,ANT
The Americas,Argentina,ARG
The Americas,Aruba,ARU
The Americas,Bahamas,BAH
The Americas,Barbados,BAR
The Americas,Belize,BIZ
The Americas,Bermuda,BER
The Americas,Bolivia,BOL
The Americas,Brazil,BRA
The Americas,Cayman Islands,CAY
The Americas,Canada,CAN
The Americas,Chile,CHI
The Americas,Colombia,COL
The Americas,Costa Rica,CRC
The Americas,Cuba,CUB
The Americas,Dominican Republic,DOM
The Americas,Dominica,DMA
The Americas,El Salvador,ESA
The Americas,Ecuador,ECU
The Americas,Grenada,GRN
The Americas,Guatemala,GUA
The Americas,Guyana,GUY
The Americas,Haiti,HAI
The Americas,Honduras,HON
The Americas,Jamaica,JAM
The Americas,Mexico,MEX
The Americas,Nicaragua,NCA
The Americas,Panama,PAN
The Americas,Paraguay,PAR
The Americas,Peru,PER
The Americas,Puerto Rico,PUR
The Americas,Saint Kitts and Nevis,SKN
The Americas,Saint Lucia,LCA
The Americas,St. Vincent and the Grenadines,VIN
The Americas,Suriname,SUR
The Americas,Trinidad and Tobago,TTO
The Americas,United States of America,USA
The Americas,Uruguay,URU
The Americas,Venezuela,VEN
The Americas,British Virgin Islands,IVB
The Americas,U.S. Virgin Islands,ISV
Asia,Afghanistan,AFG
Asia,Bahrain,BRN
Asia,Bangladesh,BAN
Asia,Bhutan,BHU
Asia,Brunei Darussalam,BRU
Asia,Cambodia,CAM
Asia,China,CHN
Asia,South Korea,KOR
Asia,Hong Kong,HKG
Asia,India,IND
Asia,Indonesia,INA
Asia,Iran,IRI
Asia,Iraq,IRQ
Asia,Japan,JPN
Asia,Jordan,JOR
Asia,Kazakhstan,KAZ
Asia,Kyrgyzstan,KGZ
Asia,Kuwait,KUW
Asia,Laos,LAO
Asia,Lebanon,LBN
Asia,Malaysia,MAS
Asia,Maldives,MDV
Asia,Mongolia,MGL
Asia,Myanmar,MYA
Asia,Nepal,NEP
Asia,Oman,OMA
Asia,Pakistan,PAK
Asia,Palestine,PLE
Asia,Philippines,PHI
Asia,Qatar,QAT
Asia,North Korea,PRK
Asia,Saudi Arabia,KSA
Asia,Singapore,SGP
Asia,Sri Lanka,SRI
Asia,Syrian Arab Republic,SYR
Asia,Tajikistan,TJK
Asia,Chinese Taipei,TPE
Asia,Thailand,THA
Asia,Democratic Rep. of Timor-Leste,TLS
Asia,Turkmenistan,TKM
Asia,United Arab Emirates,UAE
Asia,Uzbekistan,UZB
Asia,Vietnam,VIE
Asia,Yemen,YEM
Europe,Albania,ALB
Europe,Andorra,AND
Europe,Armenia,ARM
Europe,Austria,AUT
Europe,Azerbaijan,AZE
Europe,Belgium,BEL
Europe,Bosnia and Herzegovina,BIH
Europe,Bulgaria,BUL
Europe,Cyprus,CYP
Europe,Croatia,CRO
Europe,Czechia,CZE
Europe,Denmark,DEN
Europe,Spain,ESP
Europe,Estonia,EST
Europe,Finland,FIN
Europe,France,FRA
Europe,Georgia,GEO
Europe,Germany,GER
Europe,Great Britain,GBR
Europe,Greece,GRE
Europe,Hungary,HUN
Europe,Ireland,IRL
Europe,Iceland,ISL
Europe,Israel,ISR
Europe,Italy,ITA
Europe,Kosovo,KOS
Europe,Latvia,LAT
Europe,Liechtenstein,LIE
Europe,Lithuania,LTU
Europe,Luxembourg,LIE
Europe,North Macedonia,MKD
Europe,Malta,MLT
Europe,Moldova,MDA
Europe,Monaco,MON
Europe,Montenegro,MNE
Europe,Netherlands,NED
Europe,Norway,NOR
Europe,Poland,POL
Europe,Portugal,POR
Europe,Romania,ROU
Europe,San Marino,SMR
Europe,Serbia,SRB
Europe,Slovakia,SVK
Europe,Slovenia,SLO
Europe,Sweden,SWE
Europe,Switzerland,SUI
Europe,Türkiye,TUR
Europe,Ukraine,UKR
Oceania,American Samoa,ASA
Oceania,Australia,AUS
Oceania,Cook Islands,COK
Oceania,Fiji,FIJ
Oceania,Guam,GUM
Oceania,Kiribati,KIR
Oceania,Marshall Islands,MHL
Oceania,Federated States of Micronesia,FSM
Oceania,Nauru,NRU
Oceania,New Zealand,NZL
Oceania,Palau,PLW
Oceania,Papua New Guinea,PNG
Oceania,Solomon Islands,SOL
Oceania,Samoa,SAM
Oceania,Tonga,TGA
Oceania,Tuvalu,TUV
Oceania,Vanuatu,VAN
"""

# Guardar el CSV
with open("data/noc.csv", "w") as file:
    file.write(raw_data)

print("CSV guardado exitosamente.")
