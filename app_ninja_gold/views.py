from django.shortcuts import render, redirect
import random
from datetime import datetime
# import time
# from time import strftime

def index(request):
  print('\n-------- "/" INDEX -------')
  # check if gold is in session:
  if 'gold' not in request.session:
    request.session['gold'] = 0
    request.session['logs'] = []
    
  print(f'💰 GOLD = {request.session["gold"]}')
  return render(request, 'index.html')

def process_money(request):
  print('\n-------- "/process_money" () -------')
  if request.method == "POST":
    
    timestamp = datetime.now().strftime("%Y/%m/%d %I:%M %p")
    output_print = ""
    
    if request.POST['where_from'] == "farm":
      print('👨‍🌾 clicked from FARM!')
      # add random 10-20 gold
      gold_earned = random.randint(10,20)
      
      # log = f"Earned {gold_earned} from Farm! ({timestamp})"
      log = f"<li class='green'> Earned {gold_earned} from Farm! ({timestamp}) </li>"
      request.session['gold'] += gold_earned
      output_print = f"✅ Earned {gold_earned}💰 from {request.POST['where_from']}! ({timestamp})"
      print(output_print)
      # print('-=-=-==-=', output_print_html)
      # if 'my_output' in request.session:
      #   output_print_html = request.session['my_output']
      #   output_print_html.append(f"✅ Earned {gold_earned}💰 from {request.POST['where_from']}! ({timestamp})")
      #   request.session['my_output'] = output_print_html
      # else:
      #   output_print_html.append(output_print)
      #   request.session['my_output'] = output_print_html

    if request.POST['where_from'] == "cave":
      print('🗻 clicked from CAVE')
      request.session['gold'] += random.randint(5,10)
      # log = f"Earned {request.session['gold']} from Cave! ({timestamp})"
      log = f"<li class='green'> Earned {request.session['gold']} from Cave! ({timestamp}) </li>"
      
    if request.POST['where_from'] == "house":
      print('🏠 clicked from HOUSE')
      request.session['gold'] += random.randint(2,5)
      # log = f"Earned {request.session['gold']} from House! ({timestamp})"
      log = f"<li class='green'> Earned {request.session['gold']} from House! ({timestamp}) </li>"
      
    if request.POST['where_from'] == "casino":
      print('🎲 clicked from CASINO')
      steal_or_gift = random.randint(0,1)
      print('❓❓❓❓❓❓', steal_or_gift)
      if steal_or_gift == 0:
        # steal
        my_gold = random.randint(0,50)
        request.session['gold'] -= my_gold
        # log = f"Lost! -{request.session['gold']} from Casino! ({timestamp})"
        log = f"<li class='red'> Lost! -{my_gold} from Casino! ({timestamp}) </li>"
      elif steal_or_gift == 1:
        # gift
        my_gold = random.randint(0,50)
        request.session['gold'] += my_gold
        # log = f"Earned {request.session['gold']} from Casino! ({timestamp})"
        log = f"<li class='green'> Earned {my_gold} from Casino! ({timestamp}) </li>"
    
    request.session['logs'].append(log)
    # request.session['gold'] += amount_to_add
  return redirect('/')

def clear_session(request):
  print('\n === ⛔ DESTROY SESSION 💥 ===\n')
  request.session.clear()
  if 'gold' in request.session:
    del request.session['gold']
  
  return redirect('/')