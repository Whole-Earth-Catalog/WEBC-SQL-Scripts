# Whole Earth Book Catalog Project - MySQL Scripts
This directory contains queries and building scripts for the mysql database.

## MySQL on the Silver Surfer
For the complete database use:
$ mysql -u root -p                
$ use webc                
Documentation for complete data set in FullDatabase_Guide.pdf
 
For the database created in build use (this database is an example of building):                   
access wc (worldcat) database  using:           
$ mysql -u wcuser -p         
$ use wc           
                         
## Important tags:
- tag245: 
	- $a has title of record
- tag100:
	- $a has associated name
- tag260:
	- $a has place of publication
	- $b has name of publisher 
	- $c has date of publication
- tag008:
	- has the control number, with date code and other useful info
	- to use this field, use the SQL substring function (SUBSTRING(data, 8, 4) as year), SUBSTRING(data, 36, 3) as language, SUBSTRING(data, 16, 3) as country, etc. )
