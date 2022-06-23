data = d.split(',')
        row=[]
        row += d.split(',')

        print("entree boucle")
        with open('test2.csv', 'w') as fp:
            writer = csv.writer(fp, delimiter=',')
            for k in row:
                writer.writerow([i for i in k])
        print("fin ?")
        print(row)