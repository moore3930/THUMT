export PYTHONPATH="${PYTHONPATH}:/Users/wudi39/github/robust-NLU/THUMT"
python ./thumt/bin/translator.py --models transformer --input ../data/snips/test/data.query --output ../data/snips/test/data.infer --vocabulary ../data/snips/vocab.q.txt ../data/snips/vocab.s.txt --checkpoints train/eval --parameters=device_list=[0],decode_alpha=0.6
