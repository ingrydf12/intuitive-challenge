import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from config import CONFIG
from zipfile import ZipFile, ZIP_DEFLATED

class compactPDFFiles:
    def __init__(self):
        self.base_folder = os.path.dirname(os.path.abspath(__file__))
        self.urlSite = CONFIG['site_url']
        self.file_extension = CONFIG['file_extension'].lower()
        self.download_folder = os.path.join(self.base_folder, CONFIG['folderDownloadName'])
        self.prefix = CONFIG['prefix']
        
        os.makedirs(self.download_folder, exist_ok=True)
        print(f"Pasta de download criada em: {self.download_folder}")
    
    # Validação se o arquivo é pdf que começa com "Anexo"
    def validateArchive(self, file_url):
        if not file_url:
            return False
            
        filename = os.path.basename(file_url).lower()
        
        return (filename.endswith(self.file_extension) and 
                filename.startswith(self.prefix.lower()))
        
    # Baixa o arquivo
    def downloadArchive(self, file_url):
        try:
            file_url = urljoin(self.urlSite, file_url)
            
            filename = os.path.basename(file_url)
            filepath = os.path.join(self.download_folder, filename)

            headers = {
                'User-Agent': CONFIG.get('user_agent', 'Mozilla/5.0'),
                'Accept': 'application/pdf'
            }
            
            response = requests.get(file_url, headers=headers, stream=True, timeout=10)
            response.raise_for_status()
                        
            with open(filepath, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                
            print(f"Arquivo baixado com sucesso: {filepath}")
            return True
                
        except Exception as e:
            print(f"Erro ao baixar o arquivo: {e}")
            return False
    
    # MARK: Baixa os arquivos puxando as funções
    def downloadProcess(self):
        try:
            headers = {
                'User-Agent': CONFIG.get('user_agent', 'Mozilla/5.0'),
                'Accept': 'text/html'
            }
            
            response = requests.get(self.urlSite, headers=headers, timeout=10)
            response.raise_for_status()
        
        # Lê o conteúdo de links da página
            soup = BeautifulSoup(response.text, 'html.parser')
            paths = soup.find_all('a', href=True)
                        
            download_count = 0
            for path in paths:
                # E aqui ele pega o href
                href = path.get('href', '').strip()
                if self.validateArchive(href):
                    if self.downloadArchive(href):
                        download_count += 1
            
            print(f"Total de arquivos baixados: {download_count}")
            
        except Exception as e:
            print(f"Erro no processo de download: {e}")
    
    # MARK: Transforma a pasta em ZIP
    def compactFiles(self):
        nomeArquivo = os.path.join(self.base_folder, 'Anexos.zip')

        try:
            print(f"Compactando arquivos da pasta {self.download_folder} em {nomeArquivo}")

            with ZipFile(nomeArquivo, 'w', ZIP_DEFLATED) as arquivoZipado:
                #Pega cada arquivo dentro da pasta
                for nome in os.listdir(self.download_folder):
                    #Junta o arquivo com o caminho da pasta
                    caminhoArquivo = os.path.join(self.download_folder, nome)
                    #Verifica se é um arquivo
                    if os.path.isfile(caminhoArquivo): 
                        arquivoZipado.write(caminhoArquivo, nome)

            print("Arquivos zipados com sucesso!")
        except Exception as e:
            print(f"Erro ao compactar os arquivos: {e}")

if __name__ == '__main__':
    downloader = compactPDFFiles()
    downloader.downloadProcess()
    downloader.compactFiles()