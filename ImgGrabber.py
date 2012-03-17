#coding: utf-8
import sys,urllib2,re,os,MainWindow,threading,time
from PyQt4 import QtCore, QtGui


class Downloader():
	def setPath(self):
		path=''
		if str(window.ui.path_line.text())!='':path=str(window.ui.path_line.text())+'/'
		if str(window.ui.tage_line.text())=='':path+='No_Tag/'
		else:path+=str(window.ui.tage_line.text().replace(':',' '))+'/'
		if os.access(path,os.F_OK)==False:os.makedirs(path)
		return path
	def download(self,fn,p):
		def dl(url,path,treads,downloaded,p):
			print '\nDownload: '+url
			t,d=treads,downloaded
			opened=False
			if url.split('/')[2]=='behoimi.org':headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1)','Referer':'http://behoimi.org/data/ff/f3/'}
			else:headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1)'}
			req=urllib2.Request(url,None,headers)
			while opened==False:
				try:img=urllib2.urlopen(req)
				except:
					print '\nError img url'
					time.sleep(120)
				else:opened=True
			img_name=path+img.geturl().replace('%20',' ').replace('%21','!').replace('%28','(').replace('%29',')').replace('%26','&').replace('%3B',';').split('/')[-1]
			if os.access(img_name,os.F_OK)!=True or os.path.getsize(img_name)==0:
				img_file=open(img_name,'wb')
				img_file.write(img.read())
				img_file.close()
			d[0][0]+=1
			p.setValue(d[0][0])
			t[0][0]+=1
			print '\nComplete: '+url
		file=open(fn,'r')
		path=self.setPath()
		treads=[[5]]
		downloaded=[[0]]
		for i in file.readlines():
			tread=threading.Thread(target=dl,args=(i,path,treads,downloaded,p))
			tread.daemon=False
			tread.start()
			treads[0][0]-=1
			time.sleep(0.5)
			while treads[0][0]==0:time.sleep(3)
		file.close()
		while treads[0][0]!=5:time.sleep(3)
class Parser(Downloader):
	def chekStatus(self,treads):
		complit=False
		if treads!=[]:
			while complit==False:
				for i in treads[:]:
					complit=True
					if i.isAlive()==True:
						complit=False
						break
				time.sleep(3)
		window.ui.statusbar.showMessage('Complete...')
		window.ui.downloadBtn.setEnabled(True)
	def startParser(self,board):
		limit,tag=int(window.ui.num_line.text()),str(window.ui.tage_line.text()).replace('!','%21').replace('&','%26').replace(';','%3B')		
		window.ui.statusbar.showMessage('Grabbing...')
		treads=[]
		for i in board:
			if i=='Konachan.com'or i=='Yande.re'or i=='Danbooru.donmai.us'or i=='Behoimi.org'or i=='Nekobooru.net'or i=='Genso.ws':tread=threading.Thread(target=self.parse0,args=(i,limit,tag,))
			if i=='Chan.sankakucomplex.com'or i=='Idol.sankakucomplex.com':tread=threading.Thread(target=self.parse1,args=(i,limit,tag,))
			if i=='Gelbooru.com':tread=threading.Thread(target=self.parse2,args=(limit,tag,))
			if i=='Animemahou.com':tread=threading.Thread(target=self.parse3,args=(limit,tag,))
			treads.append(tread)
			tread.daemon=False
			tread.start()
		tread=threading.Thread(target=self.chekStatus,args=(treads,))
		tread.daemon=False
		tread.start()
	def openUrl(self,url):
		opened,i=False,0
		while opened==False:
			if i>10:break
			link=None
			try:link=urllib2.urlopen(url)
			except:
				print '\nError open url'
				i+=1
				time.sleep(3)
			else:opened=True
		return link
	def parse0(self,board,limit,tag):#konachan.com oreno.imouto.org danbooru.donmai.us behoimi.org nekobooru.net genso.ws
		def get997(url,page,tag,limit,fn,stop,treads,grabbed):
			print '\nProcess start: '+url+' '+str(page)
			s,t,g=stop,treads,grabbed
			link='http://'+url+'/post?limit='+str(limit)+'&page='+str(page)+'&tags='+tag
			headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)'}
			req=urllib2.Request(link,None,headers)
			urls,i='',0
			link=self.openUrl(req)
			parse=link.read()
			result=re.finditer(r'Post\.register\(\{.+\"file\_url\"\:\".+\".+\}\)',parse)
			for res in result:
				urls+=res.group().split('file_url":"')[1].split('"')[0]+'\n'
				i+=1
				g[0][0]+=1
				if g[0][0]==limit:break
			if i<997:s[0][0]=True
			if g[0][0]<=limit:
				file=open(fn,'a')
				file.write(urls)
				file.close()
			else:g[0][0]-=997
			t[0][0]+=1
			print '\nProcess end: '+url+' '+str(page)
		if board=='Konachan.com':p,fn=window.ui.PB_konachan,'url.konachan'
		if board=='Yande.re':p,fn=window.ui.PB_oreno,'url.yandere'
		if board=='Danbooru.donmai.us':p,fn=window.ui.PB_danboru,'url.danbooru'
		if board=='Behoimi.org':p,fn=window.ui.PB_behomini,'url.behoimi'
		if board=='Nekobooru.net':p,fn=window.ui.PB_nekobooru,'url.nekobooru'
		if board=='Genso.ws':p,fn=window.ui.PB_genso,'url.genso'
		file=open(fn,'w')
		file.close()
		limit_page,i,stop=limit/997+1,0,[[False]]
		treads=[[3]]
		grabbed=[[0]]
		for i in range(limit_page):
			tread=threading.Thread(target=get997,args=(board,i+1,tag,limit,fn,stop,treads,grabbed))
			tread.daemon=False
			tread.start()
			treads[0][0]-=1
			time.sleep(0.5)
			while treads[0][0]==0:time.sleep(3)
			if stop==True:break
		while treads[0][0]!=3:time.sleep(3)
		print '\n'+board+' grabbed: '+str(grabbed[0][0])+' images'
		if grabbed[0][0]!=0:
			p.setMaximum(grabbed[0][0])
			self.download(fn,p)
	def parse1(self,board,limit,tag):#chan.sankakucomplex.com idol.sankakucomplex.com
		def get50(url,page,tag,limit,fn,stop,treads,grabbed):
			print '\nProcess start: '+url+' '+str(page)
			s,t,g=stop,treads,grabbed
			link=self.openUrl('http://'+url+'/post/index?limit=50&tags='+tag+'&page='+str(page))
			parse=link.read()
			result=re.finditer(r'Post\.register\(\{.+\}\)\;',parse)
			loop,urls,i=0,'',0
			for res in result:
				loop+=1
				if page==1:
					if loop<=4:continue
				urls+=res.group().split('file_url":"')[1].split('"')[0]+'\n'
				i+=1
				g[0][0]+=1
				if g[0][0]==limit:break
			if i<50:s[0][0]=True
			if g[0][0]<=limit:
				file=open(fn,'a')
				file.write(urls)
				file.close()
			else:g[0][0]-=50
			t[0][0]+=1
			print '\nProcess end: '+url+' '+str(page)
		if board=='Chan.sankakucomplex.com':p,fn=window.ui.PB_chan,'url.chan'
		if board=='Idol.sankakucomplex.com':p,fn=window.ui.PB_idol,'url.idol'
		file=open(fn,'w')
		file.close()
		limit_page,i,stop=limit/50+1,0,[[False]]
		treads=[[5]]
		grabbed=[[0]]
		for i in range(limit_page):
			tread=threading.Thread(target=get50,args=(board,i+1,tag,limit,fn,stop,treads,grabbed))
			tread.daemon=False
			tread.start()
			treads[0][0]-=1
			time.sleep(0.5)
			while treads[0][0]==0:time.sleep(3)
			if stop==True:break
		while treads[0][0]!=5:time.sleep(3)
		print '\n'+board+' grabbed: '+str(grabbed[0][0])+' images'
		if grabbed[0][0]!=0:
			p.setMaximum(grabbed[0][0])
			self.download(fn,p)
	def parse2(self,limit,tag):#gelbooru.com
		def get25(page,tag,limit,stop,treads,grabbed):
			print '\nProcess start: Gelbooru.com '+str(page)
			s,t,g=stop,treads,grabbed
			try:link=urllib2.urlopen('http://gelbooru.com/index.php?page=post&s=list&tags='+tag+'&pid='+str(page))
			except:
				parse=''
				s[0][0]=True
				print '\nError open url'
			else:parse=link.read()
			urls,i='',0
			result=re.finditer(r'<span id\=\".+\" class\=\"thumb\"\>\<a id\=\".+\>\<img src\=\".+".+\"\/\>\<\/a\>\<\/span\>',parse)
			for res in result:
				urls+=res.group().split('img src="')[1].split('"')[0].split('?')[0].replace('thumbs','images').replace('thumbnail_','')+'\n'
				i+=1
				g[0][0]+=1
				if g[0][0]==limit:break
			if i<25:s[0][0]=True
			if g[0][0]<=limit:
				file=open('url.gelbooru','a')
				file.write(urls)
				file.close()
			else:g[0][0]-=25
			t[0][0]+=1
			print '\nProcess end: Gelbooru.com '+str(page)
		file=open('url.gelbooru','w')
		file.close()
		limit_page,i,stop=limit/25+1,0,[[False]]
		treads=[[3]]
		grabbed=[[0]]
		for i in range(limit_page):
			tread=threading.Thread(target=get25,args=(i*25,tag,limit,stop,treads,grabbed))
			tread.daemon=False
			tread.start()
			treads[0][0]-=1
			time.sleep(0.5)
			while treads[0][0]==0:time.sleep(3)
			if stop==True:
				print 'Breaked'
				break
		while treads[0][0]!=3:time.sleep(3)
		print '\nGelbooru.com grabbed: '+str(grabbed[0][0])+' images'	
		if grabbed[0][0]!=0:
			window.ui.PB_gelbooru.setMaximum(grabbed[0][0])
			self.download('url.gelbooru',window.ui.PB_gelbooru)
	def parse3(self,limit,tag):#animemahou.com
		print 'animemahou.com'
class Main(QtGui.QMainWindow):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui=MainWindow.Ui_MainWindow()
		self.ui.setupUi(self)

		f = open("settings.ini",'r')
		path = f.readline().split("path=")[1].rstrip()
		tags = f.readline().split("tags=")[1].rstrip()
		limits = f.readline().split("limits=")[1].rstrip()
		f.close()
		self.ui.path_line.setText(path)
		self.ui.tage_line.setText(tags)
		self.ui.num_line.setText(limits)
		QtCore.QObject.connect(self.ui.fileDialogBtn,QtCore.SIGNAL('clicked()'),self.fileDialog)
		QtCore.QObject.connect(self.ui.downloadBtn,QtCore.SIGNAL('clicked()'),self.get)
		self.ui.CB_animemahou.setEnabled(False)
	def fileDialog(self):
		fd=QtGui.QFileDialog(self)
		self.ui.path_line.setText(fd.getExistingDirectory())
	def get(self):
		ProgressBar=[self.ui.PB_animemahou,
				self.ui.PB_behomini,
				self.ui.PB_chan,
				self.ui.PB_danboru,
				self.ui.PB_gelbooru,
				self.ui.PB_genso,
				self.ui.PB_idol,
				self.ui.PB_konachan,
				self.ui.PB_nekobooru,
				self.ui.PB_oreno
				]
		for i in ProgressBar:i.reset()
		parse,board=Parser(),[]
		self.ui.downloadBtn.setEnabled(False)
		CheckBox=[self.ui.CB_animemahou,
				self.ui.CB_behomini,
				self.ui.CB_chan,
				self.ui.CB_danboru,
				self.ui.CB_gelbooru,
				self.ui.CB_genso,
				self.ui.CB_idol,
				self.ui.CB_konachan,
				self.ui.CB_nekobooru,
				self.ui.CB_oreno
				]
		for i in CheckBox:			
			if i.isChecked()==True:board.append(str(i.text()))
		f1 = open("settings.ini",'w')
		l = []
		l.append("path="+self.ui.path_line.text()+"\n")
		l.append("tags="+self.ui.tage_line.text()+"\n")
		l.append("limits="+self.ui.num_line.text())
		f1.writelines(l)
		f1.close()
		parse.startParser(board)
def main():
	window.show()
	sys.exit(app.exec_())
if __name__=="__main__":
	app,window=QtGui.QApplication(sys.argv),Main()
	main()