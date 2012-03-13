from django.db import models
from django.contrib.auth.models import User

COUNTRIES = (
    ('AFG', 'Afghanistan'),
    ('ALA', 'Aland Islands'),
    ('ALB', 'Albania'),
    ('DZA', 'Algeria'),
    ('ASM', 'American Samoa'),
    ('AND', 'Andorra'),
    ('AGO', 'Angola'),
    ('AIA', 'Anguilla'),
    ('ATG', 'Antigua and Barbuda'),
    ('ARG', 'Argentina'),
    ('ARM', 'Armenia'),
    ('ABW', 'Aruba'),
    ('AUS', 'Australia'),
    ('AUT', 'Austria'),
    ('AZE', 'Azerbaijan'),
    ('BHS', 'Bahamas'),
    ('BHR', 'Bahrain'),
    ('BGD', 'Bangladesh'),
    ('BRB', 'Barbados'),
    ('BLR', 'Belarus'),
    ('BEL', 'Belgium'),
    ('BLZ', 'Belize'),
    ('BEN', 'Benin'),
    ('BMU', 'Bermuda'),
    ('BTN', 'Bhutan'),
    ('BOL', 'Bolivia'),
    ('BIH', 'Bosnia and Herzegovina'),
    ('BWA', 'Botswana'),
    ('BRA', 'Brazil'),
    ('VGB', 'British Virgin Islands'),
    ('BRN', 'Brunei Darussalam'),
    ('BGR', 'Bulgaria'),
    ('BFA', 'Burkina Faso'),
    ('BDI', 'Burundi'),
    ('KHM', 'Cambodia'),
    ('CMR', 'Cameroon'),
    ('CAN', 'Canada'),
    ('CPV', 'Cape Verde'),
    ('CYM', 'Cayman Islands'),
    ('CAF', 'Central African Republic'),
    ('TCD', 'Chad'),
    ('CIL', 'Channel Islands'),
    ('CHL', 'Chile'),
    ('CHN', 'China'),
    ('HKG', 'China - Hong Kong'),
    ('MAC', 'China - Macao'),
    ('COL', 'Colombia'),
    ('COM', 'Comoros'),
    ('COG', 'Congo'),
    ('COK', 'Cook Islands'),
    ('CRI', 'Costa Rica'),
    ('CIV', 'Cote d\'Ivoire'),
    ('HRV', 'Croatia'),
    ('CUB', 'Cuba'),
    ('CYP', 'Cyprus'),
    ('CZE', 'Czech Republic'),
    ('PRK', 'Democratic People\'s Republic of Korea'),
    ('COD', 'Democratic Republic of the Congo'),
    ('DNK', 'Denmark'),
    ('DJI', 'Djibouti'),
    ('DMA', 'Dominica'),
    ('DOM', 'Dominican Republic'),
    ('ECU', 'Ecuador'),
    ('EGY', 'Egypt'),
    ('SLV', 'El Salvador'),
    ('GNQ', 'Equatorial Guinea'),
    ('ERI', 'Eritrea'),
    ('EST', 'Estonia'),
    ('ETH', 'Ethiopia'),
    ('FRO', 'Faeroe Islands'),
    ('FLK', 'Falkland Islands (Malvinas)'),
    ('FJI', 'Fiji'),
    ('FIN', 'Finland'),
    ('GAB', 'Gabon'),
    ('GMB', 'Gambia'),
    ('GEO', 'Georgia'),
    ('DEU', 'Germany'),
    ('GHA', 'Ghana'),
    ('GIB', 'Gibraltar'),
    ('GRC', 'Greece'),
    ('GRL', 'Greenland'),
    ('GRD', 'Grenada'),
    ('GLP', 'Guadeloupe'),
    ('GUM', 'Guam'),
    ('GTM', 'Guatemala'),
    ('GGY', 'Guernsey'),
    ('GIN', 'Guinea'),
    ('GNB', 'Guinea-Bissau'),
    ('GUY', 'Guyana'),
    ('HTI', 'Haiti'),
    ('VAT', 'Holy See (Vatican City)'),
    ('HND', 'Honduras'),
    ('HUN', 'Hungary'),
    ('ISL', 'Iceland'),
    ('IND', 'India'),
    ('IDN', 'Indonesia'),
    ('IRN', 'Iran'),
    ('IRQ', 'Iraq'),
    ('IRL', 'Ireland'),
    ('IMN', 'Isle of Man'),
    ('ISR', 'Israel'),
    ('ITA', 'Italy'),
    ('JAM', 'Jamaica'),
    ('JPN', 'Japan'),
    ('JEY', 'Jersey'),
    ('JOR', 'Jordan'),
    ('KAZ', 'Kazakhstan'),
    ('KEN', 'Kenya'),
    ('KIR', 'Kiribati'),
    ('KWT', 'Kuwait'),
    ('KGZ', 'Kyrgyzstan'),
    ('LAO', 'Lao People\'s Democratic Republic'),
    ('LVA', 'Latvia'),
    ('LBN', 'Lebanon'),
    ('LSO', 'Lesotho'),
    ('LBR', 'Liberia'),
    ('LBY', 'Libyan Arab Jamahiriya'),
    ('LIE', 'Liechtenstein'),
    ('LTU', 'Lithuania'),
    ('LUX', 'Luxembourg'),
    ('MKD', 'Macedonia'),
    ('MDG', 'Madagascar'),
    ('MWI', 'Malawi'),
    ('MYS', 'Malaysia'),
    ('MDV', 'Maldives'),
    ('MLI', 'Mali'),
    ('MLT', 'Malta'),
    ('MHL', 'Marshall Islands'),
    ('MTQ', 'Martinique'),
    ('MRT', 'Mauritania'),
    ('MUS', 'Mauritius'),
    ('MYT', 'Mayotte'),
    ('MEX', 'Mexico'),
    ('FSM', 'Micronesia, Federated States of'),
    ('MCO', 'Monaco'),
    ('MNG', 'Mongolia'),
    ('MNE', 'Montenegro'),
    ('MSR', 'Montserrat'),
    ('MAR', 'Morocco'),
    ('MOZ', 'Mozambique'),
    ('MMR', 'Myanmar'),
    ('NAM', 'Namibia'),
    ('NRU', 'Nauru'),
    ('NPL', 'Nepal'),
    ('NLD', 'Netherlands'),
    ('ANT', 'Netherlands Antilles'),
    ('NCL', 'New Caledonia'),
    ('NZL', 'New Zealand'),
    ('NIC', 'Nicaragua'),
    ('NER', 'Niger'),
    ('NGA', 'Nigeria'),
    ('NIU', 'Niue'),
    ('NFK', 'Norfolk Island'),
    ('MNP', 'Northern Mariana Islands'),
    ('NOR', 'Norway'),
    ('PSE', 'Occupied Palestinian Territory'),
    ('OMN', 'Oman'),
    ('PAK', 'Pakistan'),
    ('PLW', 'Palau'),
    ('PAN', 'Panama'),
    ('PNG', 'Papua New Guinea'),
    ('PRY', 'Paraguay'),
    ('PER', 'Peru'),
    ('PHL', 'Philippines'),
    ('PCN', 'Pitcairn'),
    ('POL', 'Poland'),
    ('PRT', 'Portugal'),
    ('PRI', 'Puerto Rico'),
    ('QAT', 'Qatar'),
    ('KOR', 'Republic of Korea'),
    ('MDA', 'Republic of Moldova'),
    ('REU', 'Reunion'),
    ('ROU', 'Romania'),
    ('RUS', 'Russian Federation'),
    ('RWA', 'Rwanda'),
    ('BLM', 'Saint-Barthelemy'),
    ('SHN', 'Saint Helena'),
    ('KNA', 'Saint Kitts and Nevis'),
    ('LCA', 'Saint Lucia'),
    ('MAF', 'Saint-Martin (French part)'),
    ('SPM', 'Saint Pierre and Miquelon'),
    ('VCT', 'Saint Vincent and the Grenadines'),
    ('WSM', 'Samoa'),
    ('SMR', 'San Marino'),
    ('STP', 'Sao Tome and Principe'),
    ('SAU', 'Saudi Arabia'),
    ('SEN', 'Senegal'),
    ('SRB', 'Serbia'),
    ('SYC', 'Seychelles'),
    ('SLE', 'Sierra Leone'),
    ('SGP', 'Singapore'),
    ('SVK', 'Slovakia'),
    ('SVN', 'Slovenia'),
    ('SLB', 'Solomon Islands'),
    ('SOM', 'Somalia'),
    ('ZAF', 'South Africa'),
    ('ESP', 'Spain'),
    ('LKA', 'Sri Lanka'),
    ('SDN', 'Sudan'),
    ('SUR', 'Suriname'),
    ('SJM', 'Svalbard and Jan Mayen Islands'),
    ('SWZ', 'Swaziland'),
    ('SWE', 'Sweden'),
    ('CHE', 'Switzerland'),
    ('SYR', 'Syrian Arab Republic'),
    ('TJK', 'Tajikistan'),
    ('THA', 'Thailand'),
    ('TLS', 'Timor-Leste'),
    ('TGO', 'Togo'),
    ('TKL', 'Tokelau'),
    ('TON', 'Tonga'),
    ('TTO', 'Trinidad and Tobago'),
    ('TUN', 'Tunisia'),
    ('TUR', 'Turkey'),
    ('TKM', 'Turkmenistan'),
    ('TCA', 'Turks and Caicos Islands'),
    ('TUV', 'Tuvalu'),
    ('UGA', 'Uganda'),
    ('UKR', 'Ukraine'),
    ('ARE', 'United Arab Emirates'),
    ('GBR', 'United Kingdom'),
    ('TZA', 'United Republic of Tanzania'),
    ('USA', 'United States of America'),
    ('VIR', 'United States Virgin Islands'),
    ('URY', 'Uruguay'),
    ('UZB', 'Uzbekistan'),
    ('VUT', 'Vanuatu'),
    ('VEN', 'Venezuela (Bolivarian Republic of)'),
    ('VNM', 'Viet Nam'),
    ('WLF', 'Wallis and Futuna Islands'),
    ('ESH', 'Western Sahara'),
    ('YEM', 'Yemen'),
    ('ZMB', 'Zambia'),
    ('ZWE', 'Zimbabwe'),
)
# Create your models here.
class UserProfile(models.Model):
    GENDER_CHOICES=(
                    ('m','Male'),
                    ('f','Female'),
                )
    user = models.OneToOneField(User)
    screen_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=2,choices=GENDER_CHOICES)
    about = models.TextField(max_length=200)
    web = models.TextField(max_length=50)
    country = models.CharField(max_length=255,choices=COUNTRIES)
    
    
    
class Work(models.Model):
    user = models.ForeignKey(User)
    employer_name = models.CharField(max_length=50,blank = False)
    designation = models.CharField(max_length=50)
    employer_country = models.CharField(max_length=255,choices=COUNTRIES)
    employment_year = models.IntegerField(max_length=4)
    
    
class Education(models.Model):
    LEVEL_CHOICES = (
                     ('h','High School'),
                     ('g','Graduation'),
                     ('c','Certificate'),
            )
    user = models.ForeignKey(User)
    institute_name = models.CharField(max_length=50,blank = False)
    institute_country = models.CharField(blank = False,max_length=255,choices=COUNTRIES)
    institute_year = models.IntegerField(max_length=4)
    education_level  = models.CharField(choices = LEVEL_CHOICES,max_length=30)


""" This class contains the address the physical contact details      """    
class Contact(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length = 150)
    city = models.CharField('City/town',max_length=30)
    state = models.CharField('State/Province',max_length=30)
    country = models.CharField(max_length=255,choices=COUNTRIES)

""" This class contains the Emails details      """
class EmailAccount(models.Model):
    user = models.ForeignKey(User)
    email = models.CharField(max_length=50,blank=False)
    status = models.BooleanField()
    public = models.BooleanField()

""" This class contains the Internet Messengers of each Account like Skype,yahoo,msn etc """    
class ImAccount(models.Model):
    user = models.ForeignKey(User)
    screen_name = models.CharField(max_length=30,blank=False)
    status = models.BooleanField()
    public = models.BooleanField()
    
""" This class contains the mobile phone details  """
class MobileAccount(models.Model):
    user = models.ForeignKey(User)
    mobile_no = models.IntegerField(max_length=15,blank=False)
    public = models.BooleanField()
    status = models.BooleanField()

""" This class contains the credit accounts used for transaction by application   """
class CreditAccount(models.Model):
    user = models.ForeignKey(User)
    credit_account = models.CharField(blank=False,max_length=255)
  
class AccountLanguage(models.Model):
    user = models.ForeignKey(User)
    language = models.CharField(blank=False,max_length=255)


