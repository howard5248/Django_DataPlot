from django.shortcuts import render
from .models import Stinfo,o2013Obs,o2014Obs,o2015Obs,o2016Obs,o2017Obs,o2018Obs,o2019Obs
from .forms import DatePickForm
from datetime import datetime,timedelta
import pandas as pd

### Plotly
from plotly.offline import plot
import plotly.graph_objects as go
# from plotly.graph_objs import Scatter

from django.db.models import Q

DBname = 'epaobs'



def changeColname(pdOld,flag):
    pdOld = pdOld.set_index(pdOld['time'])
    pdOld = pdOld.drop(['time'], axis=1).drop(['id'], axis=1)
    allSTList = list(pdOld['stid'].unique())
    pdNew = pd.DataFrame()
    for st in allSTList:
        dataTmp = pdOld[pdOld['stid'] == st].drop(['stid'], axis=1)
        if flag=='cwb':
            ST_cname = Stinfo.objects.using(DBname).filter(stid=st)
            ST_cname = [i.ch_name for i in ST_cname][0]
            coltuples = [(ST_cname, self.cwbVarInfo[i.upper()]) for i in list(dataTmp.columns)]
        elif flag=='epa':
            ST_cname = Stinfo.objects.using(DBname).filter(stid=st)
            ST_cname = [i.ch_name for i in ST_cname][0]
            coltuples = [(ST_cname, i) for i in list(dataTmp.columns)]
        dataTmp.columns = pd.MultiIndex.from_tuples(coltuples, names=['st', 'spc'])
        pdNew = pd.concat([pdNew, dataTmp], axis=1)
    return pdNew

def getepaobs(stlist,spclist,date1,date2):
    for year in range(date1.year,date2.year+1):
        c_stlist =  '( '+' | '.join(['Q(stid="'+id+'")' for id in stlist ])+' )'
        cmd = 'o'+str(year)+'Obs.objects.using(DBname).filter('+c_stlist + \
                ' & Q(time__range=["'+date1.strftime("%Y-%m-%d")+'","'+(date2+timedelta(days=1)).strftime("%Y-%m-%d")+'"]))'
        # print(cmd)
        obs = eval(cmd)
        
        df = pd.DataFrame(list(obs.values()))
    return(df)
    # for st in stlist:

def selectSt(request):
    stlists = Stinfo.objects.using(DBname).all().filter(~Q(type='FPG')).order_by("-county")
    if request.method == 'GET':
        # stOptions = tuple([ ( str(st.stid),st.ch_name ) for st in stlists ])
        return render(request,'dataProcess/obsStList.html',{'stlists':stlists,'form':DatePickForm()})
    else:
        ID_list = request.POST.getlist('stID')
        spec_list = request.POST.getlist('spec')
        date1 = datetime.strptime(request.POST.get('date_field1'),'%Y-%m-%d')
        date2 = datetime.strptime(request.POST.get('date_field2'),'%Y-%m-%d')
        diffdate = (date2-date1).days + 1
        if not ID_list or not spec_list:
            return render(request,'dataProcess/obsStList.html',{'stlists':stlists,'form':DatePickForm(),'error':'物種及測站不可為空'})
        elif diffdate <= 0 or diffdate >= 99:
            return render(request,'dataProcess/obsStList.html',{'stlists':stlists,'form':DatePickForm(),'error':'日期必須介於99天內，且結束日必須大於起始日'})
        else:
            ###取得資料
            df = getepaobs(ID_list,spec_list,date1,date2)
            if len(df) == 0:
                return render(request, "dataProcess/obsStList.html", {'stlists':stlists,'form':DatePickForm(),'error':'本次篩選並無任何資料產生!'})
            df = changeColname(df,'epa')
            cst_list = df.columns.levels[0]
            # print(df)
            
            plot_div = ''
            for spec in spec_list:
                cmd = []
                for st in cst_list:
                    y_data = df[st,spec]
                    y_data[y_data<0] = None   #去除-999
                    cmd.append(go.Scatter(x=df.index, y=y_data, mode='lines', name=st, opacity=0.8)) 

                layout = go.Layout(
                            width=1200,
                            height=500,
                            title= spec,font=dict(family='<b>Courier New</b>', size=20, color='black'),
                            xaxis=dict(tickfont=dict(family='<b>Courier New</b>', size=15),color='black',gridcolor='#9d9d9d',
                                    showline=True,linewidth=3,mirror='ticks',tickformat='%d %B (%a)<br>%Y'),
                            yaxis=dict(rangemode='tozero',
                                    titlefont=dict(family='<b>Courier New</b>',color='black'),
                                    tickfont=dict(family='<b>Courier New</b>', size=15,color='black'),
                                    gridcolor='#9d9d9d',showline=True,linewidth=3,mirror='ticks'),
                            # showlegend=True,
                            legend=dict(font={'size':12}, bordercolor="Black",borderwidth=2,traceorder="normal",),
                        )

                plot_div = plot_div + plot({'data':cmd, "layout" : layout},
                                output_type='div', include_plotlyjs=False)
            return render(request, "dataProcess/obsStList.html", {'stlists':stlists,'form':DatePickForm(),'plot_div': plot_div})