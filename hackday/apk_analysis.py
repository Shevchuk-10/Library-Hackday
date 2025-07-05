from zipfile import ZipFile

def list_apk_files(apk_path):
    try:
        with ZipFile(apk_path, 'r') as zip_ref:
            return zip_ref.namelist()
    except Exception as e:
        return [str(e)]
