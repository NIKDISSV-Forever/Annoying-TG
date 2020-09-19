import os

banner = """
      {_                                                                 {___ {______   {____   
     {_ __                                           {_                       {__     {_    {__ 
    {_  {__    {__ {__  {__ {__     {__    {__   {__   {__ {__     {__        {__    {__        
   {__   {__    {__  {__ {__  {__ {__  {__  {__ {__ {__ {__  {__ {__  {__     {__    {__        
  {______ {__   {__  {__ {__  {__{__    {__   {___  {__ {__  {__{__   {__     {__    {__   {____
 {__       {__  {__  {__ {__  {__ {__  {__     {__  {__ {__  {__ {__  {__     {__     {__    {_ 
{__         {__{___  {__{___  {__   {__       {__   {__{___  {__     {__      {__      {_____    
"""
os.system('clear')
print(banner)
try:
	from telethon import TelegramClient, sync
except ModuleNotFoundError:
	os.system('pip install -U telethon')
	os.system('pip install --upgrade pip')
	
from time import sleep
import random

global n, client, num, name, msg, SLP
SLP = 0
num = 1
n = '\n'


session = input('Имя сессии: ')
if session == '' or session == ' ':
	session = random.choice((os.name,  os.getlogin(), str(os.getpid())))

print(session)

sdir = os.getcwd() + '/saved/'

if not os.path.exists(sdir):
	os.mkdir(sdir)

fid = sdir + session + '.id'
hashf = sdir + session + '.hash'

if os.path.isfile(fid):
	f = open(fid, 'r')
	api_id = f.read()
	f.close()
else:
	api_id = int(input('ID приложения: '))
	f = open(fid, 'w')
	f.write(str(api_id))
	f.close()
	
if os.path.isfile(hashf):
	f = open(hashf, 'r')
	api_hash = f.read()
	f.close()
else:
	api_hash = input('HASH приложения: ')
	f = open(hashf, 'w')
	f.write(str(api_hash))
	f.close()

client = TelegramClient(session, api_id, api_hash)
client.start()

global actlist

actlist = """
[0] - Данные моего аккаунта.
[1] - Флуд сообщениями.
[2] - Флуд файлами.
[3] - Все чаты в которых есть я.
[4] - История сообщений какого-н. чата.
[5] - Флуд с упоминанием в сообщении.
"""
def Q():
	whatAct = input(actlist + n + 'Введите какую-нибудь цифру: ')
	return whatAct

def profile():
	
	r = input('Введите имя профиля / чата: ')
	try:
		if r[0] == '+':
			pl = '+'
		else:
			pl = ''
		r = int(pl + r)
	except:
		if r[0] != '+':
			if r[0] != '@' and r != 'me':
				r = '@' + r
			elif r == '' or r == ' ':
				r = 'me'
		else:
			r = str(r)
	del(pl)
			
	return r
	

	
def while1msg(msg, name):
	global num
	num = 1
	while 1:
		client.send_message(name, msg.replace('%%num%%', str(num)).replace('%%name%%', str(name)).replace('%%randint%%', str(random.randint(-100000000, 1000000000))).replace('%%rfloat%%', str(random.uniform(-1, 1))).replace('%%rbit%%', str(os.urandom(1))).replace('%%reff%%', random.choice(('__', '**', '```'))).replace('%%rchr%%', chr(random.randint(1, 110000))))
		print('Отправлено сообщение %s, для %s, %s раз(а).' % (msg, name, num))
		
		num += 1
		sleep(SLP)
		
def spamm(msg, name, col):
	global num
	num = 1
	while num <= col:
		try:
			client.send_message(name, msg.replace('%%num%%', str(num)).replace('%%name%%', str(name)).replace('%%randint%%', str(random.randint(-100000000, 1000000000))).replace('%%rfloat%%', str(random.uniform(-1, 1))).replace('%%rbit%%', str(os.urandom(1))).replace('%%reff%%', random.choice(('__', '**', '```'))).replace('%%rchr%%', chr(random.randint(1, 110000))))
			print('Отправлено сообщение %s, для %s, %s раз(а).' % (msg, name, num))
			num += 1
			sleep(SLP)
		except Exception as er:
			print(er)
			
def while1msgF(msg, name):
	global num
	num = 1
	while 1:
		client.send_file(name, msg.replace('%%num%%', str(num)).replace('%%name%%', str(name)).replace('%%randint%%', str(random.randint(-100000000, 1000000000))).replace('%%rfloat%%', str(random.uniform(-1, 1))).replace('%%rbit%%', str(os.urandom(1))).replace('%%reff%%', random.choice(('__', '**', '```'))).replace('%%rchr%%', chr(random.randint(1, 110000))))
		print('Отправлено сообщение %s, для %s, %s раз(а).' % (msg, name, num))
		
		num += 1
		sleep(SLP)
		
def spammF(msg, name, col):
	global num
	num = 1
	while num <= col:
		
		try:
			client.send_file(name, msg.replace('%%num%%', str(num)).replace('%%name%%', str(name)).replace('%%randint%%', str(random.randint(-100000000, 1000000000))).replace('%%rfloat%%', str(random.uniform(-1, 1))).replace('%%rbit%%', str(os.urandom(1))).replace('%%reff%%', random.choice(('__', '**', '```'))).replace('%%rchr%%', chr(random.randint(1, 110000))))
			print('Отправлено сообщение %s, для %s, %s раз(а).' % (msg, name, num))
			num += 1
			sleep(SLP)
			
		except Exeption as er:
			print(er)
			
def sleeper():
	global SLP
	SLP = input('Введите задержку (0): ')
	try:
		SLP = int(SLP)
		if SLP < 0:
			SLP = 0
	except Exception:
		SLP = 0
	return SLP

def mainQ(C):
		if C <= 0:
			print(n + client.get_me().stringify() + n)
		elif C == 1:
			while 1:
				col = input('0 - Бесконечно, или введите сумму сообщений (100): ')
				if col == '':
					col = '100'
				try:
					col = int(col)
					SLP = sleeper()
					break
				except Exception as er:
					print(er)
			if col <= 0:
				msg = input('Введите сообщение: ')
				name = profile()
				while1msg(msg, name)
			else:
				msg = input('Введите сообщение: ')
				name = profile()
				spamm(msg, name, col)
				
		elif C == 2:
			
			while 1:
				col = input('0 - Бесконечно, или введите сумму сообщений (100): ')
				if col == '':
					col = '100'
				SLP = sleeper()
				try:
					col = int(col)
					break
				except Exception as er:
					print(er)



			if col <= 0:
				msg = input('Введите путь к файлу или URL: ')
				name = profile()
				while1msgF(msg, name)
			else:
				msg = input('Введите путь к файлу или URL: ')
				name = profile()
				spammF(msg, name, col)
				
		elif C == 3:
			for dialog in client.iter_dialogs():
				id = str(dialog.id)
				print(n + dialog.name + n + id)
				
		elif C == 4:
			name = profile()
			for msgg in client.iter_messages(name):
				id = str(msgg.id)
				print(id + ':', msgg.text + n)
		elif C == 5:
			msg = input('Введите сообщение: ')
			name = profile()
			SLP = sleeper()
			num = 1
			for msgg in client.iter_messages(name):
				text = msgg.text
				print(msgg.id, text, str(num))
				
				try:
					msgg.reply(msg.replace('%%text%%', str(text)).replace('%%num%%', str(num)).replace('%%randint%%', str(random.randint(-100000000, 1000000000))).replace('%%rfloat%%', str(random.uniform(-1, 1))).replace('%%rbit%%', str(os.urandom(1))).replace('%%reff%%', random.choice(('__', '**', '```'))).replace('%%rchr%%', chr(random.randint(1, 110000))))
					num += 1
					sleep(SLP)
				except Exception as er:
					print(er)
				

def main():
	try:
		whatAct = Q()
		if whatAct == '':
			exit()
		whatAct = int(whatAct)
	except Exception as er:
		print(er)
		whatAct = Q()
	else:
		C = whatAct
		del(whatAct)
	mainQ(C)
	input('Нажмите Enter' + n)
	main()
	
main()
