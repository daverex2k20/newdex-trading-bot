false  # Want to set $? to non-zero return
while [ $? -ne 0 ]
do

   counter=$((counter+1))

   if [ $counter -gt 5 ]
   then
           echo "Maximum number of newdex price query attempts reached."
   fi

   # Get newdex prices
   python newdex_prices.py >> cron_prices.log


done
