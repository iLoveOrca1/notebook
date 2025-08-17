Category: Forensic
Tags: Disk Dump
Tools: autopsy

1. You may find something interesting in "All Deleted Files"

2. Have you checked all user? Including root? You can access root folder in disk dump ya know

3. You may find something useful in .bash_history

4. Tired of typing the absolute path of the file inside your directory? Fear not the "realpath" command is for you
```
kali@kali:~/Downloads$ realpath flag.txt
/home/kali/Downloads/flag.txt
```


5. When you download something from autopsy web you may find the file format was like these when opened:
```
Contents Of File: /3/root/.ash_history


touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

```
# These are just a some file information
Contents Of File: /3/root/.ash_history

# Below are the actual inside of the file
touch flag.txt
nano flag.txt 
apk get nano
apk --help
apk add nano
nano flag.txt 
openssl
openssl aes256 -salt -in flag.txt -out flag.txt.enc -k unbreakablepassword1234567
shred -u flag.txt
ls -al
halt
```

