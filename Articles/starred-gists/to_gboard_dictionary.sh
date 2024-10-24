#!/usr/bin/env sh

echo '# Gboard Dictionary version:1' > dictionary.txt
cut -f 1,2 cute_AA.txt | sed 's/$/\tja-JP/' >> dictionary.txt
7z a PersonalDictionary.zip dictionary.txt
rm dictionary.txt
