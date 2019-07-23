#!/bin/bash

# We want all files with the country code ES
# Then all files with a language tag for Spanish, but not those where the Spanish subtitles were just translations of English Audio

FILELIST="/mnt/sita_02/UUID_list/filename_uuid_list.txt"
STEM="/mnt/netapp/tv/TV_"
#grep "_ES_" $FILELIST | while read -r FIL ; do
#       FIL=$(echo $FIL | grep -Po "^(.*?)(?=,)")
#       DDIR=${STEM}${FIL:0:4}/${FIL:0:7}/${FIL:0:10}
#       cp ${DDIR}/${FIL} 1_inputfiles/
#done;


# Process each text file in turn
#for FIL in $( find /mnt/netapp/tv -type f -maxdepth 4 -name "*.txt" 2> /dev/null ); do
for FIL in $( grep -Po "^(.*?)(?=,)" $FILELIST 2> /dev/null ); do
        DDIR=${STEM}${FIL:0:4}/${FIL:0:7}/${FIL:0:10}

        # Skip non-Spanish
        #echo $FIL
        LAN=$( grep -P "^(LAN|CC.|TR.|ASR_[0-9]+)\|" ${DDIR}/${FIL} ) ; if [ -n "$LAN" ] ; then if [ "${LAN#*|}" != "SPA" ] ; then continue ; fi ; fi

        echo $FIL

done;
