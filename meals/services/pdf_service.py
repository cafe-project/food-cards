import os
# from wsgiref.util import FileWrapper

# import pdfkit
import platform
import subprocess
from wsgiref.util import FileWrapper

import pdfkit
from django.http import HttpResponse

from bottle import template


class PdfService:
    def _get_pdfkit_config(self):
        """wkhtmltopdf lives and functions differently depending on Windows or Linux. We
         need to support both since we develop on windows but deploy on Heroku.

        Returns:
            A pdfkit configuration
        """
        if platform.system() == 'Windows':
            return pdfkit.configuration(wkhtmltopdf=os.environ.get('WKHTMLTOPDF_BINARY',
                                                                   'C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe'))
        else:
            WKHTMLTOPDF_CMD = subprocess.Popen(['which', os.environ.get('WKHTMLTOPDF_BINARY', 'wkhtmltopdf')],
                                               stdout=subprocess.PIPE).communicate()[0].strip()
            return pdfkit.configuration(wkhtmltopdf=WKHTMLTOPDF_CMD)

    def make_pdf_from_raw_html(self, html, filename: str, options=None):
        """Produces a pdf from raw html.
        Args:
            html (str): Valid html
            options (dict, optional): for specifying pdf parameters like landscape
                mode and margins
        Returns:
            pdf of the supplied html
        """
        return pdfkit.from_string(html, filename, configuration=self._get_pdfkit_config(), options=options)

    def generate_pdf(self, meal, user):
        info = {'company_name': 'company_name',
                'card_number': meal.card_number,
                'meal_name': meal.name,
                'recipe_number': meal.code,
                'notes': meal.notes,
                'describe': meal.describe,
                'storage': meal.storage,
                'serving': meal.serving,
                'expiry': meal.expiry,
                }


        result = template('templates/sample.html', info)
        result += self.generate_table(meal)
        result += template('templates/footer1.html', info)
        filename = f'_{meal.code}.pdf'
        pdf_status = self.make_pdf_from_raw_html(result, filename=filename)

        assert pdf_status, "PDF was not generated."

        try:
            wrapper = FileWrapper(open(filename, 'rb'))
            response = HttpResponse(wrapper, content_type='application/force-download')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(filename)
            return response
        except Exception as e:
            return None
    #
    def generate_table(self, meal):
        info = {
            'name': 'Pavadinimas',
            'bruto': 'Bruto',
            'neto': 'Neto',
            'proteins': 'Baltymai',
            'fats': 'Riebalai',
            'carbs': 'Angliavandeniai',
            'kcal': 'Kcal',
        }
        table = '<table cellspacing="0" cellpadding="2">'
        table += template('templates/product1.html', info)

        for product in list(meal.products.all()):
            info = {
                'name': product.name,
                'bruto': product.bruto or 0,
                'neto': product.neto or 0,
                'proteins': product.proteins or 0,
                'fats': product.fats or 0,
                'carbs': product.carbs or 0,
                'kcal': product.calories or 0,
            }
            row = template('templates/product1.html', info)

            table += row
        info = {
            'name': 'Viso',
            'bruto': meal.bruto or 0,
            'neto': meal.neto or 0,
            'proteins': meal.proteins or 0,
            'fats': meal.fats or 0,
            'carbs': meal.carbs or 0,
            'kcal': meal.calories or 0,
        }
        table += template('templates/product1.html', info)
        table += '</table>'
        return table



