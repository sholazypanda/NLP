
Dependencies:

used version 3.5
pip3 install numpy
pip3 install nltk


These packages should be present inside 3.5 version/site-packages to make the code run.
3.5/lib/python3.5/site-packages/numpy and 3.5/lib/python3.5/site-packages/nltk


Development work was done in Ipython notebook Python version 3.5
Corpus file should be present in same directory.

Once there is no module error.

Use the exact command::

python Homework1NLP.py corpus.txt "The chief executive said that the company’s profit was going down last year." "The president said the revenue was good last year."

For my local machine(Mac OSX) command line: I had to set this up in my program:
after , I have commented that line for now, its the path in my system.
import sys
sys.path.append("/Library/Frameworks/Python.framework/Versions/3.5/lib/python3.5/site-packages")

I have attached the output that I got as output.txt