class DataModel:
    def __init__(self):
        self.date_time = str()
        self.skin_temp = str()
        self.air_temp = str()
        self.mute_flag = 1
        self.patient_name = str()
        self.form_patient_name = str()
        self.form_patient_age = str()
        self.form_patient_sex = str()
        self.patient_sex = str()
        self.patient_age = str()
        self.patient_id = str()
        self.find_by_patient_id = str()
        self.patient_skin_temp = str()
        self.heater_output = str()
        self.skin_low_temp = float()
        self.skin_high_temp = float()
        self.air_low_temp = float()
        self.air_high_temp = float()
        self.skin_cal_point = float()
        self.air_cal_point = float()

    def set_skin_low_temp(self, _skin_low_temp):
        self.skin_low_temp = _skin_low_temp

    def get_skin_low_temp(self):
        return self.skin_low_temp

    def set_skin_high_temp(self, _skin_high_temp):
        self.skin_high_temp = _skin_high_temp

    def get_skin_high_temp(self):
        return self.skin_high_temp

    def set_air_low_temp(self, _air_low_temp):
        self.air_low_temp = _air_low_temp

    def get_air_low_temp(self):
        return self.air_low_temp

    def set_air_high_temp(self, _air_high_temp):
        self.air_high_temp = _air_high_temp

    def get_air_high_temp(self):
        return self.air_high_temp

    def set_skin_cal_point(self, _skin_cal_point):
        self.skin_cal_point = _skin_cal_point

    def get_skin_cal_point(self):
        return self.skin_cal_point

    def set_air_cal_point(self, _air_cal_point):
        self.air_cal_point = _air_cal_point

    def get_air_cal_point(self):
        return self.air_cal_point

    def set_heater_output(self, _heater_output):
        self.heater_output = _heater_output

    def get_heater_output(self):
        return self.heater_output

    def set_form_patient_name(self, _form_patient_name):
        self.form_patient_name = _form_patient_name

    def get_form_patient_name(self):
        return self.form_patient_name

    def set_form_patient_age(self, _form_patient_age):
        self.form_patient_age = _form_patient_age

    def get_form_patient_age(self):
        return self.form_patient_age

    def set_form_patient_sex(self, _form_patient_sex):
        self.form_patient_sex = _form_patient_sex

    def get_form_patient_sex(self):
        return self.form_patient_sex

    def set_date_time(self, _date_time):
        self.date_time = _date_time

    def get_date_time(self):
        return self.date_time

    def set_mute_flag(self, _mute_flag):
        self.mute_flag = _mute_flag

    def get_mute_flag(self):
        return self.mute_flag

    def set_skin_temp(self, _skin_set_temp):
        self.skin_temp = _skin_set_temp

    def get_skin_temp(self):
        return self.skin_temp

    def set_air_temp(self, _air_set_temp):
        self.air_temp = _air_set_temp

    def get_air_temp(self):
        return self.air_temp

    def set_patient_name(self, _patient_name):
        self.patient_name = _patient_name

    def get_patient_name(self):
        return self.patient_name

    def set_patient_age(self, _patient_age):
        self.patient_age = _patient_age

    def get_patient_age(self):
        return self.patient_age

    def set_patient_sex(self, _patient_sex):
        self.patient_sex = _patient_sex

    def get_patient_sex(self):
        return self.patient_sex

    def set_patient_id(self, _patient_id):
        self.patient_id = _patient_id

    def get_patient_id(self):
        return self.patient_id

    def set_patient_skin_temp(self, _patient_skin_temp):
        self.patient_skin_temp = _patient_skin_temp

    def get_patient_skin_temp(self):
        return self.patient_skin_temp

    def set_find_by_patient_id(self, _find_by_patient_id):
        self.find_by_patient_id = _find_by_patient_id

    def get_find_by_patient_id(self):
        self.find_by_patient_id
