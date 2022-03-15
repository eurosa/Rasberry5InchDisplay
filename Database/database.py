import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox, QTableWidgetItem


class DataBaseManagement:
    def __init__(self):
        self.patientSex = None
        self.patientAge = None
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
        query2 =  QSqlQuery()
        query3 = QSqlQuery()
        query2.prepare("DELETE FROM patient_master WHERE  id NOT IN ( SELECT id FROM patient_master ORDER BY id desc limit 5000)")
        if not query2.exec():
            qDebug() << "Error deleting data from table:\n" << query2.lastError()

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

        query3.prepare(
            "DELETE FROM patient_details WHERE  patient_id NOT IN ( SELECT pm.patient_id  FROM patient_master pm "
            "WHERE patient_details.patient_id = pm.patient_id)")
        if not query3.exec():
            qDebug() << "Error deleting data into table:\n" << query3.lastError()

    def queryGeneralSettingsData(self, model):
        query = QSqlQuery()
        query.exec_("SELECT * FROM general_setting where id=1")
        while query.next():
            model.set_skin_temp(query.value('skin_set_temp'))
            model.set_air_temp(query.value('air_set_temp'))
            model.set_mute_flag(query.value('mute_flag'))
            model.set_heater_output(query.value('heater_output'))
            model.set_skin_low_temp(query.value('skin_low_temp'))
            model.set_skin_high_temp(query.value('skin_high_temp'))
            model.set_air_low_temp(query.value('air_low_temp'))
            model.set_air_high_temp(query.value('air_high_temp'))
            model.set_skin_cal_point(query.value('skin_cal_point'))
            model.set_air_cal_point(query.value('air_cal_point'))

    def getPatientById(self, text, model):
        query = QSqlQuery()
        self.patientName = ""
        self.patientAge = ""
        self.patientSex = ""
        query.exec_("SELECT * FROM patient_master where patient_id=" + "'" + str(text) + "'")
        while query.next():
            self.patientName = query.value('patient_name')
            self.patientAge = query.value('patient_age')
            self.patientSex = query.value('patient_sex')
        model.set_form_patient_name(self.patientName)
        model.set_patient_age(self.patientAge)
        model.set_patient_sex(self.patientSex)

    def updateSkinTempValue(self, model):
        _skin_temp = model.get_skin_temp()
        query = QSqlQuery()
        query.exec_("UPDATE general_setting SET skin_set_temp ='" + str(
            _skin_temp) + "' WHERE id= 1")  # str("{:.1f}".format(tempValue))

    def updateHeaterOutput(self, model):
        _heater_output = model.get_heater_output()
        query = QSqlQuery()
        query.exec_("UPDATE general_setting SET heater_output ='" + str(_heater_output) + "' WHERE id= 1")

    def updateAirTempValue(self, model):
        _air_temp = model.get_air_temp()
        query = QSqlQuery()
        query.exec_("UPDATE general_setting SET air_set_temp ='" + str(_air_temp) + "' WHERE id= 1")

    def updateMuteValue(self, model):
        _mute_flag = model.get_mute_flag()
        query = QSqlQuery()
        query.exec_("UPDATE general_setting SET mute_flag ='" + _mute_flag + "' WHERE id= 1")

    def updateSettingData(self, model):
        query = QSqlQuery()
        query.exec_(
            "UPDATE general_setting SET skin_low_temp ='" + str(model.get_skin_low_temp()) + "',skin_high_temp ='" + str(model.get_skin_high_temp()) + "', air_low_temp ='" + str(model.get_air_low_temp()) + "',"
            "air_high_temp ='" + str(model.get_air_high_temp()) + "', skin_cal_point ='" + str(model.get_skin_cal_point()) + "',air_cal_point ='" + str(model.get_air_cal_point()) + "' WHERE id= 1")

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
                    "skin_set_temp varchar(100), air_set_temp varchar(100), mute_flag varchar(20), heater_output "
                    "varchar(20), skin_low_temp varchar(100), skin_high_temp varchar(100), air_low_temp varchar(100), "
                    "air_high_temp varchar(100), skin_cal_point varchar(100), air_cal_point varchar(100))")

        query.exec_("create table patient_master(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "patient_name varchar(200), patient_age varchar(100), "
                    "patient_sex varchar(80),patient_id varchar(100),UNIQUE (patient_id) ON CONFLICT IGNORE)")

        query.exec_("create table patient_details(id INTEGER PRIMARY KEY AUTOINCREMENT, "
                    "patient_id varchar(100), patient_skin_temp varchar(100), "
                    "air_temp varchar(80),UNIQUE (patient_skin_temp, air_temp) ON CONFLICT IGNORE)")

        query.prepare("INSERT INTO general_setting (skin_set_temp, air_set_temp, "
                      "mute_flag, heater_output, skin_low_temp, skin_high_temp, air_low_temp, air_high_temp, "
                      "skin_cal_point, air_cal_point) "
                      "VALUES (:skin_set_temp, :air_set_temp,"
                      ":mute_flag, :heater_output, :skin_low_temp, :skin_high_temp, :air_low_temp, :air_high_temp, "
                      ":skin_cal_point, :air_cal_point)")
        query.bindValue(":skin_set_temp", 360)
        query.bindValue(":air_set_temp", 300)
        query.bindValue(":mute_flag", False)
        query.bindValue(":heater_output", 100)
        query.bindValue(":skin_low_temp", 320)
        query.bindValue(":skin_high_temp", 380)
        query.bindValue(":air_low_temp", 300)
        query.bindValue(":air_high_temp", 390)
        query.bindValue(":skin_cal_point", 0)
        query.bindValue(":air_cal_point", 0)

        if not query.exec():
            qDebug() << "Error inserting data into table:\n" << query.lastError()
