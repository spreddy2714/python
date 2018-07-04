import numpy as np
import pandas as pd
import vobject

contactsdf = pd.read_excel('Team.xlsx')
contactsdf.drop(['Sl No'],  axis=1, inplace=True)

for index, row in contactsdf.iterrows():
    word_list = row["Name"].split()
    print(word_list[0], word_list[-1], row["Email ID"], row['Mobile'])
    word_list = row["Name"].split()
    v = vobject.vCard()
    v.add('n')
    v.n.value = vobject.vcard.Name(family=word_list[-1], given=word_list[0])
    v.add('fn')
    v.fn.value = "%s %s" % (word_list[0], word_list[-1])
    v.add('email')
    v.email.value = row['Email ID']
    v.add('tel')
    v.tel.value = str(row['Mobile'])
    v.tel.type_param = 'WORK'
    output = v.serialize()
    file = open('D:/Contacts\\' +word_list[0] + ' ' + word_list[-1] + '.vcf','w')
    file.write(output)
    file.close()
