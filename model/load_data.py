import pandas as pd
import urllib.request
import zipfile



def extract_zip(src, dst, member_name):
    """
    Extract a member file from a zip file and read it into pandas DataFrame
    Args: 
        src (str): URL of the zip file to be downloaded and extracted
        dst (str): Local file path where the zip file will be written
        member_name (str): Name of the member file inside the zip file to be read into a DataFrame
    Returns:
        pandas.DataFrame: DataFrame containing the contents of the member file
    """
    url = src
    frame = dst
    fin = urllib.request.urlopen(url)
    data = fin.read()

    with open (dst, mode="wb") as fout:
        fout.write(data)
    with zipfile.ZipFile(dst) as z:
        kag = pd.read_csv(z.open(member_name))
        kag_questions = kag.iloc[0]
        raw = kag.iloc[1:]
        return raw
    
