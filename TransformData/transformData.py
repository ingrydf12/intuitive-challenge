import pdfplumber
import csv
import os
import zipfile
from pathlib import Path
import re

# Classe de anexo, pode ser mais perfomático isso
class AnexoIProcessor:  
    def __init__(self, input_dir="WebScraping/downloads", output_dir="transformedData"):
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.pdf_file = "Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"
        self.full_path = os.path.join(self.input_dir, self.pdf_file)
        
        self.table_settings = {
            "vertical_strategy": "lines",
            "horizontal_strategy": "text",
            "intersection_y_tolerance": 10,
            "snap_tolerance": 3,
            "join_tolerance": 3,
            "edge_min_length": 15
        }
        
        # As abreviações presente nas tabelas do arquivo
        self.abbreviations = {
            'OD': 'Odontológico',
            'AMB': 'Ambulatorial',
            'HOSP': 'Hospitalar',
            'SADT': 'Serviço Auxiliar de Diagnóstico e Terapia',
            'MR': 'Materiais',
            'SP': 'Serviços Profissionais',
            'UX': 'Urgência/Emergência'
        }
        
        self.clean_patterns = [
            (r'\s+', ' '),
            (r'\n', ' '),
        ]

# Validação de arquivo PDF na pasta
    def _validate_file(self):
        if not os.path.exists(self.full_path):
            raise FileNotFoundError(f"Arquivo {self.pdf_file} não encontrado em {self.input_dir}")
        
        print(f"Arquivo validado: {self.pdf_file}")

    def _clean_text(self, text):
        if not text or not isinstance(text, str):
            return ""
            
        text = text.strip()
        for pattern, replacement in self.clean_patterns:
            text = re.sub(pattern, replacement, text)
        return text


    def extract_data(self):
        self._validate_file()
        processed_data = []
        total_pages = 0
        total_tables = 0
        total_rows = 0
        
        print(f"\nIniciando extração de dados de {self.pdf_file}...")
        
        try:
            with pdfplumber.open(self.full_path) as pdf:
                total_pages = len(pdf.pages)
                print(f"Total de páginas para processar: {total_pages}")
                
                for page_num, page in enumerate(pdf.pages, 1):
                    try:
                        page = page.crop(page.bbox) if hasattr(page, 'bbox') else page
                        
                        tables = page.extract_tables(self.table_settings)
                        if not tables:
                            continue
                            
                        for table_num, table in enumerate(tables, 1):
                            for row in table:
                                if any(cell is not None for cell in row):
                                    processed_row = self._process_row(row)
                                    if processed_row:
                                        processed_data.append(processed_row)
                                        total_rows += 1
                            total_tables += 1
                            
                        print(f"Página {page_num}: {len(tables)} tabelas extraídas", end='\r')
                        
                    except Exception as page_error:
                        print(f"\nErro na página {page_num}: {str(page_error)}")
                        continue
            
            print(f"\n\nExtracção concluída:")
            print(f"- Páginas processadas: {total_pages}")
            print(f"- Tabelas extraídas: {total_tables}")
            print(f"- Quantidade de registros: {total_rows}")
            
            if not processed_data:
                raise ValueError("Nenhum dado válido foi extraído do arquivo")
                
            return processed_data
            
        except Exception as e:
            print(f"\nFalha crítica na extração: {str(e)}")
            return None

# Processa cada linha dentro da tabela
    def _process_row(self, row):
        processed_cells = []
        for cell in row:
            content = self._clean_text(str(cell)) if cell is not None else ""
            
            for abbrev, full_text in self.abbreviations.items():
                content = content.replace(abbrev, full_text)
                
            processed_cells.append(content)
            
        return processed_cells if any(processed_cells) else None

    # Salva os dados recebidos
    def save_results(self, data):
        if not data:
            print("Nenhum dado válido para salvar.")
            return False
            
        Path(self.output_dir).mkdir(parents=True, exist_ok=True)
        
        csv_filename = "Rol_de_Procedimentos_Anexo_I.csv"
        zip_filename = "Teste_Ingryd_Cordeiro_Duarte.zip"
        
        csv_path = os.path.join(self.output_dir, csv_filename)
        zip_path = os.path.join(self.output_dir, zip_filename)
        
        try:
            print("\nSalvando resultados...")
            
            # Salva CSV com encoding UTF-8 e delimitador seguro
            with open(csv_path, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f, delimiter=';', quoting=csv.QUOTE_MINIMAL)
                writer.writerows(data)
            
            # Cria ZIP com compactação máxima
            with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED, compresslevel=9) as zipf:
                zipf.write(csv_path, arcname=csv_filename)
            
            # Remove CSV temporário
            os.remove(csv_path)
            
            # Verificacao de resultado com tamanho
            if os.path.exists(zip_path):
                print("\nProcessamento concluído com sucesso!")
                print(f"Arquivo gerado: {zip_path}")
                print(f"Tamanho: {os.path.getsize(zip_path)/1024:.2f} KB")
                return True
            else:
                raise RuntimeError("O arquivo ZIP não gerado")
                
        except Exception as e:
            print(f"\nErro ao salvar: {str(e)}")
            return False

def main():
    try:
        print("Inicializando transformData")
        
        processor = AnexoIProcessor()
        
        print("\nFASE 1: Extração de dados")
        processed_data = processor.extract_data()
        
        if processed_data:
            print("\nFASE 2: Geração de arquivos")
            success = processor.save_results(processed_data)
            
            if not success:
                print("\nO processamento foi concluído com problemas.")
        
    except Exception as e:
        print(f"\nERRO: - {str(e)}")

if __name__ == "__main__":
    main()