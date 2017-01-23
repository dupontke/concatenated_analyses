##!/mnt/lustre_fs/users/mjmcc/apps/python2.7/bin/python
##!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

sel = []
sel.append(['protein','protein and not name H*'])
sel.append(['aligment_confirmed','protein and name CA and (resid 68:73 or resid 91:96 or resid 117:120 or resid 135:138 or resid 171:175 or resid 197:199 or resid 211:214)'])
sel.append(['gtp','resname GTP and not name H*'])
sel.append(['Mg','resname MG and not name H*'])
sel.append(['sah','resname SAH and not name H*'])

#sel.append(['region_31-57','protein and resid 31:57 and not name H*'])
#sel.append(['ah_31-41','protein and resid 31:41 and not name H*'])
#sel.append(['loop_41-49','protein and resid 42:49 and not name H*'])
#sel.append(['ah_50-62','protein and resid 50:62 and not name H*'])
#sel.append(['loop_98-108','protein and resid 98:108 and not name H*'])
#sel.append(['loop_99-104','protein and resid 99:104 and not name H*'])
#sel.append(['rest_of_protein','protein and (resid 1:30 or resid 58:98 or resid 105:257) and not name H*'])
