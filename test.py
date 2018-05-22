
link_dic= {
}

file = open('5GB.txt','r')
lines = file.readlines()
for line in lines:
    islink = line in link_dic.keys()
    if islink:
        link_dic[line] +=1
    else:
        link_dic.update({line:1})

# for key in link_dic.keys():
#     if '\n' in key:
#         key.replace('\n','')
for key,value in link_dic.items():
    print('{} -> {}'.format(key,value))