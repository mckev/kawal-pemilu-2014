import re

import requests_html

from classes.browser import Browser


class KpuC1:
    @staticmethod
    def parse_c1_page(content):
        """
        Parse a C1 page
        Arguments:
            content: HTML string
        Output:
            administrative_type: Type of Administrative Division, i.e. 'Provinsi', 'Kabupaten/Kota', 'Kecamatan', 'Kelurahan/Desa'
            administratives: [{
               'name',
               'id',
               'parent_id',
               'url',
            }, ...]
        """
        html = requests_html.HTML(html=content)

        # On main page: <select class="formfield" name="wilayah_id" onChange="selectCat(this,'0')"><option value="">pilih</option><option  value="1">ACEH</option><option  value="6728">SUMATERA UTARA</option>
        # When selecting Provinsi "SUMATERA UTARA", it will download: https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=0&parent=6728
        # On Provinsi "SUMATERA UTARA": <select class="formfield" name="wilayah_id" onChange="selectCat(this,'6728')"><option value="">pilih</option><option  value="7240">TAPANULI TENGAH</option><option  value="7438">TAPANULI UTARA</option>
        # When selecting Kabupaten/Kota "TAPANULI UTARA", it will download: https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=6728&parent=7438
        # On Kabupaten/Kota "TAPANULI UTARA": <select class="formfield" name="wilayah_id" onChange="selectCat(this,'7438')"><option value="">pilih</option><option  value="7439">TARUTUNG</option><option  value="7668">GAROGA</option>
        # When selecting Kecamatan "TARUTUNG", it will download: https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7438&parent=7439
        # On Kecamatan "TARUTUNG": <select class="formfield" name="wilayah_id" onChange="selectCat(this,'7439')"><option value="">pilih</option><option  value="7440">PARTALI TORUAN</option><option  value="7457">HUTATORUAN IV</option>
        # When selecting Kelurahan/Desa "PARTALI TORUAN", it will download: https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent=7439&parent=7440
        # On Kelurahan/Desa "PARTALI TORUAN": There is no <span> and no <select>

        # Parse: <span class="label">Provinsi :</span>
        html_span_label = html.find(selector='span.label', first=True)
        if html_span_label is None:
            return None, []
        html_span_label_text = html_span_label.text
        administrative_type = html_span_label_text.replace(' :', '')

        # Parse: <select class="formfield" name="wilayah_id" onChange="selectCat(this,'6728')">
        html_select = html.find(selector='select.formfield', first=True)
        assert html_select.attrs['name'] == 'wilayah_id'
        assert html_select.attrs['class'] == ('formfield',)
        html_select_onchange = html_select.attrs['onchange']
        matches = re.match(r'^selectCat\(this,\'(\d+)\'\)$', html_select_onchange)
        if not matches:
            raise Exception('Cannot parse onChange="{}"'.format(html_select_onchange))
        parent_id = int(matches.group(1))

        # Parse: <option  value="1">ACEH</option><option  value="6728">SUMATERA UTARA</option>
        administratives = []
        html_select_options = html_select.find(selector='option')
        for html_select_option in html_select_options:
            if html_select_option.attrs['value'] == '':
                # Ignore 'pilih'
                continue
            option_value = int(html_select_option.attrs['value'])
            option_name = html_select_option.text
            url = 'https://pilpres2014.kpu.go.id/c1.php?cmd=select&grandparent={}&parent={}'.format(parent_id,
                                                                                                    option_value)
            administrative = {
                'name': option_name,
                'id': option_value,
                'parent_id': parent_id,
                'url': url
            }
            administratives.append(administrative)
        return administrative_type, administratives

    @staticmethod
    def browse_c1_page(url):
        content = Browser.browse_url(url)
        administrative_type, administratives = KpuC1.parse_c1_page(content)
        for administrative in administratives:
            url = administrative['url']
            print('Browsing {} {} - id {}, parent_id {}'.format(administrative_type, administrative['name'],
                                                                administrative['id'], administrative['parent_id']))
            KpuC1.browse_c1_page(url)
