#funtion
# #biodata
def getBiodata(nama,kelas,sd,smp):
    pendidikan = getPendidikan(sd,smp)
    return "nama saya : " + nama + "dari kelas :" + kelas + pendidikan

#history
def getPendidikan(sd,smp):
    sd = "SD saya : " +  sd
    smp = "SMP saya" + smp
    return sd + smp