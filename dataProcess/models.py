# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class o2013Obs(models.Model):
    stid = models.SmallIntegerField(db_column='stID')  # Field name made lowercase.
    time = models.DateTimeField()
    temp = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    nmhc = models.FloatField(db_column='NMHC', blank=True, null=True)  # Field name made lowercase.
    no = models.FloatField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    no2 = models.FloatField(db_column='NO2', blank=True, null=True)  # Field name made lowercase.
    nox = models.FloatField(db_column='NOx', blank=True, null=True)  # Field name made lowercase.
    o3 = models.FloatField(db_column='O3', blank=True, null=True)  # Field name made lowercase.
    pm10 = models.FloatField(db_column='PM10', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.FloatField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.FloatField(db_column='RainFall', blank=True, null=True)  # Field name made lowercase.
    rh = models.FloatField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    so2 = models.FloatField(db_column='SO2', blank=True, null=True)  # Field name made lowercase.
    thc = models.FloatField(db_column='THC', blank=True, null=True)  # Field name made lowercase.
    uvb = models.FloatField(db_column='UVB', blank=True, null=True)  # Field name made lowercase.
    wd_hr = models.FloatField(db_column='WD_HR', blank=True, null=True)  # Field name made lowercase.
    wind_dir = models.FloatField(db_column='WIND_DIR', blank=True, null=True)  # Field name made lowercase.
    wind_sp = models.FloatField(db_column='WIND_SP', blank=True, null=True)  # Field name made lowercase.
    ws_hr = models.FloatField(db_column='WS_HR', blank=True, null=True)  # Field name made lowercase.
    rainph = models.FloatField(db_column='RainPH', blank=True, null=True)  # Field name made lowercase.
    raincond = models.FloatField(db_column='RainCond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2013OBS'


class o2014Obs(models.Model):
    stid = models.SmallIntegerField(db_column='stID')  # Field name made lowercase.
    time = models.DateTimeField()
    temp = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    nmhc = models.FloatField(db_column='NMHC', blank=True, null=True)  # Field name made lowercase.
    no = models.FloatField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    no2 = models.FloatField(db_column='NO2', blank=True, null=True)  # Field name made lowercase.
    nox = models.FloatField(db_column='NOx', blank=True, null=True)  # Field name made lowercase.
    o3 = models.FloatField(db_column='O3', blank=True, null=True)  # Field name made lowercase.
    pm10 = models.FloatField(db_column='PM10', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.FloatField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.FloatField(db_column='RainFall', blank=True, null=True)  # Field name made lowercase.
    rh = models.FloatField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    so2 = models.FloatField(db_column='SO2', blank=True, null=True)  # Field name made lowercase.
    thc = models.FloatField(db_column='THC', blank=True, null=True)  # Field name made lowercase.
    uvb = models.FloatField(db_column='UVB', blank=True, null=True)  # Field name made lowercase.
    wd_hr = models.FloatField(db_column='WD_HR', blank=True, null=True)  # Field name made lowercase.
    wind_dir = models.FloatField(db_column='WIND_DIR', blank=True, null=True)  # Field name made lowercase.
    wind_sp = models.FloatField(db_column='WIND_SP', blank=True, null=True)  # Field name made lowercase.
    ws_hr = models.FloatField(db_column='WS_HR', blank=True, null=True)  # Field name made lowercase.
    rainph = models.FloatField(db_column='RainPH', blank=True, null=True)  # Field name made lowercase.
    raincond = models.FloatField(db_column='RainCond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2014OBS'


class o2015Obs(models.Model):
    stid = models.SmallIntegerField(db_column='stID')  # Field name made lowercase.
    time = models.DateTimeField()
    temp = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    nmhc = models.FloatField(db_column='NMHC', blank=True, null=True)  # Field name made lowercase.
    no = models.FloatField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    no2 = models.FloatField(db_column='NO2', blank=True, null=True)  # Field name made lowercase.
    nox = models.FloatField(db_column='NOx', blank=True, null=True)  # Field name made lowercase.
    o3 = models.FloatField(db_column='O3', blank=True, null=True)  # Field name made lowercase.
    pm10 = models.FloatField(db_column='PM10', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.FloatField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.FloatField(db_column='RainFall', blank=True, null=True)  # Field name made lowercase.
    rh = models.FloatField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    so2 = models.FloatField(db_column='SO2', blank=True, null=True)  # Field name made lowercase.
    thc = models.FloatField(db_column='THC', blank=True, null=True)  # Field name made lowercase.
    uvb = models.FloatField(db_column='UVB', blank=True, null=True)  # Field name made lowercase.
    wd_hr = models.FloatField(db_column='WD_HR', blank=True, null=True)  # Field name made lowercase.
    wind_dir = models.FloatField(db_column='WIND_DIR', blank=True, null=True)  # Field name made lowercase.
    wind_sp = models.FloatField(db_column='WIND_SP', blank=True, null=True)  # Field name made lowercase.
    ws_hr = models.FloatField(db_column='WS_HR', blank=True, null=True)  # Field name made lowercase.
    rainph = models.FloatField(db_column='RainPH', blank=True, null=True)  # Field name made lowercase.
    raincond = models.FloatField(db_column='RainCond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2015OBS'


class o2016Obs(models.Model):
    stid = models.SmallIntegerField(db_column='stID')  # Field name made lowercase.
    time = models.DateTimeField()
    temp = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    nmhc = models.FloatField(db_column='NMHC', blank=True, null=True)  # Field name made lowercase.
    no = models.FloatField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    no2 = models.FloatField(db_column='NO2', blank=True, null=True)  # Field name made lowercase.
    nox = models.FloatField(db_column='NOx', blank=True, null=True)  # Field name made lowercase.
    o3 = models.FloatField(db_column='O3', blank=True, null=True)  # Field name made lowercase.
    pm10 = models.FloatField(db_column='PM10', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.FloatField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.FloatField(db_column='RainFall', blank=True, null=True)  # Field name made lowercase.
    rh = models.FloatField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    so2 = models.FloatField(db_column='SO2', blank=True, null=True)  # Field name made lowercase.
    thc = models.FloatField(db_column='THC', blank=True, null=True)  # Field name made lowercase.
    uvb = models.FloatField(db_column='UVB', blank=True, null=True)  # Field name made lowercase.
    wd_hr = models.FloatField(db_column='WD_HR', blank=True, null=True)  # Field name made lowercase.
    wind_dir = models.FloatField(db_column='WIND_DIR', blank=True, null=True)  # Field name made lowercase.
    wind_sp = models.FloatField(db_column='WIND_SP', blank=True, null=True)  # Field name made lowercase.
    ws_hr = models.FloatField(db_column='WS_HR', blank=True, null=True)  # Field name made lowercase.
    rainph = models.FloatField(db_column='RainPH', blank=True, null=True)  # Field name made lowercase.
    raincond = models.FloatField(db_column='RainCond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2016OBS'


class o2017Obs(models.Model):
    stid = models.SmallIntegerField(db_column='stID')  # Field name made lowercase.
    time = models.DateTimeField()
    temp = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    nmhc = models.FloatField(db_column='NMHC', blank=True, null=True)  # Field name made lowercase.
    no = models.FloatField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    no2 = models.FloatField(db_column='NO2', blank=True, null=True)  # Field name made lowercase.
    nox = models.FloatField(db_column='NOx', blank=True, null=True)  # Field name made lowercase.
    o3 = models.FloatField(db_column='O3', blank=True, null=True)  # Field name made lowercase.
    pm10 = models.FloatField(db_column='PM10', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.FloatField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.FloatField(db_column='RainFall', blank=True, null=True)  # Field name made lowercase.
    rh = models.FloatField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    so2 = models.FloatField(db_column='SO2', blank=True, null=True)  # Field name made lowercase.
    thc = models.FloatField(db_column='THC', blank=True, null=True)  # Field name made lowercase.
    uvb = models.FloatField(db_column='UVB', blank=True, null=True)  # Field name made lowercase.
    wd_hr = models.FloatField(db_column='WD_HR', blank=True, null=True)  # Field name made lowercase.
    wind_dir = models.FloatField(db_column='WIND_DIR', blank=True, null=True)  # Field name made lowercase.
    wind_sp = models.FloatField(db_column='WIND_SP', blank=True, null=True)  # Field name made lowercase.
    ws_hr = models.FloatField(db_column='WS_HR', blank=True, null=True)  # Field name made lowercase.
    rainph = models.FloatField(db_column='RainPH', blank=True, null=True)  # Field name made lowercase.
    raincond = models.FloatField(db_column='RainCond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2017OBS'


class o2018Obs(models.Model):
    stid = models.SmallIntegerField(db_column='stID')  # Field name made lowercase.
    time = models.DateTimeField()
    temp = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    nmhc = models.FloatField(db_column='NMHC', blank=True, null=True)  # Field name made lowercase.
    no = models.FloatField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    no2 = models.FloatField(db_column='NO2', blank=True, null=True)  # Field name made lowercase.
    nox = models.FloatField(db_column='NOx', blank=True, null=True)  # Field name made lowercase.
    o3 = models.FloatField(db_column='O3', blank=True, null=True)  # Field name made lowercase.
    pm10 = models.FloatField(db_column='PM10', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.FloatField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.FloatField(db_column='RainFall', blank=True, null=True)  # Field name made lowercase.
    rh = models.FloatField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    so2 = models.FloatField(db_column='SO2', blank=True, null=True)  # Field name made lowercase.
    thc = models.FloatField(db_column='THC', blank=True, null=True)  # Field name made lowercase.
    uvb = models.FloatField(db_column='UVB', blank=True, null=True)  # Field name made lowercase.
    wd_hr = models.FloatField(db_column='WD_HR', blank=True, null=True)  # Field name made lowercase.
    wind_dir = models.FloatField(db_column='WIND_DIR', blank=True, null=True)  # Field name made lowercase.
    wind_sp = models.FloatField(db_column='WIND_SP', blank=True, null=True)  # Field name made lowercase.
    ws_hr = models.FloatField(db_column='WS_HR', blank=True, null=True)  # Field name made lowercase.
    rainph = models.FloatField(db_column='RainPH', blank=True, null=True)  # Field name made lowercase.
    raincond = models.FloatField(db_column='RainCond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2018OBS'


class o2019Obs(models.Model):
    stid = models.SmallIntegerField(db_column='stID')  # Field name made lowercase.
    time = models.DateTimeField()
    temp = models.FloatField(blank=True, null=True)
    ch4 = models.FloatField(db_column='CH4', blank=True, null=True)  # Field name made lowercase.
    co = models.FloatField(db_column='CO', blank=True, null=True)  # Field name made lowercase.
    nmhc = models.FloatField(db_column='NMHC', blank=True, null=True)  # Field name made lowercase.
    no = models.FloatField(db_column='NO', blank=True, null=True)  # Field name made lowercase.
    no2 = models.FloatField(db_column='NO2', blank=True, null=True)  # Field name made lowercase.
    nox = models.FloatField(db_column='NOx', blank=True, null=True)  # Field name made lowercase.
    o3 = models.FloatField(db_column='O3', blank=True, null=True)  # Field name made lowercase.
    pm10 = models.FloatField(db_column='PM10', blank=True, null=True)  # Field name made lowercase.
    pm25 = models.FloatField(db_column='PM25', blank=True, null=True)  # Field name made lowercase.
    rainfall = models.FloatField(db_column='RainFall', blank=True, null=True)  # Field name made lowercase.
    rh = models.FloatField(db_column='RH', blank=True, null=True)  # Field name made lowercase.
    so2 = models.FloatField(db_column='SO2', blank=True, null=True)  # Field name made lowercase.
    thc = models.FloatField(db_column='THC', blank=True, null=True)  # Field name made lowercase.
    uvb = models.FloatField(db_column='UVB', blank=True, null=True)  # Field name made lowercase.
    wd_hr = models.FloatField(db_column='WD_HR', blank=True, null=True)  # Field name made lowercase.
    wind_dir = models.FloatField(db_column='WIND_DIR', blank=True, null=True)  # Field name made lowercase.
    wind_sp = models.FloatField(db_column='WIND_SP', blank=True, null=True)  # Field name made lowercase.
    ws_hr = models.FloatField(db_column='WS_HR', blank=True, null=True)  # Field name made lowercase.
    rainph = models.FloatField(db_column='RainPH', blank=True, null=True)  # Field name made lowercase.
    raincond = models.FloatField(db_column='RainCond', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '2019OBS'


class Stinfo(models.Model):
    stid = models.SmallIntegerField(db_column='stID', primary_key=True)  # Field name made lowercase.
    type = models.CharField(max_length=10)
    ch_name = models.CharField(max_length=50, blank=True, null=True)
    en_name = models.CharField(max_length=50, blank=True, null=True)
    descr = models.CharField(max_length=50, blank=True, null=True)
    county = models.CharField(max_length=4, blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stInfo'
