import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class DataBaseManagement:
    def __init__(self):
        self.patientName = None

    def init(self, filename, server):
        import os
        if not os.path.exists(filename):
            self.db_connect(filename, server)
            self.db_create()
        else:
            self.db_connect(filename, server)

    def insertPatientDetails(self, model):
        patient_name = model.get_patient_name()
        patient_sex = model.get_patient_sex()
        patient_age = model.get_patient_age()
        patient_id = model.get_patient_id()

        query = QSqlQuery()
        query1 = QSqlQuery()

        query1.prepare("INSERT OR REPLACE INTO patient_master (patient_name, patient_age, "
                       "patient_sex, patient_id) "
                       "VALUES ( :patient_name, :patient_age, :patient_sex,"
                       " :patient_id)")

        query1.bindValue(":patient_name", patient_name)
        query1.bindValue(":patient_age", patient_sex)
        query1.bindValue(":patient_sex", patient_age)
        query1.bindValue(":patient_id", patient_id)

        if not query1.exec():
            qDebug() << "Error inserting data into table:\n" << query1.lastError()

        '''
        
          query.prepare("INSERT INTO patient_details (patient_skin_temp, air_temp, "
                      " patient_id) "
                      "VALUES ( :patient_skin_temp, :air_temp,"
                      " :patient_id)")

        query.bindValue(":patient_skin_temp", patient_name)
        query.bindValue(":air_temp", patient_sex)
        query.bindValue(":patient_id", patient_id)'''

        query.prepare(
            "INSERT INTO patient_details(patient_skin_temp, air_temp, patient_id)  SELECT * FROM ( SELECT '" + patient_name
            + "','" + patient_age
            + "', '" + patient_id + "' ) as temp  where exists  (Select patient_id from "
                                    "patient_master where patient_id='" + patient_id + "') LIMIT 1 ")
        '''print("INSERT INTO patient_details(patient_skin_temp, air_temp, patient_id)  SELECT * FROM ( SELECT '" + patient_name
            + "','" + patient_age
            + "', '" + patient_id + "' ) as temp  where not exists  (Select patient_id from "
                                    "patient_master where patient_id='" + patient_id + "') LIMIT 1 ")'''

        if not query.exec():
            qDebug() << "Error inserting data into table:\n" << query.lastError()

    def queryGeneralSettingsData(self, model):
        query = QSqlQuery()
        query.exec_("SELECT * FROM general_setting where id=1")
        while query.next():
            model.set_skin_temp(query.value('skin_set_temp'))
            model.set_air_temp(query.value('air_set_temp'))
            model.set_mute_flag(query.value('mute_flag'))

    def getPatientById(self, text, model):
        query = QSqlQuery()
        self.patientName = ""
        print("SELECT * FROM patient_master where patient_id=" + "'" + str(text) + "'")
        query.exec_("SELECT * FROM patient_master where patient_id=" + "'" + str(text) + "'")
        while query.next():
            self.patientName = query.value('patient_name')
        model.set_form_patient_name(self.patientName)


    def updateSkinTempValue(self, model):
        _skin_temp = model.get_skin_temp()
        query = QSqlQuery()
        query.exec_("UPDATE general_setting SET skin_set_temp ='" + str(_skin_temp) + "' WHERE id= 1")

    def updateAirTempValue(self, model):
        _air_temp = model.get_air_temp()
        query = QSqlQuery()
        query.exec_("UPDATE general_setting SET air_set_temp ='" + str(_air_temp) + "' WHERE id= 1")

    def updateMuteValue(self, model):
        _mute_flag = model.get_mute_flag()
        query = QSqlQuery()
        query.exec_("UPDATE general_setting SET mute_flag ='" + _mute_flag + "' WHERE id= 1")

    def db_connect(self, filename, server):
        db = QSqlDatabase.addDatabase(server)
        db.setDatabaseName(filename)
        if not db.open():
            QMessageBox.critical(None, "Cannot open database",
                                 "Unable to establish a database connection.\n"
                                 "This example needs SQLite support. Please read the Qt SQL "
                                 "driver documentation for information how to build it.\n\n"
                                 "Click Cancel to exit.", QMessageBox.Cancel)
            return False
        return True

    def db_create(self):
        query = QSqlQuery()
        query.exec_("create table general_setting(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "skin_set_temp varchar(100), air_set_temp varchar(100), mute_flag varchar(20))")

        query.exec_("create table patient_master(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "patient_name varchar(200), patient_age varchar(100), "
                    "patient_sex varchar(80),patient_id varchar(100),UNIQUE (patient_id) ON CONFLICT IGNORE)")

        query.exec_("create table patient_details(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "patient_id varchar(100), patient_skin_temp varchar(100), "
                    "air_temp varchar(80),UNIQUE (patient_skin_temp, air_temp) ON CONFLICT IGNORE)")

        query.prepare("INSERT INTO general_setting (skin_set_temp, air_set_temp, "
                      "mute_flag) "
                      "VALUES (:skin_set_temp, :air_set_temp,"
                      " :mute_flag)")
        query.bindValue(":skin_set_temp", 36)
        query.bindValue(":air_set_temp", 30)
        query.bindValue(":mute_flag", False)

        if not query.exec():
            qDebug() << "Error inserting data into table:\n" << query.lastError()
