# pyrouge setup
Step 1: `pip install -r requirements.txt`

Step 2: 
```
git clone https://github.com/andersjo/pyrouge.git

pyrouge_set_rouge_path /to/yourpath/pyrouge/tools/ROUGE-1.5.5

```

Step 3: `cd /pyrouge/tools/ROUGE-1.5.5/data; rm WordNet-2.0.exc.db`

Step 4: `./WordNet-2.0-Exceptions/buildExeptionDB.pl ./WordNet-2.0-Exceptions ./smart_common_words.txt ./WordNet-2.0.exc.db`

Step 5: `python test_cal_rouge.py`
