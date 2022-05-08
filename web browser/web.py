from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtGui import QIcon
import qrc_resources
import sys
import os

#window on which all is going to go aka climax
class MainWindow(QMainWindow):
    #constructor man
    def __init__(self,  *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        #tab widget
        self.tabs = QTabWidget()

        #turning doc mode true
        self.tabs.setDocumentMode(True)

        #action(man) when double clicked
        self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)

        #tab changed action
        self.tabs.currentChanged.connect(self.current_tab_changed)

        #tabs closeable?
        self.tabs.setTabsClosable(True)

        #tab close req
        self.tabs.tabCloseRequested.connect(self.close_current_tab)

        #setting tab as central widget
        self.setCentralWidget(self.tabs)

        #makin status bar (cus why not!)
        self.status = QStatusBar()

        #status bar neds to be in main window aint it?
        self.setStatusBar(self.status)

        #tb for nav
        navtb = QToolBar("Navigation")

        #ugh tb also needs to be in main window
        self.addToolBar(navtb)

        #back action
        back_btn = QAction(QIcon(":backward.png"), "Back", self)

        #status tip aka tool tip
        back_btn.setStatusTip("Back to previous page")

        #action to back btn
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())

        #adding this to nav tb
        navtb.addAction(back_btn)

        #addin next btn (this gets boring now)
        #next action
        next_btn = QAction(QIcon(":forward.png"), "Next", self)

        #status tip aka tool tip
        next_btn.setStatusTip("Forward to next page")

        #action to next btn
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().next())

        #adding this to nav tb
        navtb.addAction(next_btn)

        #also adding reload btn
        reload_btn = QAction(QIcon(":refresh.png"), 'Reload', self)
        reload_btn.setStatusTip('Reload the current page')
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

        #also adding home button
        home_btn = QAction(QIcon(":home.png"), 'Home', self)
        home_btn.setStatusTip('Go to Home Tab')
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        #adding seperator (intresting!)
        navtb.addSeparator()
        #welp nvm

        #adding a text box aka line widget for url
        self.urlbar = QLineEdit()

        #adding action wen return key is pressed
        self.urlbar.returnPressed.connect(self.navigate_to_url)

        #addin it to tb
        navtb.addWidget(self.urlbar)

        #ALSO adding stop btn *why now?* {cuz it should appear at last}
        stop_btn = QAction(QIcon(":cancel.png"), 'Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        #init the first tab 
        self.add_new_tab(QUrl('https://www.google.co.in'), 'Homepage')
		#showing all contents
        self.show()

        #set window title
        self.setWindowTitle('PyWeb')


    def add_new_tab(self, qurl = None, label ='Blank'):

    	#so what if url is blank?
    	if qurl is None:
    		#add default url
    		qurl = QUrl('https://www.google.co.in/')

    	#making QtWebEngineView obj
    	browser = QWebEngineView()

    	#setting url to browser
    	browser.setUrl(qurl)

    	#setting tab index
    	g = self.tabs.addTab(browser, label)
    	self.tabs.setCurrentIndex(g)

    	#adding action when url is changed
    	browser.urlChanged.connect(lambda qurl, browser = browser:
		    self.update_urlbar(qurl, browser))

    	browser.loadFinished.connect(lambda _, i = g, browser = browser:
		    self.tabs.setTabText(i, browser.page().title()))
	
	#when double click presssed on tab
    def tab_open_doubleclick(self, g):
 
        # checking index i.e
        # No tab under the click
        if g == -1:
            # creating a new tab
            self.add_new_tab()

	#when tab is changed
    def current_tab_changed(self, g):
 
        #get the url
        qurl = self.tabs.currentWidget().url()
 
        #update the url
        self.update_urlbar(qurl, self.tabs.currentWidget())
 
        #update the title
        self.update_title(self.tabs.currentWidget())

	#wen tab is closed
    def close_current_tab(self, g):
 
        #if there is only one tab
        if self.tabs.count() < 2:
            #do nothing
            return
 
        #else remove the tab
        self.tabs.removeTab(g)

    def update_title(self, browser):
 		
        if browser != self.tabs.currentWidget():
			#do nothin
            return

        title = self.tabs.currentWidget().page().title()

		#set window title
        self.setWindowTitle('% s - PyWeb' % title)

	#go home!
    def navigate_home(self):
        self.tabs.currentWidget().setUrl(QUrl('https://www.google.co.in/'))

	#nav to url
    def navigate_to_url(self):
		#get box text
        q = QUrl(self.urlbar.text())

		#if scheme is none
        if q.scheme() == "":
			#set scheme
            q.setScheme('https')

		#set url
        self.tabs.currentWidget().setUrl(q)

    def update_urlbar(self, q, browser = None):

		#if sig non ign
        if browser != self.tabs.currentWidget():
            return

		#set text to url
        self.urlbar.setText(q.toString())
		#set cursor position
        self.urlbar.setCursorPosition(0)

#making all this into a PyQt5 application
app = QApplication(sys.argv)
app.setStyle('Breeze')

#setting name
app.setApplicationName("PyWeb")

#creating mainwindow obj
window = MainWindow()

#loop this all
app.exec_()



