import progressbar
import os
from progressbar import ProgressBar

if os.path.isfile('cpu.txt') == True:
    os.remove('cpu.txt')

if os.path.isfile('cpu1.txt') == True:
     os.remove('cpu1.txt')

pbar = ProgressBar().start()

def job():
    total_steps = 3
    pbar.update(0)
    os.system('python NetworkApp.py')
    pbar.update((1/3)*100)
    os.system('python graph.py')
    pbar.update((2/3)*100)
    os.system('python ConfigMgmt.py')
    pbar.update((3/3)*100)
    pbar.finish()

job()