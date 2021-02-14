# Calculate the accuracy of a baseline that simply predicts "London" for every
#   example in the dev set.
# Hint: Make use of existing code.
# Your solution here should only be a few lines.
import utils
from tqdm import tqdm
import torch

correct = 0
total = 0
# with open(args.outputs_path, 'w') as fout:
predictions = []
for line in tqdm(open('birth_dev.tsv')):
    # x = line.split('\t')[0]
    # x = x + '⁇'
    # x = torch.tensor([pretrain_dataset.stoi[s] for s in x], dtype=torch.long)[None,...].to(device)
    # pred = utils.sample(model, x, 32, sample=False)[0]
    # completion = ''.join([pretrain_dataset.itos[int(i)] for i in pred])
    # pred = completion.split('⁇')[1]
    predictions.append("London")
    # fout.write(pred + '\n')
total, correct = utils.evaluate_places('birth_dev.tsv', predictions)
if total > 0:
    print('Correct: {} out of {}: {}%'.format(correct, total, correct/total*100))
