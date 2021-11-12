# AMICorpus-Meeting-Transcript-Extraction
This python script can be used to convert the AMI corpus meeting transcripts to a speaker by speaker conversation or dialogue discourse for each meeting.     
An example from the transcript:     
     
C:The basic word importance is off-line.     
E:Yeah Okay.     
C:as well The combined measure might not be if we want to wait what.     
C:the user has typed in into the search.     
E:Okay 'Kay.     
D:Uh mine's gonna be mostly using the off-line But the actual stuff it's doing will be on-line But it won't be very.     
D:um processor intensive or memory intensive I don't.     
     
`Note: The AMI corpus has many instances of cross talk which I have tried to eliminate using the code. The current code eliminates cross talk (to an extent) but it could use some improvement`

## The AMI Corpus:
You can find out more about the AMI Corpus [here][amilink]

## See it in action:
Just clone this repo and do:
```sh
$ python3 preprocess.py
```
The output is saved in EN2001a.txt

## Prerequisites

 - You can download the AMI corpus from the [official download page][ami] of the AMI Corpus. Click the *AMI manual annotations v1.6.2* under the **Annotations** heading. That should download the zip file.
 - Tested on Python >= 3.6 (It should work with any version of python 3 though)

## How to use
In this repo I have taken the example of the EN2001a meeting and converted it to EN2001a.txt. You can refer to this example and follow these steps:
 1. First unzip the manual annotations folder from the above downloaded file. The individual speaker transcripts are located in the words folder of the downloaded annotations file. Go to this folder.
 2. Copy the meeting speakers xml for the meeting you want, convert them to a txt file (any text editor will work), and paste them to a folder in the repo folder. For the example, in this repo I copied 'EN2001a.A.words.xml, EN2001a.B.words.xml, EN2001a.C.words.xml, EN2001a.D.words.xml, EN2001a.E.words.xml', converted them to txt and pasted them in the EN2001a folder.
 3. In the `preprocess.py` code, put the destination of the above files in the file_list list as well as the speaker names in the speakers list (Refer to the code of this repo, it has the EN2001a example defined).
 4. Define your output file at the end of `preprocess.py`
 5. Run 
    ```sh
    $ python3 preprocess.py
    ```
    The output will be saved in the output file you defined
 
[//]: # (These are reference links)


   [ami]: <http://groups.inf.ed.ac.uk/ami/download/>
   [amilink]: <http://groups.inf.ed.ac.uk/ami/corpus/overview.shtml>

    

