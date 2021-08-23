import twint
import pandas

#up
c = twint.Config()
c.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
c.Store_csv = True
c.Output = 'Texas2021test.csv'
c.Since = '2020-1-01'
c.Until = '2021-7-27'
c.Geo ="30.798664,-98.922761,407.2059km"
twint.run.Search(c)

#up
h = twint.Config()
h.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
h.Store_csv = True
h.Output = 'Hawaii2021test.csv'
h.Since = '2020-1-01'
h.Until = '2021-7-27'
h.Geo ="20.788909,-156.908697,435.34472km"
twint.run.Search(h)

#up
a = twint.Config()
a.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
a.Store_csv = True
a.Output = 'Arizona021test.csv'
a.Since = '2020-1-01'
a.Until = '2021-7-27'
a.Geo =" 34.256337,-111.527533,328.54362km"
twint.run.Search(a)

#up
m = twint.Config()
m.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
m.Store_csv = True
m.Output = 'Massachusetts2021test.csv'
m.Since = '2020-1-01'
m.Until = '2021-7-27'
m.Geo ="42.260260,-71.830127,101.37082km"
twint.run.Search(m)

#down
i = twint.Config()
i.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
i.Store_csv = True
i.Output = 'Idaho2021test.csv'
i.Since = '2020-1-01'
i.Until = '2021-7-27'
i.Geo ="44.072942,-114.003996,330.54737km"
twint.run.Search(i)

#down
u = twint.Config()
u.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
u.Store_csv = True
u.Output = 'Utah2021test.csv'
u.Since = '2020-1-01'
u.Until = '2021-7-27'
u.Geo ="39.318800,-111.660658,332.00759km"
twint.run.Search(u)

#down
k = twint.Config()
k.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
k.Store_csv = True
k.Output = 'Kansas2021test.csv'
k.Since = '2020-1-01'
k.Until = '2021-7-27'
k.Geo ="38.259915,-98.388306,324.64631km"
twint.run.Search(k)


#down
p = twint.Config()
p.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
p.Store_csv = True
p.Output = 'Louisiana2021test.csv'
p.Since = '2020-1-01'
p.Until = '2021-7-27'
p.Geo ="30.874696,-92.054228,269.18204km"
twint.run.Search(p)

#down
w = twint.Config()
w.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
w.Store_csv = True
w.Output = 'Louisiana2021test.csv'
w.Since = '2020-1-01'
w.Until = '2021-7-27'
w.Geo ="44.688641,-89.817293,269.17821km"
twint.run.Search(p)

#down
w = twint.Config()
w.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
w.Store_csv = True
w.Output = 'Wisconsin2021test.csv'
w.Since = '2020-1-01'
w.Until = '2021-7-27'
w.Geo ="44.688641,-89.817293,269.17821km"
twint.run.Search(w)

#up
z = twint.Config()
z.Search = ' "electric prices" OR "electricty cost" OR "electricty bill" OR "enery cost" OR "energy grid" OR "electric bill" OR "utility price" OR "utility cost" OR "utility bill" OR "electric cost" OR "electric grid" OR "power outage" OR "electricity"'
z.Store_csv = True
z.Output = 'California2021test.csv'
z.Since = '2020-1-01'
z.Until = '2021-7-27'
z.Geo ="35.679319,-123.104606,669.10444km"
twint.run.Search(z)