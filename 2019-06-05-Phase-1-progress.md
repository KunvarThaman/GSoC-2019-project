---
layout: home
author_profile: true
title: Phase 1 Progress
published: true
---
For the first week, I got myself familiarized with the system. Peter Uhrig, my mentor, provided me an account on Pisa where I’ll be working. 

I found the Russian Corpus there, and took a look at Red Hen’s data format to understand it. Then I went through the existing code, and the pipeline, and copied some files over to a temp directory and played around a little to get an understanding of how the multilingual pipeline worked.

**Update**: Almost the entire day was taken up when I accidentally removed my ssh key from the authorized_keys. I messaged one of the admins, Mark Turner, who helped set up our system on galina, with the problem and was able to recover it (made a backup after that!!)

**Update**: After discussing some tasks with Peter, I have three goals to complete:

1. Improving the conversion of broken files, files that come with some sort of wrong encoding. The existing solution worked but broke things such as tags which should be kept. I need to create a program which converts the broken files while retaining this kind of information. 

2. Including <turn></turn> tags around speakers’ turns, where they are marked in the input. Usually, they are marked with a dash at the beginning of a line. This was an easy task, I just had to identify whenever a dash was at the beginning of the line and adding tags around the text between every pair. This task was made easier by the use of Prannoy’s code for his 2017 project, which I edited. I ran the code on some sample files and it works as desired. I’ll be updating the code (after testing a range of files) on the GitHub repo for this project soon.

3. Some of the files weren’t being processed completely. I had to figure out why this was happening and fix it. Initially, having no clue as to how to approach this, I found the files which weren’t being processed completely and tried manually looking at whatever problems there could be.

When I didn’t find any proper solution, I asked my mentor, Peter, for any idea he might have to approaching this. He suggested using print statements and going through the file to check what’s the problem. 

My approach then was to force the UTF-8 encoding on to the files. I tried this, and then started going from statement to statement. There were some Russian characters which weren’t being converted to UTF-8. I’ve searched online for similar issues and I think I have one which might work. I’ll update this page with the results accordingly.

