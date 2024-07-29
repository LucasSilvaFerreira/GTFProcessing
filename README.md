# GTFProcessing
GTFProcessing class using the gtf parse tool
```
!pip uninstall GTFProcessing -y
!pip install git+https://github.com/LucasSilvaFerreira/GTFProcessing.git
```
```python

from GTFProcessing import GTFProcessing
gtf = GTFProcessing('hg19.refGene.gtf')
df_gtf_refseq = gtf.get_gtf_df()

```
