## Movie Query Command Line Tool

This project queries by Field Name of the CSV file which is located in the URL below. 



http://www.hometheaterinfo.com/dvdlist.htm

Particularly this file 
http://www.hometheaterinfo.com/download/dvd_csv.zip

The python program essentially takes the URL from above and works with the file directly.   
No need to download the file and unzip etc etc.   
The software will automatically go to the URL above and use the file directly. 

Be aware that the Field name are case senstive, therefore be sure to use fields as shown below

(DVD_Title,Studio,Released,Status,Sound,Versions,Price,Rating,Year,Genre,Aspect,UPC,DVD_ReleaseDate,ID,Timestamp)

## Code Example
To run the Command Line Tool under terminal (be sure that you have pandas installed)

python movie_query.py -c [FIELD NAME] -s [Movie Title, Studio Name, Versions, Price, etc]




## Motivation

This project was recommended by Prospective Employer.

## Installation
-Ensure that Python 2.7.6 
-In case Pandas is not installed - (assuming you are using linux (debian ubuntu flavor)
-This also assumes that python automatically has argparse, csv, requests, zipfile, urllib2, io libraries.

    ~: sudo apt-get install python-pandas 
 
    (as this will install all necessary libraries including numpy)



## Tests


Examples
  
     python movie_query.py -c DVD_Title -s Jurrasic Park
     python movie_query.py -c Price -s 14.95
     python movie_query.py -c Year -s 2008

## Contributors

Daniel Chan @pookeye on twitter.

## License

Open Source
