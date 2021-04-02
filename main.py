import os



path = "C:\\Unreal Projects"


#print(os.listdir(path))
#for j in path[-1::-1]:
 #   print(j)

def get_distinct_suff(path, suff_set = set()):
    file_list = os.listdir(path)
    if file_list != []:
        for i in file_list:
            if os.path.isfile(path + '\\' + i):
                file_suff = ""
                for j in i[-1::-1]:
                    if j == '.':
                        suff_set.add(file_suff[-1::-1])
                        break
                    file_suff += j
            if os.path.isdir(path + '\\' + i):
                dir_set = get_distinct_suff(path + '\\' + i, suff_set)
                if type(dir_set) is set:
                    suff_set.update(dir_set)
        return suff_set

distinct_names = get_distinct_suff(path)
print(distinct_names)
print(len(distinct_names))