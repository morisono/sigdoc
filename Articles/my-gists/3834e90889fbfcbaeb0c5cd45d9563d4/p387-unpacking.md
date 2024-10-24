
1. Right click unpack target file and run.
3. find 'search' section from tag file, record the value i.e. '1020'.
4. run target file
   ```
   pe-sieve.exe /pid 6860 /imp
   ```
2. check folder created named "process_6860", then dump files will be in it.
3. open the dumped file, load tag file from 'star-mark' > Load
4. click the value same as recorde
5. right click the line includes the value, then click Set EP.
6. change access right 6 to E in UPX0
7. click Save executable as...