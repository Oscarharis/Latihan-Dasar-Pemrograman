

#function deskriptif
def ambilBiodata():
  nama= "oscar haris.n"
  kelas = "TI2023B"
  return "Nama saya :"+nama+ "Kelas saya"+kelas

def ambilpendidikan():
  sd = "SDN 5 PASIR HALANG"
  smp = "SMPN 1 SUKARAJA"
  smk = "SMK TAMAN SISWA"
  return "sd saya :"+sd + "smp saya "+smp + "smk saya "+smk

#function simple
def getBiodata(nama,kelas):
    return "Nama saya :"+nama+ "Kelas saya"+kelas
def getPendidikan(sd,smp,smk):
    return "sd saya :"+sd + "smp saya "+smp + "smk saya" +smk


biodata = ambilBiodata()
riwayatpendidikan = ambilpendidikan()
print(biodata)
print(riwayatpendidikan)
print("==================================")
getbiodata = getBiodata("oscar haris.n","TI2023B")
getriwayatpendidikan = getPendidikan("SDN 5 PASIR HALANG","SMPN 1 SUKARAJA","SMK TAMAN SISWA")
print(getbiodata)
print(getriwayatpendidikan)