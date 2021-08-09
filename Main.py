import pandas as pd
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from plotter import Ui_Plotter
from connection import Login


     
class Ui_MainWindow(object):  
    def open_window(self,d1,d2):
        self.window=QtWidgets.QMainWindow()
        self.pt= Ui_Plotter()
        self.pt.setupUi(self.window,d1,d2,self.chart_type.currentText())
        self.window.show()
    def setupUi(self, MainWindow,con):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 750)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DB_list = QtWidgets.QComboBox(self.centralwidget)
        self.DB_list.setGeometry(QtCore.QRect(21, 15, 180, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DB_list.sizePolicy().hasHeightForWidth())
        self.DB_list.setSizePolicy(sizePolicy)
        self.DB_list.setMinimumSize(QtCore.QSize(180, 26))
        self.DB_list.setMaximumSize(QtCore.QSize(180, 26))
        self.DB_list.setAccessibleName("")
        self.DB_list.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.DB_list.setObjectName("DB_list")
        self.Interest_list = QtWidgets.QComboBox(self.centralwidget)
        self.Interest_list.setGeometry(QtCore.QRect(21, 75, 180, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Interest_list.sizePolicy().hasHeightForWidth())
        self.Interest_list.setSizePolicy(sizePolicy)
        self.Interest_list.setMinimumSize(QtCore.QSize(180, 26))
        self.Interest_list.setMaximumSize(QtCore.QSize(180, 26))
        self.Interest_list.setAccessibleName("")
        self.Interest_list.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.Interest_list.setObjectName("Interest_list")
        self.related_list = QtWidgets.QComboBox(self.centralwidget)
        self.related_list.setGeometry(QtCore.QRect(21, 183, 180, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.related_list.sizePolicy().hasHeightForWidth())
        self.related_list.setSizePolicy(sizePolicy)
        self.related_list.setMinimumSize(QtCore.QSize(180, 26))
        self.related_list.setMaximumSize(QtCore.QSize(180, 26))
        self.related_list.setAccessibleName("")
        self.related_list.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.related_list.setObjectName("related_list")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(21, 55, 180, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(21, 164, 180, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(21, 279, 180, 16))
        self.label_3.setObjectName("label_3")
        self.Analysis_type = QtWidgets.QComboBox(self.centralwidget)
        self.Analysis_type.setGeometry(QtCore.QRect(21, 297, 180, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Analysis_type.sizePolicy().hasHeightForWidth())
        self.Analysis_type.setSizePolicy(sizePolicy)
        self.Analysis_type.setAccessibleName("")
        self.Analysis_type.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.Analysis_type.setObjectName("Analysis_type")
        self.Analysis_type.addItem("")
        self.Analysis_type.addItem("")
        self.Analysis_type.addItem("")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(105, 215, 95, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        self.label_8.setObjectName("label_8") 
        self.sorting_related = QtWidgets.QComboBox(self.centralwidget)
        self.sorting_related.setGeometry(QtCore.QRect(105, 235, 95, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sorting_related.sizePolicy().hasHeightForWidth())
        self.sorting_related.setSizePolicy(sizePolicy)
        self.sorting_related.setAccessibleName("")
        self.sorting_related.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.sorting_related.setObjectName("sorting_related")
        self.sorting_related.addItem("")
        self.sorting_related.addItem("")
        self.sorting_related.addItem("")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(21, 106, 180, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        self.label_9.setObjectName("label_9") 
        self.sorting_interest = QtWidgets.QComboBox(self.centralwidget)
        self.sorting_interest.setGeometry(QtCore.QRect(21, 123, 180, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sorting_interest.sizePolicy().hasHeightForWidth())
        self.sorting_interest.setSizePolicy(sizePolicy)
        self.sorting_interest.setAccessibleName("")
        self.sorting_interest.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.sorting_interest.setObjectName("sorting_interest")
        self.sorting_interest.addItem("")
        self.sorting_interest.addItem("")
        self.sorting_interest.addItem("")
        self.run_bt = QtWidgets.QPushButton(self.centralwidget)
        self.run_bt.setGeometry(QtCore.QRect(21, 485, 180, 50))
        self.run_bt.setMinimumSize(QtCore.QSize(180, 40))
        self.run_bt.setMaximumSize(QtCore.QSize(180, 40))
        self.run_bt.setObjectName("run_bt")
        self.Save = QtWidgets.QPushButton(self.centralwidget)
        self.Save.setGeometry(QtCore.QRect(21, 525, 180, 50))
        self.Save.setMinimumSize(QtCore.QSize(180, 40))
        self.Save.setMaximumSize(QtCore.QSize(180, 40))
        self.Save.setObjectName("Save Table")
        self.counter=0
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 10, 581, 531))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setTabletTracking(True)
        self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 809, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionDB1 = QtWidgets.QAction(MainWindow)
        self.actionDB1.setObjectName("actionDB1")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(21, 340, 180, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QtCore.QSize(180, 16))
        self.label_4.setMaximumSize(QtCore.QSize(180, 16))
        self.label_4.setObjectName("label_4")
        self.chart_type = QtWidgets.QComboBox(self.centralwidget)
        self.chart_type.setGeometry(QtCore.QRect(21, 358, 180, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.chart_type.sizePolicy().hasHeightForWidth())
        self.chart_type.setSizePolicy(sizePolicy)
        self.chart_type.setMinimumSize(QtCore.QSize(180, 26))
        self.chart_type.setMaximumSize(QtCore.QSize(121, 26))
        self.chart_type.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.chart_type.setObjectName("chart_type")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(21, 570, 180, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.notes = QtWidgets.QLabel(self.centralwidget)
        self.notes.setGeometry(QtCore.QRect(11, 590, 780, 150))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes.sizePolicy().hasHeightForWidth())
        self.notes.setSizePolicy(sizePolicy)
        self.notes.setFrameShape(QtWidgets.QFrame.Panel)
        self.notes.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.notes.setLineWidth(1)
        self.notes.setMidLineWidth(0)
        self.notes.setText("")
        self.notes.setTextFormat(QtCore.Qt.AutoText)
        self.notes.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.notes.setObjectName("notes")
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        self.notes.setWordWrap(True)
        self.label_5.setFont(font)
        self.aggrigation = QtWidgets.QComboBox(self.centralwidget)
        self.aggrigation.setGeometry(QtCore.QRect(21, 235, 80, 26))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aggrigation.sizePolicy().hasHeightForWidth())
        self.aggrigation.setSizePolicy(sizePolicy)
        self.aggrigation.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToMinimumContentsLengthWithIcon)
        self.aggrigation.setObjectName("aggrigation")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(21, 216, 180, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(21, 340, 180, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(21, 50, 180, 3))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(21, 157, 180, 3))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(21, 270, 180, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(21, 335, 180, 3))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.listView = QtWidgets.QListWidget(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(21, 358, 180, 121))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QtWidgets.QAbstractItemView.MultiSelection)
        self.listView.setSelectionRectVisible(True)
        self.listView.setObjectName("listView")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.connection=con
        self.databases= pd.read_sql_query("select schema_name as database_name from information_schema.schemata", self.connection)
        self.databases=[self.databases.database_name.iloc[i] for i in range(len(self.databases)) if self.databases.database_name.iloc[i] not in ['mysql','information_schema','performance_schema','sys']]
        self.label_4.hide()
        self.chart_type.hide()
        self.vars=pd.DataFrame(data=None,columns=['variables','tables'])
        self.DB_list.currentIndexChanged.connect(self.get_interests)
        for db in self.databases:
            self.DB_list.addItem(db)
        self.DB_list.setCurrentIndex(0)
        self.current_db=self.DB_list.currentText()
        self.tables=pd.read_sql_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='"+self.current_db+"'", self.connection)
        self.get_interests(0)
        self.get_related_vars(0)
        self.run_bt.clicked.connect(self.analysis)
        self.supported_charts=['Bar Chart','Line Chart','Scatter Plot','Pie Chart','Histogram']
        for chart in self.supported_charts:
            self.chart_type.addItem(chart)
        self.chart_type.currentIndexChanged.connect(self.special_actions)
        self.aggrigation_set=['None','Sum','Count','Average','Min','Max']
        for s in self.aggrigation_set:
             self.aggrigation.addItem(s)
        self.aggrigation.currentIndexChanged.connect(self.special_actions)        
        self.Analysis_type.currentIndexChanged.connect(self.special_actions)
        self.Interest_list.currentIndexChanged.connect(self.interest_changed)
        self.related_list.currentIndexChanged.connect(self.additionals)
        self.listView.itemActivated.connect(self.get_add_data)
        self.notes.setText('Welcome to Rapid Reports. \nHow to Use: \n- Select needed Database \n- Select your interest variable and other variable (aggrigate if needed) \n- Select type of analysis (table, chart, descriptives) \n- Add any additional data by double click on each item (works with table view only) \n- Click Run Reports \nEnjoy! ')
        self.Save.clicked.connect(self.save_table)
        self.data_table=pd.DataFrame()
        
    def save_table(self,index):
        if  self.data_table.shape[0]:
            file = "C:/Output/"
            file_name="Table_"+str(self.counter)+'.xlsx'
            if not os.path.exists(file):
                os.makedirs(file)
            self.data_table.to_excel(file+file_name)  
            self.counter+=1
            msg= QtWidgets.QMessageBox()
            msg.setWindowTitle('Notification')
            msg.setText('Data Exported to: \n'+file+file_name)
            msg.setIcon(QtWidgets.QMessageBox.Information)
            x=msg.exec_()
        else:
            msg= QtWidgets.QMessageBox()
            msg.setWindowTitle('Error Message')
            msg.setText('No data to export, Press Run Report first')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            x=msg.exec_()

    def interest_changed(self,index):
        self.current_interest=self.Interest_list.currentText()
        self.current_related=self.related_list.currentText()
        self.get_related_vars(0)
        self.additionals(0)

    def additionals(self,index):
        self.current_interest=self.Interest_list.currentText()
        self.current_related=self.related_list.currentText()
        if index == -1:
            self.get_related_vars(0)
        self.current_interest=self.Interest_list.currentText()
        self.current_related=self.related_list.currentText()     
        self.t1=list(self.vars[self.vars['variables']== self.Interest_list.currentText()]['tables'])[0]
        self.t2=list(self.vars[self.vars['variables']== self.related_list.currentText()]['tables'])[0]
        self.c1=list(pd.read_sql_query("SHOW COLUMNS FROM "+self.current_db+"."+self.t1,self.connection)['Field'])
        self.c2=list(pd.read_sql_query("SHOW COLUMNS FROM "+self.current_db+"."+self.t2,self.connection)['Field'])
        c=[]
        c.extend(self.c1)
        c.extend(self.c2)
        c=set(c)
        if self.current_interest ==self.current_related:
            c.remove(self.current_interest)
        else:
            c.remove(self.current_interest)
            c.remove(self.current_related)
        self.listView.clear()
        for col in c:            
            self.listView.addItem(col)
        
    def get_add_data (self):
        self.current_interest=self.Interest_list.currentText()
        self.current_related=self.related_list.currentText()
        self.get_data(self.current_interest,self.current_related)
        t1=list(self.vars[self.vars['variables']== self.current_interest]['tables'])[0]
        t2=list(self.vars[self.vars['variables']== self.current_related]['tables'])[0]
        c1=list(pd.read_sql_query("SHOW COLUMNS FROM "+self.current_db+"."+t1,self.connection)['Field'])
        c2=list(pd.read_sql_query("SHOW COLUMNS FROM "+self.current_db+"."+t2,self.connection)['Field'])
        buffer=self.listView.selectedItems()
        item_data=[]
        for item in buffer:
            v=item.text()
            if v in c1: item_data.append([v,t1])
            elif v in c2: item_data.append([v,t2])
            else: item_data.append(['No Data','No Data'])
        item_data.append([self.current_interest,t1])
        item_data.append([self.current_related,t2])
        table_map=pd.DataFrame(data=item_data ,columns=['variable','table'])
        var1=",".join(table_map[table_map['table']==t1]['variable'])
        var2=",".join(table_map[table_map['table']==t2]['variable'])
        data1=pd.read_sql_query("SELECT "+var1+" FROM "+self.current_db+"."+t1,self.connection)
        data2=pd.read_sql_query("SELECT "+var2+" FROM "+self.current_db+"."+t2,self.connection)
        data=pd.concat([data1,data2],axis=1)
        data=data.loc[:,~data.columns.duplicated()]
        cols=list(data.columns)
        if self.current_interest ==self.current_related:
            cols.remove(self.current_interest)
        else:
            cols.remove(self.current_interest)
            cols.remove(self.current_related)
        new_cols=[self.current_interest,self.current_related]
        new_cols.extend(cols)
        self.data_table = data[new_cols].drop_duplicates()
        self.sorter()
        self.load_data(self.data_table)
        
    def get_related_vars(self, index):
        interest=self.Interest_list.currentText()
        if len(self.Interest_list.currentText()): interest=self.Interest_list.currentText()
        interest=self.vars[self.vars['variables']==self.Interest_list.currentText()]
        self.related_vars=self.vars.drop(interest.index)
        self.related_list.clear()
        for rv in list(self.related_vars['variables']):
            self.related_list.addItem(rv)
        self.current_related=self.related_list.currentText()
        self.related_list.setCurrentIndex(0) 

    def get_interests (self, index):
        self.Interest_list.blockSignals(True)
        self.related_list.blockSignals(True)
        self.vars=pd.DataFrame(data=None,columns=['variables','tables'])
        self.current_db=self.DB_list.currentText()
        self.tables=pd.read_sql_query("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='"+self.current_db+"'", self.connection)
        col_tables=[]
        cols=[]
        for table in self.tables.iloc[:,0]:
            temp=pd.read_sql_query("SELECT * FROM "+self.DB_list.currentText()+"."+table+" LIMIT 1", self.connection).columns
            cols.extend(temp)
            for i in range(len(temp)):
                col_tables.append(table)
        self.vars['variables']=cols
        self.vars['tables']=col_tables
        self.vars.drop_duplicates(subset=['variables'],inplace=True)
        self.Interest_list.clear()        
        interests=list(self.vars['variables'])
        for col in interests:
            self.Interest_list.addItem(col)
        self.Interest_list.setCurrentIndex(0)
        self.get_related_vars(0)
        self.additionals(0)
        self.Interest_list.blockSignals(False)
        self.related_list.blockSignals(False)
        self.current_interest=self.Interest_list.currentText()
        self.current_related=self.related_list.currentText()
 
    def sorter(self):
        sort_dic={'Ascending':True,'Descending':False,'None':''}
        int_flag=sort_dic[self.sorting_interest.currentText()]
        rel_flag=sort_dic[self.sorting_related.currentText()]
        if self.sorting_interest.currentText() != 'None': 
            self.data_table=self.data_table.sort_values(by=[self.current_interest],ascending=int_flag)
        if self.sorting_related.currentText() != 'None': 
            self.data_table=self.data_table.sort_values(by=[self.current_related],ascending=rel_flag)     
            
    def load_data(self, Data):
        self.tableWidget.setRowCount(Data.shape[0])
        self.tableWidget.setColumnCount(Data.shape[1])
        self.tableWidget.setHorizontalHeaderLabels(Data.columns)
        for col in range(Data.shape[1]):
            for row in range(Data.shape[0]):
                self.tableWidget.setItem(row,col,QtWidgets.QTableWidgetItem(str(Data.iloc[row,col])))
    
    def find_related_tables(self,t1,t2):
        t1_k=pd.read_sql_query(("SHOW KEYS FROM "+self.current_db+"."+t1), self.connection)
        t1_k=t1_k.loc[:,['Column_name']].rename(columns={'Column_name':'key'})
        t2_k=pd.read_sql_query(("SHOW KEYS FROM "+self.current_db+"."+t2), self.connection)
        t2_k=t2_k.loc[:,['Column_name']].rename(columns={'Column_name':'key'})
        key_table=pd.DataFrame(data=None, columns=['key','table'])
        for table in self.tables.iloc[:,0]:
             t=pd.read_sql_query(("SHOW KEYS FROM "+self.current_db+"."+table), self.connection)
             t=t.loc[:,['Column_name','Table']].rename(columns={'Column_name':'key','Table':'table'})
             key_table=key_table.append(t,ignore_index=True)
        t1_related_tables=key_table[key_table['key'].isin(t1_k['key'])]
        t2_related_tables=key_table[key_table['key'].isin(t2_k['key'])]
        t1_related_tables=t1_related_tables[t1_related_tables['table']!=t1].drop_duplicates(subset=['key'])
        t2_related_tables=t2_related_tables[t2_related_tables['table']!=t2].drop_duplicates(subset=['key'])
        matching_table= pd.DataFrame(data=None,columns=['key','table'])
        matching_table=matching_table.append(t1_related_tables[t1_related_tables['table'].isin(t2_related_tables['table'])])
        matching_table=matching_table.append(t2_related_tables[t2_related_tables['table'].isin(t1_related_tables['table'])])
        if matching_table.shape[0]==0:
            msg= QtWidgets.QMessageBox()
            msg.setWindowTitle('Error Message')
            msg.setText('No relationship found between variables! \n Please choose another combination')
            msg.setIcon(QtWidgets.QMessageBox.Information)
            x=msg.exec_()
            return '','',''
        else: 
            return matching_table.drop_duplicates()
 
    def get_data(self,x,y):
        t1=list(self.vars[self.vars['variables']==x]['tables'])[0]
        pk1=list(pd.read_sql_query(("SHOW KEYS FROM "+self.DB_list.currentText()+"."+t1+" WHERE Key_name = 'PRIMARY'"), self.connection)['Column_name'])
        fk1=list(pd.read_sql_query("SHOW KEYS FROM "+self.DB_list.currentText()+"."+t1+" WHERE Key_name <> 'PRIMARY'", self.connection)['Column_name'])
        t2=list(self.vars[self.vars['variables']==y]['tables'])[0]
        pk2=list(pd.read_sql_query("SHOW KEYS FROM "+self.DB_list.currentText()+"."+t2+" WHERE Key_name = 'PRIMARY'", self.connection)['Column_name'])
        fk2=list(pd.read_sql_query("SHOW KEYS FROM "+self.DB_list.currentText()+"."+t2+" WHERE Key_name <> 'PRIMARY'", self.connection)['Column_name'])
        v1=x
        v2=y
        if t1==t2:
            self.data_table=pd.read_sql_query("SELECT "+v1+","+v2+" FROM "+self.current_db+"."+t1+"",self.connection).drop_duplicates()
        elif v1 in list(self.vars[self.vars['tables']==t2]['variables']):
            self.data_table=pd.read_sql_query("SELECT "+v1+","+v2+" FROM "+self.current_db+"."+t2+"",self.connection).drop_duplicates()
        elif (pk1[0] in fk2) or (pk1[0]==pk2[0]): 
            self.data_table=pd.read_sql_query("SELECT "+t1+"."+v1+","+t2+"."+v2+" FROM "+self.current_db+"."+t1+","+self.current_db+"."+t2+" WHERE "+t1+"."+pk1[0]+"="+t2+"."+pk1[0],self.connection).drop_duplicates()
        else:
            #if fk1 is empty or not found in direct relationship
            flag=0
            if len(fk1):
                for fk in fk1:
                    if flag==0:    
                        if (fk in fk2)or(fk in pk2):
                            self.data_table=pd.read_sql_query("SELECT "+t1+"."+v1+","+t2+"."+v2+" FROM "+self.current_db+"."+t1+","+self.current_db+"."+t2+" WHERE "+t1+"."+fk+"="+t2+"."+fk,self.connection).drop_duplicates()
                            flag=1
                        else:
                            t3_d=self.find_related_tables(t1,t2)
                            if t3_d.shape[0]<2: 
                                print('no k in r1')
                                pass
                            else: 
                                t3=t3_d.iloc[0,1]
                                t1_t3_k=t3_d.iloc[0,0]
                                t2_t3_k=t3_d.iloc[1,0]
                                self.data_table=pd.read_sql_query("SELECT "+t1+"."+v1+","+t2+"."+v2+" FROM "+self.current_db+"."+t1+" , "+self.current_db+"."+t2+" , "+self.current_db+"."+t3
                                                                  +" WHERE "+self.current_db+"."+t1+"."+t1_t3_k+"="+self.current_db+"."+t3+"."+t1_t3_k
                                                                  +" AND "+ self.current_db+"."+t3+"."+t2_t3_k+"="+self.current_db+"."+t2+"."+t2_t3_k , self.connection ).drop_duplicates()
                                flag=1                                
            else: 
                t3_d=self.find_related_tables(t1,t2)
                if t3_d.shape[0]<2: 
                    print('no k in r1')
                    pass
                else: 
                    t3=t3_d.iloc[0,1]
                    t1_t3_k=t3_d.iloc[0,0]
                    t2_t3_k=t3_d.iloc[1,0]
                    self.data_table=pd.read_sql_query("SELECT "+t1+"."+v1+","+t2+"."+v2+" FROM "+self.current_db+"."+t1+" , "+self.current_db+"."+t2+" , "+self.current_db+"."+t3
                                                      +" WHERE "+self.current_db+"."+t1+"."+t1_t3_k+"="+self.current_db+"."+t3+"."+t1_t3_k
                                                      +" AND "+ self.current_db+"."+t3+"."+t2_t3_k+"="+self.current_db+"."+t2+"."+t2_t3_k , self.connection ).drop_duplicates()

    def table_view (self,x,y):
        for i in reversed(range(self.gridLayout.count())): 
            self.gridLayout.itemAt(i).widget().deleteLater()
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        if len(self.listView.selectedIndexes())>0:
            self.sorter()
            self.load_data(self.data_table)
        elif self.aggrigation.currentText()=='None':
            self.get_data(x,y)
            self.sorter()
            self.load_data(self.data_table)
        else: 
            self.agg_functions(x,y)
            self.sorter()
            self.load_data(self.data_table)

    def special_actions(self,index):
        self.run_bt.move(21, 485) #move back button to its place
        self.Save.move(21,525)
        self.label_4.hide()
        self.line_4.show()
        self.chart_type.hide()
        self.related_list.setEnabled(True) # Enabling related
        self.aggrigation.setEnabled(True) # Enabling aggrigation
        self.notes.setText('')
        self.listView.show()
        self.label_7.show()
        self.sorting_interest.setEnabled(True)
        self.sorting_related.setEnabled(True)
        self.Save.show()
        if self.Analysis_type.currentText()=='Descriptives':
            self.run_bt.move(21,340)
            self.Save.move(21,380)
            self.aggrigation.setEnabled(False) # disabling aggrigation
            self.related_list.setEnabled(False) # disabling related        
            self.label_7.hide()
            self.line_4.hide()
            self.listView.hide()
            self.sorting_interest.setEnabled(False)
            self.sorting_related.setEnabled(False)
            self.notes.setText('Descriptives are more efficient for numerical interests like prices. \nThis tool uses only one variable!')
        elif self.Analysis_type.currentText()=='Chart':
            self.run_bt.move(21,400)
            self.Save.move(21,440)
            self.label_7.hide()
            self.line_4.hide()
            self.listView.hide()
            self.label_4.show()
            self.chart_type.show()
            if self.chart_type.currentText() == 'Histogram':
                self.related_list.setEnabled(False) # disabling related        
                self.aggrigation.setEnabled(False)
                self.notes.setText('Histogram is used to present distribution and relationships of a single variable over a set of categories like distribution of grades on a school exam . \n \nThis tool uses only one variable!')
            elif self.chart_type.currentText() =='Bar Chart':
                self.notes.setText('Bar chart compare values for different categories or compare value changes over a period of time for a single category. \nUse if the number of categories is quite small,or if one of your data dimensions is time. \n \nx-axis: interest , y-axis: other variable')
            elif self.chart_type.currentText() == 'Line Chart':
                self.notes.setText('Line chart best continuous scales like sales per day. Use line chart when you have a continuous variable.  \n \nx-axis: interest , y-axis: other variable')                
            elif self.chart_type.currentText() == 'Scatter Plot':
                self.notes.setText("Scatter charts are primarily used for correlation and distribution analysis. Good for showing the relationship between two different variables where one correlates to another (or doesn’t). Don't use aggrigations or variables with categories. \n \nx-axis: interest , y-axis: other variable")
            elif self.chart_type.currentText() == 'Pie Chart':
                self.notes.setText("Pie Chart is useful for comparing categories. A pie chart typically represents numbers in percentages, used to visualize a part to whole relationship or a composition. use aggrigations like count of sold units per sales point.  \n \nx-axis: interest , y-axis: other variable")
        elif  self.Analysis_type.currentText()=='Table (Report)':
            if self.aggrigation.currentText() != 'None':
                self.listView.hide()
                self.label_7.hide()
                self.run_bt.move(21,340)
                self.Save.move(21,380)
                self.notes.setText('In Aggrigations, additional data is disabled due to the nature of the output.')
            else:
                self.run_bt.move(21, 485)
                self.Save.move(21,525)
                self.label_7.show()
                self.listView.show()            
    
    def best_chart(self,x,y):
        if self.aggrigation.currentText()=='None':
            self.get_data(x,y)
            self.sorter()
            self.load_data(self.data_table)
        else: 
            self.agg_functions(x,y)
            self.sorter()
            self.load_data(self.data_table)        
        self.open_window(list(self.data_table.iloc[:,0]),list(self.data_table.iloc[:,1]))
        
    def descriptive (self,x):
        for i in reversed(range(self.gridLayout.count())): 
            self.gridLayout.itemAt(i).widget().deleteLater()
        self.tableWidget = QtWidgets.QTableWidget(self.gridLayoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        t=list(self.vars[self.vars['variables']==x]['tables'])[0]
        data=pd.read_sql_query("SELECT "+x+" FROM "+self.current_db+"."+t,self.connection)
        self.data_table=data.describe().reset_index()
        self.load_data(self.data_table)           
        
    def analysis (self, index):
        self.current_interest=self.Interest_list.currentText()
        self.current_related=self.related_list.currentText()
        if self.Analysis_type.currentText()=='Table (Report)':
            self.table_view(self.current_interest,self.current_related)
        elif self.Analysis_type.currentText()=='Chart':
            self.best_chart(self.current_interest,self.current_related)
        elif self.Analysis_type.currentText()=='Descriptives':
            self.descriptive(self.current_interest)
    
    def agg_functions (self, interest, related):
        self.get_data(interest,related)
        if self.aggrigation.currentText() == 'Sum':
            agg_data=self.data_table.groupby([interest]).sum()
        elif self.aggrigation.currentText() == 'Count':
            agg_data=self.data_table.groupby([interest]).count()
        elif self.aggrigation.currentText() == 'Average':
            agg_data=self.data_table.groupby([interest]).mean().round(4)
        elif self.aggrigation.currentText() == 'Min':
            agg_data=self.data_table.groupby([interest]).min()
        elif self.aggrigation.currentText() == 'Max':
            agg_data=self.data_table.groupby([interest]).max()
        self.data_table=agg_data.reset_index()
       
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rapid Reports"))
        self.DB_list.setCurrentText(_translate("MainWindow", "Select Table"))
        self.DB_list.setPlaceholderText(_translate("MainWindow", "Select Table"))
        self.Interest_list.setCurrentText(_translate("MainWindow", "Select Interest"))
        self.Interest_list.setPlaceholderText(_translate("MainWindow", "Select Interest"))
        self.related_list.setCurrentText(_translate("MainWindow", "Select Info"))
        self.related_list.setPlaceholderText(_translate("MainWindow", "Select Info"))
        self.label.setText(_translate("MainWindow", "Interest"))
        self.label_2.setText(_translate("MainWindow", "What to know about Interest"))
        self.label_3.setText(_translate("MainWindow", "Type Of Analysis"))
        self.Analysis_type.setCurrentText(_translate("MainWindow", "Select Info"))
        self.Analysis_type.setPlaceholderText(_translate("MainWindow", "Select Info"))
        self.Analysis_type.setItemText(0, _translate("MainWindow", "Table (Report)"))
        self.Analysis_type.setItemText(1, _translate("MainWindow", "Chart"))
        self.Analysis_type.setItemText(2, _translate("MainWindow", "Descriptives"))
        self.run_bt.setText(_translate("MainWindow", "Run Report"))
        self.Save.setText(_translate("MainWindow", "Save Table"))
        self.actionDB1.setText(_translate("MainWindow", "DB1"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.label_4.setText(_translate("MainWindow", "Chart Type"))
        self.label_5.setText(_translate("MainWindow", "Tips:"))
        self.label_6.setText(_translate("MainWindow", "Aggrigation"))
        self.label_7.setText(_translate("MainWindow", "Additional Data"))
        self.label_8.setText(_translate("MainWindow", "Sort"))
        self.label_9.setText(_translate("MainWindow", "Sort"))
        self.tableWidget.setSortingEnabled(True)
        self.sorting_related.setCurrentText(_translate("MainWindow", "Select Info"))
        self.sorting_related.setPlaceholderText(_translate("MainWindow", "Select Info"))
        self.sorting_related.setItemText(0, _translate("MainWindow", "None"))
        self.sorting_related.setItemText(1, _translate("MainWindow", "Ascending"))
        self.sorting_related.setItemText(2, _translate("MainWindow", "Descending"))
        self.sorting_interest.setCurrentText(_translate("MainWindow", "Select Info"))
        self.sorting_interest.setPlaceholderText(_translate("MainWindow", "Select Info"))
        self.sorting_interest.setItemText(0, _translate("MainWindow", "None"))
        self.sorting_interest.setItemText(1, _translate("MainWindow", "Ascending"))
        self.sorting_interest.setItemText(2, _translate("MainWindow", "Descending"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    login= Login()
    
    if login.exec_() == QtWidgets.QDialog.Accepted:      
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_MainWindow()
        ui.setupUi(MainWindow,login.connection)
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        sys.exit()