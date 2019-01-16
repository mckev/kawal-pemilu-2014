import unittest

from classes.browser import Browser
from classes.kpu_c1_web import KpuC1Web


class TestKpuC1Web(unittest.TestCase):

    def test_parse_c1_html_main(self):
        # Main page
        content = Browser.browse_url('https://pilpres2014.kpu.go.id/c1.php')
        administrative_type, administratives = KpuC1Web.parse_c1_html(content)
        self.assertEqual(administrative_type, 'Provinsi')
        expected_administratives = [
            {'name': 'ACEH', 'id': 1, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=1'},
            {'name': 'SUMATERA UTARA', 'id': 6728, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=6728'},
            {'name': 'SUMATERA BARAT', 'id': 12920, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=12920'},
            {'name': 'RIAU', 'id': 14086, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=14086'},
            {'name': 'JAMBI', 'id': 15885, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=15885'},
            {'name': 'SUMATERA SELATAN', 'id': 17404, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=17404'},
            {'name': 'BENGKULU', 'id': 20802, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=20802'},
            {'name': 'LAMPUNG', 'id': 22328, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=22328'},
            {'name': 'KEPULAUAN BANGKA BELITUNG', 'id': 24993, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=24993'},
            {'name': 'KEPULAUAN RIAU', 'id': 25405, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=25405'},
            {'name': 'DKI JAKARTA', 'id': 25823, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=25823'},
            {'name': 'JAWA BARAT', 'id': 26141, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=26141'},
            {'name': 'JAWA TENGAH', 'id': 32676, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=32676'},
            {'name': 'DAERAH ISTIMEWA YOGYAKARTA', 'id': 41863, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=41863'},
            {'name': 'JAWA TIMUR', 'id': 42385, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=42385'},
            {'name': 'BANTEN', 'id': 51578, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=51578'},
            {'name': 'BALI', 'id': 53241, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=53241'},
            {'name': 'NUSA TENGGARA BARAT', 'id': 54020, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=54020'},
            {'name': 'NUSA TENGGARA TIMUR', 'id': 55065, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=55065'},
            {'name': 'KALIMANTAN BARAT', 'id': 58285, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=58285'},
            {'name': 'KALIMANTAN TENGAH', 'id': 60371, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=60371'},
            {'name': 'KALIMANTAN SELATAN', 'id': 61965, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=61965'},
            {'name': 'KALIMANTAN TIMUR', 'id': 64111, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=64111'},
            {'name': 'SULAWESI UTARA', 'id': 65702, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=65702'},
            {'name': 'SULAWESI TENGAH', 'id': 67393, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=67393'},
            {'name': 'SULAWESI SELATAN', 'id': 69268, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=69268'},
            {'name': 'SULAWESI TENGGARA', 'id': 72551, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=72551'},
            {'name': 'GORONTALO', 'id': 74716, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=74716'},
            {'name': 'SULAWESI BARAT', 'id': 75425, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=75425'},
            {'name': 'MALUKU', 'id': 76096, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=76096'},
            {'name': 'MALUKU UTARA', 'id': 77085, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=77085'},
            {'name': 'PAPUA', 'id': 78203, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=78203'},
            {'name': 'PAPUA BARAT', 'id': 81877, 'parent_id': 0,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=81877'}
        ]
        self.assertEqual(administratives, expected_administratives)

    def test_parse_c1_html_provinsi(self):
        # Provinsi 'SUMATERA UTARA' page
        content = Browser.browse_url('https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=6728')
        administrative_type, administratives = KpuC1Web.parse_c1_html(content)
        self.assertEqual(administrative_type, 'Kabupaten/Kota')
        expected_administratives = [
            {'name': 'TAPANULI TENGAH', 'id': 7240, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7240'},
            {'name': 'TAPANULI UTARA', 'id': 7438, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7438'},
            {'name': 'TAPANULI SELATAN', 'id': 7697, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7697'},
            {'name': 'NIAS', 'id': 7960, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7960'},
            {'name': 'LANGKAT', 'id': 8094, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=8094'},
            {'name': 'KARO', 'id': 8408, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=8408'},
            {'name': 'DELI SERDANG', 'id': 8688, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=8688'},
            {'name': 'SIMALUNGUN', 'id': 9114, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=9114'},
            {'name': 'ASAHAN', 'id': 9497, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=9497'},
            {'name': 'LABUHANBATU', 'id': 9727, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=9727'},
            {'name': 'DAIRI', 'id': 9835, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=9835'},
            {'name': 'TOBA SAMOSIR', 'id': 10020, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=10020'},
            {'name': 'MANDAILING NATAL', 'id': 10227, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=10227'},
            {'name': 'NIAS SELATAN', 'id': 10646, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=10646'},
            {'name': 'PAKPAK BHARAT', 'id': 11022, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11022'},
            {'name': 'HUMBANG HASUNDUTAN', 'id': 11083, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11083'},
            {'name': 'SAMOSIR', 'id': 11247, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11247'},
            {'name': 'SERDANG BEDAGAI', 'id': 11374, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11374'},
            {'name': 'BATU BARA', 'id': 11635, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11635'},
            {'name': 'PADANG LAWAS UTARA', 'id': 12208, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=12208'},
            {'name': 'PADANG LAWAS', 'id': 12606, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=12606'},
            {'name': 'LABUHANBATU SELATAN', 'id': 6729, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=6729'},
            {'name': 'LABUHANBATU UTARA', 'id': 6789, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=6789'},
            {'name': 'NIAS UTARA', 'id': 6888, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=6888'},
            {'name': 'NIAS BARAT', 'id': 7013, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7013'},
            {'name': 'KOTA MEDAN', 'id': 11743, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11743'},
            {'name': 'KOTA PEMATANGSIANTAR', 'id': 11916, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11916'},
            {'name': 'KOTA SIBOLGA', 'id': 11978, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=11978'},
            {'name': 'KOTA TANJUNG BALAI', 'id': 12000, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=12000'},
            {'name': 'KOTA BINJAI', 'id': 12038, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=12038'},
            {'name': 'KOTA TEBING TINGGI', 'id': 12081, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=12081'},
            {'name': 'KOTA PADANG SIDIMPUAN', 'id': 12122, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=12122'},
            {'name': 'KOTA GUNUNGSITOLI', 'id': 7132, 'parent_id': 6728,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7132'}
        ]
        self.assertEqual(administratives, expected_administratives)

    def test_parse_c1_html_kabupaten(self):
        # Kabupaten/Kota 'TAPANULI UTARA' page
        content = Browser.browse_url('https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7438')
        administrative_type, administratives = KpuC1Web.parse_c1_html(content)
        self.assertEqual(administrative_type, 'Kecamatan')
        expected_administratives = [
            {'name': 'TARUTUNG', 'id': 7439, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7439'},
            {'name': 'GAROGA', 'id': 7668, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7668'},
            {'name': 'PANGARIBUAN', 'id': 7645, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7645'},
            {'name': 'SIPAHUTAR', 'id': 7621, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7621'},
            {'name': 'PARMONANGAN', 'id': 7606, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7606'},
            {'name': 'PAGARAN', 'id': 7591, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7591'},
            {'name': 'SIBORONG-BORONG', 'id': 7569, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7569'},
            {'name': 'PURBA TUA', 'id': 7557, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7557'},
            {'name': 'SIMANGUMBAN', 'id': 7548, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7548'},
            {'name': 'PAHAE JAE', 'id': 7534, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7534'},
            {'name': 'PAHAE JULU', 'id': 7514, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7514'},
            {'name': 'SIPOHOLON', 'id': 7499, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7499'},
            {'name': 'ADIAN KOTING', 'id': 7484, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7484'},
            {'name': 'SIATAS BARITA', 'id': 7471, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7471'},
            {'name': 'MUARA', 'id': 7681, 'parent_id': 7438,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7681'}
        ]
        self.assertEqual(administratives, expected_administratives)

    def test_parse_c1_html_kecamatan(self):
        # Kecamatan 'TARUTUNG' page
        content = Browser.browse_url('https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7439')
        administrative_type, administratives = KpuC1Web.parse_c1_html(content)
        self.assertEqual(administrative_type, 'Kelurahan/Desa')
        expected_administratives = [
            {'name': 'PARTALI TORUAN', 'id': 7440, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7440'},
            {'name': 'HUTATORUAN IV', 'id': 7457, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7457'},
            {'name': 'SOSUNGGULON', 'id': 7458, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7458'},
            {'name': 'HUTATORUAN VIII', 'id': 7459, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7459'},
            {'name': 'SIMAMORA', 'id': 7460, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7460'},
            {'name': 'PARBAJU TORUAN', 'id': 7461, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7461'},
            {'name': 'PARBAJU JULU', 'id': 7462, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7462'},
            {'name': 'PARBAJU TONGA', 'id': 7463, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7463'},
            {'name': 'SITAMPURUNG', 'id': 7464, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7464'},
            {'name': 'SIRAJA OLOAN', 'id': 7465, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7465'},
            {'name': 'JAMBUR NAULI', 'id': 7466, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7466'},
            {'name': 'SIHUJUR', 'id': 7467, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7467'},
            {'name': 'PARTALI JULU', 'id': 7468, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7468'},
            {'name': 'HUTATORUAN I', 'id': 7469, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7469'},
            {'name': 'PARBUBU PEA', 'id': 7456, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7456'},
            {'name': 'HUTAGALUNG SIWALUOMPU', 'id': 7455, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7455'},
            {'name': 'AEK SIANSIMUN', 'id': 7454, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7454'},
            {'name': 'HUTATORUAN V', 'id': 7441, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7441'},
            {'name': 'HUTATORUAN VI', 'id': 7442, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7442'},
            {'name': 'HUTATORUAN VII', 'id': 7443, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7443'},
            {'name': 'HUTATORUAN IX', 'id': 7444, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7444'},
            {'name': 'HUTATORUAN X', 'id': 7445, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7445'},
            {'name': 'HUTATORUAN XI', 'id': 7446, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7446'},
            {'name': 'PARBUBU I', 'id': 7447, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7447'},
            {'name': 'PARBUBU II', 'id': 7448, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7448'},
            {'name': 'HUTAPEA BANUAREA', 'id': 7449, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7449'},
            {'name': 'SIANDOR-ANDOR', 'id': 7450, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7450'},
            {'name': 'HUTAURUK', 'id': 7451, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7451'},
            {'name': 'HAPOLTAHAN', 'id': 7452, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7452'},
            {'name': 'PARBUBU DOLOK', 'id': 7453, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7453'},
            {'name': 'HUTATORUAN III', 'id': 7470, 'parent_id': 7439,
             'url': 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7470'}
        ]
        self.assertEqual(administratives, expected_administratives)

    def test_parse_c1_html_kelurahan(self):
        # Kelurahan/Desa 'PARTALI TORUAN' page
        content = Browser.browse_url('https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7440')
        administrative_type, administratives = KpuC1Web.parse_c1_html(content)
        self.assertEqual(administrative_type, None)
        self.assertEqual(administratives, [])
