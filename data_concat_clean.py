import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# load all data
meta_huttenhower = pd.read_csv("C:/Users/talno/microbiom_project/ibd_huttenhower_results/ibd_huttenhower.metadata.txt",sep='\t')
ibd_huttenhower = pd.read_csv("C:/Users/talno/microbiom_project/ibd_huttenhower_results/RDP/ibd_huttenhower.otu_table.100.denovo.rdp_assigned",sep='\t')

ibd_gevers = pd.read_csv("C:/Users/talno/microbiom_project/ibd_gevers_2014_results/RDP/ibd_gevers_2014.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_gevers = pd.read_csv("C:/Users/talno/microbiom_project/ibd_gevers_2014_results/ibd_gevers_2014.metadata.txt",sep='\t')
meta_gevers.rename(columns={"sample": "#SampleID"}, inplace=True)

ibd_youngster = pd.read_csv("C:/Users/talno/microbiom_project/cdi_youngster_results/cdi_youngster_results/RDP/cdi_youngster.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_youngster = pd.read_csv("C:/Users/talno/microbiom_project/cdi_youngster_results/cdi_youngster_results/cdi_youngster.metadata.txt",sep='\t')
meta_youngster.rename(columns={"#Sample_id": "#SampleID"}, inplace=True)

ibd_schubert = pd.read_csv("C:/Users/talno/microbiom_project/cdi_schubert_results/RDP/cdi_schubert.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_schubert = pd.read_csv("C:/Users/talno/microbiom_project/cdi_schubert_results/cdi_schubert.metadata.txt",sep='\t', encoding= 'unicode_escape')
meta_schubert.rename(columns={"sample_id": "#SampleID"}, inplace=True)

ibd_asd = pd.read_csv("C:/Users/talno/microbiom_project/asd_son_results/RDP/asd_son.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_asd = pd.read_csv("C:/Users/talno/microbiom_project/asd_son_results/asd_son.metadata.txt",sep='\t')
meta_asd.rename(columns={"Library_Name_s": "#SampleID"}, inplace=True)

ibd_vincent = pd.read_csv("C:/Users/talno/microbiom_project/cdi_vincent_v3v5_results/RDP/cdi_vincent_v3v5.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_vincent = pd.read_csv("C:/Users/talno/microbiom_project/cdi_vincent_v3v5_results/cdi_vincent_v3v5.metadata.txt",sep='\t')
meta_vincent.rename(columns={"Unnamed: 0": "#SampleID"}, inplace=True)

ibd_autism = pd.read_csv("C:/Users/talno/microbiom_project/autism_kb_results/RDP/autism_kb.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_autism = pd.read_csv("C:/Users/talno/microbiom_project/autism_kb_results/autism_kb.metadata.txt",sep='\t')
meta_autism.rename(columns={"#Sample ID": "#SampleID"}, inplace=True)

ibd_ross = pd.read_csv("C:/Users/talno/microbiom_project/ob_ross_results/RDP/ob_ross.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_ross = pd.read_csv("C:/Users/talno/microbiom_project/ob_ross_results/ob_ross.metadata.txt",sep='\t')
meta_ross.rename(columns={"sampleID": "#SampleID"}, inplace=True)


ibd_zupancic = pd.read_csv("C:/Users/talno/microbiom_project/ob_zupancic_results/RDP/ob_zupancic.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_zupancic = pd.read_csv("C:/Users/talno/microbiom_project/ob_zupancic_results/ob_zupancic.metadata.txt",sep='\t')
meta_zupancic.rename(columns={"Unnamed: 0": "#SampleID"}, inplace=True)

# ibd_scheperjans = pd.read_csv("C:/Users/talno/microbiom_project/par_scheperjans_results/RDP/par_scheperjans.otu_table.100.denovo.rdp_assigned",sep='\t')
# meta_scheperjans = pd.read_csv("C:/Users/talno/microbiom_project/par_scheperjans_results/par_scheperjans.metadata.txt",sep='\t')
# meta_scheperjans.rename(columns={"sample_accession": "#SampleID"}, inplace=True)

ibd_littman = pd.read_csv("C:/Users/talno/microbiom_project/ra_littman_results/RDP/ra_littman.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_littman = pd.read_csv("C:/Users/talno/microbiom_project/ra_littman_results/ra_littman.metadata.txt",sep='\t')


ibd_alkanani = pd.read_csv("C:/Users/talno/microbiom_project/t1d_alkanani_results/RDP/t1d_alkanani.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_alkanani = pd.read_csv("C:/Users/talno/microbiom_project/t1d_alkanani_results/t1d_alkanani.metadata.txt",sep='\t')
meta_alkanani.rename(columns={"Lib": "#SampleID"}, inplace=True)

ibd_mejialeon = pd.read_csv("C:/Users/talno/microbiom_project/t1d_mejialeon_results/RDP/t1d_mejialeon.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_mejialeon = pd.read_csv("C:/Users/talno/microbiom_project/t1d_mejialeon_results/t1d_mejialeon.metadata.txt",sep='\t')

ibd_xiang = pd.read_csv("C:/Users/talno/microbiom_project/crc_xiang_results/RDP/crc_xiang.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_xiang = pd.read_csv("C:/Users/talno/microbiom_project/crc_xiang_results/crc_xiang.metadata.txt",sep='\t')

ibd_zackular = pd.read_csv("C:/Users/talno/microbiom_project/crc_zackular_results/RDP/crc_zackular.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_zackular = pd.read_csv("C:/Users/talno/microbiom_project/crc_zackular_results/crc_zackular.metadata.txt",sep='\t', encoding= 'unicode_escape')
meta_zackular.rename(columns={"sample_id": "#SampleID"}, inplace=True)

ibd_zeller = pd.read_csv("C:/Users/talno/microbiom_project/crc_zeller_results/RDP/crc_zeller.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_zeller = pd.read_csv("C:/Users/talno/microbiom_project/crc_zeller_results/crc_zeller.metadata.txt",sep='\t', encoding= 'unicode_escape')
meta_zeller.rename(columns={"Subject ID": "#SampleID"}, inplace=True)

ibd_zhao = pd.read_csv("C:/Users/talno/microbiom_project/crc_zhao_results/RDP/crc_zhao.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_zhao = pd.read_csv("C:/Users/talno/microbiom_project/crc_zhao_results/crc_zhao.metadata.txt",sep='\t')

ibd_singh = pd.read_csv("C:/Users/talno/microbiom_project/edd_singh_results/RDP/edd_singh.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_singh = pd.read_csv("C:/Users/talno/microbiom_project/edd_singh_results/edd_singh.metadata.txt",sep='\t')
meta_singh.rename(columns={"SampleID": "#SampleID"}, inplace=True)

ibd_dinh = pd.read_csv("C:/Users/talno/microbiom_project/hiv_dinh_results/RDP/hiv_dinh.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_dinh = pd.read_csv("C:/Users/talno/microbiom_project/hiv_dinh_results/hiv_dinh.metadata.txt",sep='\t')
meta_dinh.rename(columns={"Sample_Name_s": "#SampleID"}, inplace=True)

ibd_lozupone = pd.read_csv("C:/Users/talno/microbiom_project/hiv_lozupone_results/RDP/hiv_lozupone.otu_table.100.denovo.rdp_assigned",sep='\t')
meta_lozupone = pd.read_csv("C:/Users/talno/microbiom_project/hiv_lozupone_results/hiv_lozupone.metadata.txt",sep='\t')
meta_lozupone.rename(columns={"new_sample_name": "#SampleID"}, inplace=True)

def drop_features(data):
    result = data.copy()
    result['total'] = result.apply(lambda x: (x > 0).sum(), axis=1)
    result['total'] = result['total']/result['total'].sum()
    result = result[result['total'] > 0]
    result.drop('total',axis=1)
    return result


all_ibds = [ibd_huttenhower, ibd_gevers, ibd_youngster, ibd_schubert, ibd_asd,ibd_vincent,ibd_autism,ibd_ross, ibd_littman, ibd_alkanani, ibd_mejialeon,ibd_xiang, ibd_zackular, ibd_zeller, ibd_zhao, ibd_singh, ibd_dinh, ibd_lozupone]
all_metas = [meta_huttenhower, meta_gevers, meta_youngster, meta_schubert, meta_asd, meta_vincent,meta_autism,meta_ross, meta_littman, meta_alkanani, meta_mejialeon, meta_xiang, meta_zackular, meta_zeller, meta_zhao, meta_singh, meta_dinh, meta_lozupone]
names =  ["huttenhower", "gevers", "youngster", "schubert", "asd", "vincent" , "autism" ,"ross", "littman" , "alkanani", "mejialeon", "xiang", "zackular", "zeller", "zhao", "singh", "dinh", "lozupone"]

# arrange the otu with disease state and where from and take just what appears in the meta data
def clean(meta,ibd,name):
    
    otu = ibd.copy()
    otu["taxon_g"] = otu["Unnamed: 0"].str.split(';', expand=True)[5]
    otu["taxon_f"] = otu["Unnamed: 0"].str.split(';', expand=True)[4]
    otu = otu.groupby(["taxon_f", "taxon_g"]).sum()
    try:
        otu.drop(('f__', 'g__'), inplace=True)
    except Exception:
        print("no g__, f__")
    otu = otu /otu.sum(axis = 0)
    otu.fillna(0,inplace=True)
    otu = otu.T
    meta.set_index("#SampleID", inplace=True)
    keepsmpls = [i for i in otu.index if i in meta.index]
    otu = otu.loc[keepsmpls]
    meta = meta.loc[keepsmpls]
    otu = otu.join(meta.DiseaseState)
    otu.loc[:, "DiseaseState"] = otu.loc[:, "DiseaseState"].map(
        {"ASD": "D", "nonCDI": "H", "nonIBD": "H", "CD": "D", "UC": "D", "CDI": "D", "H": "H", "postFMT_CDI": "H",
         "ASD": "D", 'HIV': "D", 'EDD': "D", "CRC": 'D', 'OB': "D", 'PAR': "D", "OW": "D", "CIRR": "D", "MHE": "D",
         "nonCRC": "H", "RA": "D", "T1D": "D", "CRC": "D"})
    otu["From"] = name
    return otu

fixed = []
for ibd, meta, name in zip(all_ibds, all_metas, names):
       fixed.append(clean(meta,ibd,name))
finish_data = pd.concat(fixed)
finish_data.fillna(0,inplace=True)
finish_data.reset_index(drop=True, inplace=True)    
finish_data.to_csv("cleaned_microbiomeHD")

#american clean
start = "C:/Users/talno/microbiom_project/american_gut/"
data_americans = pd.read_csv(start + "feature_table_gtdb.tsv", sep='\t')
data_americans.drop('ID',inplace=True, axis=1)
data_americans["taxon_g"] = data_americans['taxon'].str.split(';', expand=True)[5]
data_americans["taxon_f"] = data_americans['taxon'].str.split(';', expand=True)[4]
data_americans = data_americans.groupby(['taxon_f', "taxon_g"]).sum()
data_americans.drop(('f__', 'g__'), inplace=True)
data_americans = data_americans/data_americans.sum(axis=0)
data_americans.fillna(0,inplace=True)
data_americans = data_americans.T
data_americans.drop('g__',inplace=True, axis=1)
data_americans.to_csv("cleaned_Americans")
