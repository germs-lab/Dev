#usage: bash Tax.sh
for line in $(cat RefSoilTax.unix.txt);
 do wget -O $line.html "http://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=$line";
done

grep "<dd><a ALT" *.html > TaxInfo.txt