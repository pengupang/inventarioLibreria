import subprocess

def imprimirPDF(archivo):
    try:
        subprocess.run(['powershell.exe','Start-Process','-FilePath',
                        "{}".format("pdfs/{}.pdf".format(archivo)),"-Verb","Print",
                        "-PassThru"],check=True)
    except Exception as e:
        print("ERROR: {}".format(e))

