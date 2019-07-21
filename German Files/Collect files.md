Our goal here is to obtain all the german text files. The data format for the text files is as follows:


20XX-XX-XX_TIME_CountryCode_ChannelName.txt


The Country code for Germany is DE. However, not all the files from Germany will be in German, as some of them may be in English, or some may be German translations of English.
We want only the files which have German as the language. 


In each text file, in the header section, the language code is specified, such as:
LAN|POR.


In our case, the language code for German is DEU.


Hence, we would extract all the files containing the metadata LAN|DEU from the files with country code DE.


Thus, we create two directories:
mkdir input_files
mkdir text_files_only


We can skip the non-german files as:


 LAN=$( grep -P "^(LAN|CC.|TR.|ASR_[0-9]+)\|" ${DDIR}/${FIL} ) ; if [ -n "$LAN" ] ; then if [ "${LAN#*|}" != "DEU" ] ; then continue ; fi ; fi


OR


find . ! -name '*.txt’ ! -path '*.*' -exec grep 'LAN|XXX' {} /dev/null \;
where we can substitute XXX for whatever language we want to skip, such as English in this case.
