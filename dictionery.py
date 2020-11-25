# tipe dat dictionery atau kamus menghubungkan  key dan value atau kpv  key value pair
kamus ={ }
kamus ['anak'] = 'son'
kamus [ 'istri'] = 'wive'
kamus ['ayah'] = 'father'

print (kamus['ayah'])
data_dari_server_gojek ={
    'tanggal':'20-11-2020',
    'driver_list':[{'nama':'eko','jarak':20},
                   {'nama':'jojo','jarak':30},
                   {'nama':'koko','jarak' :100}
] }
print(data_dari_server_gojek)
print(f"Driver disekitar sini {data_dari_server_gojek['driver_list']}")
print(f"Driver #1{data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #3{data_dari_server_gojek['driver_list'][2]}")
print(f"Driver terdekat berjarak{data_dari_server_gojek['driver_list'][0]['jarak']} meter")

