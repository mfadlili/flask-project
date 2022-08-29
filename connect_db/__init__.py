import mysql.connector

class connect_mysql_db:
    def __init__(self):
        self.cnx = mysql.connector.connect(user="adminkelas", password="walikelas9A", host="coba-azure-mysql.mysql.database.azure.com", port=3306, database="students_9a", ssl_ca="DigiCertGlobalRootCA.crt.pem", ssl_disabled=False)
        self.cursor = self.cnx.cursor()

    def query_pelanggaran(self, id):
        query = ("SELECT * FROM pelanggaran_siswa WHERE students_id=%s")
        self.cursor.execute(query, [id])
        pelanggaran = []
        for i in self.cursor:
            pelanggaran.append(i[2])
        return pelanggaran
    
    def query_data_siswa(self, id):
        query = ("SELECT * FROM data_siswa WHERE id=%s")
        self.cursor.execute(query, [id])
        hasil = []
        for i in self.cursor:
            hasil.append(i[1])
            hasil.append(i[2])
            hasil.append(i[3])
            hasil.append(i[4])
        return hasil
    
    def query_nama(self):
        query = ("SELECT nama FROM data_siswa")
        self.cursor.execute(query)
        nama_panggilan = []
        for i in self.cursor:
            nama_panggilan.append(i[0])
        return nama_panggilan
    
    def input_data_siswa(self, nama, nama_lengkap, alamat, jk):
        add_students = ("INSERT INTO data_siswa "
              "(nama, nama_lengkap, alamat, jk) "
              "VALUES (%s, %s, %s, %s)")
        data_siswa = (nama, nama_lengkap, alamat, jk)
        self.cursor.execute(add_students, data_siswa)
        self.cnx.commit()
        
    def input_pelanggaran_siswa(self, id, pelanggaran):
        add_violation = ("INSERT INTO pelanggaran_siswa "
              "(students_id, pelanggaran) "
              "VALUES (%s, %s)")

        data_pelanggaran = (id, pelanggaran)
        self.cursor.execute(add_violation, data_pelanggaran)
        self.cnx.commit()
    
    def close_db(self):
        self.cursor.close()
        self.cnx.close()
