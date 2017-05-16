# any()

ostree = 'download-node-02.eng.bos.redhat.com/released/RHEL-7/7.3/Server/ppc64/os/'
archlist = ['RHEL', 'Pegas']
if any(i for i in archlist if i in ostree):
    print('hello world')

'''
如果RHEL或Pegas在ostree中，则输出hello world
'''
