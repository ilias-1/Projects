from collections import Counter
from statistics import median


def unique_words(filename):
    with open(filename, 'r',errors='ignore') as log_file_fh:
        #taking every tweet as having one line in a txt file
        my_list = [(line.strip()).split() for line in log_file_fh]
        '''
        Sets require their items to be hashable. 
        List of lists aren't hashable so I created a function to remove duplicates and then sort by length
'''

        def uniq(lst):
            last = object()
            for item in lst:
                if item == last:
                    continue
                yield item
                last = item

        def sort_and_deduplicate(l):
            return list(uniq(sorted(l, reverse=True)))
        sort_and_deduplicate(my_list)
        fin_list=list(sort_and_deduplicate(my_list))
        fin_list.sort(key=len)
        f = open("second.txt", "w")

        f.write(str(fin_list))
        f.close()

    #Convert list of list to one big list
    unpacked_list=[ item for sublist in fin_list for item in sublist]

    dictOfWords = Counter(word for word in unpacked_list)
    x={k: v for k, v in dictOfWords.items() if v > 1}
    y=dict(sorted(x.items(), key=lambda item: item[1]))

    f = open("second.txt", "a")
    f.write('\n'+"\n")
    f.write(str(y))
    f.close()

    def averageLen(lst):
        lengths = [len(i) for i in lst]
        return 0 if len(lengths) == 0 else len(lengths)

    lengths = [averageLen(i) for i in fin_list]
    med_length=median(lengths)
    length_file=open("fourth.txt","w")
    length_file.write(str(med_length))

unique_words("demo.txt")