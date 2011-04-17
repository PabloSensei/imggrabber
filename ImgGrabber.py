#coding: utf-8
import sys,urllib2,re,os,MainWindow,threading
from PyQt4 import QtCore, QtGui
class BoardParser():
	def get_urls(self):
		limit,tag,url=int(window.ui.LimitInput.text()),str(window.ui.TagInput.text()).replace(' ','_').replace('&','%26'),str(window.ui.Board.currentText())
		window.ui.statusbar.showMessage('Grabbing links')
		if url=='konachan.com'or url=='oreno.imouto.org'or url=='danbooru.donmai.us'or url=='behoimi.org'or url=='nekobooru.net'or url=='genso.ws':urls=self.parse_0(limit,url,tag)
		if url=='chan.sankakucomplex.com'or url=='idol.sankakucomplex.com':urls=self.parse_1(limit,url,tag)
		if url=='gelbooru.com':urls=self.parse_2(limit,tag)
		if url=='animemahou.com':urls=self.parse_3(limit,tag)
		window.ui.statusbar.showMessage('Download images')
		return urls 
	def parse_0(self,limit,url,tag):#konachan.com oreno.imouto.org danbooru.donmai.us behoimi.org nekobooru.net genso.ws
		global progress
		urls,page,i,limit_page='',1,0,limit/999+1
		while page<=limit_page:
			url=urllib2.urlopen('http://'+url+'/post?limit='+str(limit)+'&page='+str(page)+'&tags='+tag)
			parse=url.read()
			result=re.finditer(r'Post\.register\(\{.+\"file\_url\"\:\".+\".+\}\)',parse)
			for res in result:
				urls+=res.group().split('file_url":"')[1].split('"')[0]+'\n'
				progress+=1
				i+=1
				if i==limit:break
			if i<999:break
			page+=1
		return urls
	def parse_1(self,limit,url,tag):#chan.sankakucomplex.com idol.sankakucomplex.com
		urls,page,limit_page,i,i1='',1,limit/70+1,0,0
		while page<=limit_page:
			global progress
			url=urllib2.urlopen('http://'+url+'/post/index?limit=70&tags='+tag+'&page='+str(page))
			parse=url.read()
			result=re.finditer(r'Post\.register\(\{.+\}\)\;',parse)
			for res in result:
				i+=1
				if i<=4:continue
				urls+=res.group().split('file_url":"')[1].split('"')[0]+'\n'
				progress+=1
				i1+=1
				if i1==limit:break
			if i1<70:break
			page+=1
		return urls
	def parse_2(self,limit,tag):#gelbooru.com
		global progress
		urls,page,='',0
		while limit>0:
			i=0
			url=urllib2.urlopen('http://gelbooru.com/index.php?page=post&s=list&tags='+tag+'&pid='+str(page))			
			parse=url.read()
			result=re.finditer( r'<span id\=\".+\" class\=\"thumb\"\>\<a id\=\".+\>\<img src\=\".+".+\"\/\>\<\/a\>\<\/span\>',parse)
			for res in result:
				urls+=res.group().split('img src="')[1].split('"')[0].split('?')[0].replace('thumbs','images').replace('thumbnail_','')+'\n'
				progress+=1
				i+=1
				if i==limit:break
			if i<25:break
			page+=25
			limit-=25
		return urls
	def parse_3(self,limit,tag):#animemahou.com
		global progress
		urls,page,='',1
		while limit>0:
			i=0
			url=urllib2.urlopen('http://www.animemahou.com/post/'+str(page)+'?search='+tag)			
			parse=url.read()
			result=re.finditer( r'\<img onMouseover\=\'ddrivetip\(\".+\;.+\;.+\' alt\=\'.+\' title\=.+src\=\'.+\' class\=\'preview\'\/\>',parse)
			for res in result:
				if int(res.group().split('src=\'')[1].split('-')[0].split('/')[-1])<40660:urls+='http://www.jp-girls.org/_images/'+res.group().split('_thumbs/')[1].split('/')[0]+'.'+res.group().split('(')[1].split(')')[0].split('/')[4].split(' ')[1]+'/AnimeMahou-'+res.group().split('src=\'')[1].split('-')[0].split('/')[-1]+'.'+res.group().split('(')[1].split(')')[0].split('/')[4].split(' ')[1]+'\n'
				else:urls+='http://www.animemahou.com/_images/'+res.group().split('_thumbs/')[1].split('/')[0]+'.'+res.group().split('(')[1].split(')')[0].split('/')[4].split(' ')[1]+'/AnimeMahou-'+res.group().split('src=\'')[1].split('-')[0].split('/')[-1]+'.'+res.group().split('(')[1].split(')')[0].split('/')[4].split(' ')[1]+'\n'
				progress+=1
				i+=1
				if i==limit:break
			if i<20:break
			page+=1
			limit-=20
		return urls
class UrlFile():
	urls=BoardParser()
	def write_to_file_urls(self):
		file=open('url.txt','w')
		file.write(self.urls.get_urls())
		file.close()
	def get_file_urls(self):
		self.write_to_file_urls()
		self.file=open('url.txt','r')
		return self.file
class Path():
	def set_path(self):
		path=''
		if str(window.ui.PathEdit.text())!='':path=str(window.ui.PathEdit.text())+'/'
		if str(window.ui.TagInput.text())=='':path+='No_Tag/'
		else:path+=str(window.ui.TagInput.text())+'/'
		if os.access(path,os.F_OK)==False:os.makedirs(path)
		return path
class ImgSave():
	file,path=UrlFile(),Path()
	def run(self):
		path,file,value=self.path.set_path(),self.file.get_file_urls(),0
		window.ui.progressBar.setMaximum(progress)
		for url in file.readlines():
			img=urllib2.urlopen(url)
			img_name=path+img.geturl().replace('%20',' ').split('/')[-1]
			if os.access(img_name,os.F_OK)==True:continue
			img_file=open(img_name,'wb')
			img_file.write(img.read())
			img_file.close()
			value+=1
			window.ui.progressBar.setValue(value)
		file.close()	
		window.ui.statusbar.showMessage('Complete')
class Main(QtGui.QMainWindow):
	get=ImgSave()
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui=MainWindow.Ui_MainWindow()
		self.ui.setupUi(self)
		QtCore.QObject.connect(self.ui.Get,QtCore.SIGNAL('clicked()'),self.Get)
		QtCore.QObject.connect(self.ui.PathButton,QtCore.SIGNAL('clicked()'),self.file_dialog)
	def file_dialog(self):
		fd=QtGui.QFileDialog(self)
		self.ui.PathEdit.setText(fd.getExistingDirectory())
	def Get(self):
		def run():
			global progress
			progress=0
			window.ui.statusbar.clearMessage()
			self.ui.progressBar.reset()
			num=str(self.ui.LimitInput.text())
			if num=='' or int(num)<=0:self.ui.statusbar.showMessage('Ilegal limit',3000)
			else:self.get.run()
		tread=threading.Thread(target=run)
		tread.daemon=False
		tread.start()	
def main():
	window.show()
	sys.exit(app.exec_())
if __name__=="__main__":
	app,window,progress=QtGui.QApplication(sys.argv),Main(),0
	main()