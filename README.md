# rename-files
(for renaming pictures)

<p>I usually compile pictures from many sources into my album folders. Taken from different devices and downloaded from facebook and links from friends, organization can get messy. Instead of individually going around changing names manually, I wrote a simple program to rename and organize files by the timestamp of last modification.</p>
<p>This program takes one string argument for the filepath to the directory containing the files. Names of folders in that directory are ignored. Timestamps are written in the format <b>YYYYMMDD_HHMMSS</b>. If there are multiple files with that timestamp, we add <b>_CTR</b> to the end of the name where CTR is just increments with every file with the same timestamp.</p>
