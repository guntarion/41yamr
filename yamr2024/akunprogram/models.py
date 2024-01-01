from django.db import models
from django.utils import timezone
from unitbidang.models import Unit

class AkunProgram(models.Model):
    IN = 'IN'
    OT = 'OT'
    JENIS_INPUT_OUTPUT_CHOICES = [
        (IN, 'Input'),
        (OT, 'Output'),
    ]


    NON_ASSET = 'nonAsset'
    YES_ASSET = 'yesAsset'
    JENIS_PROGRAM_CHOICES = [
        (NON_ASSET, 'Non Asset'),
        (YES_ASSET, 'Asset'),
    ]

    PERIODE_BULAN = 'bulan'
    PERIODE_TAHUN = 'tahun'
    PERIODE_CHOICES = [
        (PERIODE_BULAN, 'Bulan'),
        (PERIODE_TAHUN, 'Tahun'),
    ]

    SIFAT_FIKS = 'fiks'
    SIFAT_FLEKSIBEL = 'fleksibel'
    SIFAT_PERIODE_CHOICES = [
        (SIFAT_FIKS, 'Fiks'),
        (SIFAT_FLEKSIBEL, 'Fleksibel'),
    ]

    TERENCANA = 'terencana'
    MODIFIKASI = 'modifikasi'
    USULANBARU = 'usulanbaru'
    DIPERTIMBANGKAN = 'dipertimbangkan'
    DITOLAK = 'usulanditolak'
    DIGUGURKAN = 'digugurkan'
    SIFAT_KREASI_CHOICES = [
        (TERENCANA, 'Terencana'),
        (MODIFIKASI, 'Modifikasi'),
        (USULANBARU, 'Usulan Baru'),
        (DIPERTIMBANGKAN, 'Dipertimbangkan'),
        (DITOLAK, 'Usulan Ditolak'),
        (DIGUGURKAN, 'Digugurkan'),
    ]

    namaAkun = models.CharField(max_length=100)
    unitBidang = models.ForeignKey(Unit, on_delete=models.CASCADE)
    jenisInputOutput = models.CharField(
        max_length=2,
        choices=JENIS_INPUT_OUTPUT_CHOICES,
        default=OT,
    )
    jenisProgram = models.CharField(
        max_length=8,
        choices=JENIS_PROGRAM_CHOICES,
        default=NON_ASSET,
    )
    kodeAkun = models.CharField(max_length=100)
    kodeAnggaran = models.CharField(max_length=100)
    sifatKreasi = models.CharField(
        max_length=15,  # length of the longest choice
        choices=SIFAT_KREASI_CHOICES,
        default=TERENCANA,
    )
    periodeAnggaran = models.CharField(
        max_length=5,
        choices=PERIODE_CHOICES,
        default=PERIODE_BULAN,
    )
    sifatPeriodeAnggaran = models.CharField(
        max_length=9,
        choices=SIFAT_PERIODE_CHOICES,
        default=SIFAT_FIKS,
    )
    anggaranSatuTahun = models.DecimalField(max_digits=25, decimal_places=2, default=0.00) #komulatif dari AnggaranBulanan
    anggaranTerencana = models.DecimalField(max_digits=25, decimal_places=2, default=0.00) #dari awal tahun sampai bulan ini
    anggaranRealisasi = models.DecimalField(max_digits=25, decimal_places=2, default=0.00) #dari awal tahun sampai bulan ini
    anggaranSelisih = models.DecimalField(max_digits=25, decimal_places=2, default=0.00) #dari awal tahun sampai bulan ini
    keterangan = models.TextField()
    creationDate = models.DateTimeField(auto_now_add=True)
    lastUpdateTime = models.DateTimeField(auto_now=True)

class AnggaranBulanan(models.Model):
    SESUAI = 'sesuai'
    MELEBIHI = 'melebihi'
    KURANGDARI = 'kurangdari'
    TAKTERLAKSANATEKNIS = 'takterlaksanateknis'
    TAKTERLAKSANADANA = 'takterlaksanadana'
    STATUS_PROGRAM_CHOICES = [
        (SESUAI, 'Sesuai'),
        (MELEBIHI, 'Melebihi'),
        (KURANGDARI, 'Kurang Dari'),
        (TAKTERLAKSANATEKNIS, 'Tak Terlaksana Teknis'),
        (TAKTERLAKSANADANA, 'Tak Terlaksana Dana'),
    ]

    akunProgram = models.ForeignKey(AkunProgram, on_delete=models.CASCADE)
    bulanAnggaran = models.IntegerField(blank=True, null=True)  # 1 for January, 2 for February, etc.
    tahunAnggaran = models.IntegerField()
    rupiahAnggaran = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    rupiahRealisasi = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    rupiahSelisih = models.DecimalField(max_digits=25, decimal_places=2, default=0.00)
    statusProgram = models.CharField(
        max_length=20,  # length of the longest choice
        choices=STATUS_PROGRAM_CHOICES,
        blank=True,
        null=True,
    )
    keterangan = models.TextField()
    creationDate = models.DateTimeField(auto_now_add=True)
    lastUpdateTime = models.DateTimeField(auto_now=True)
    jumlahRevisi = models.IntegerField(default=0)
    revisiTerakhirOleh = models.CharField(max_length=100, default='admin')

