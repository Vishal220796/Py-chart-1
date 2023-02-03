import matplotlib.pyplot as plt


activities = ['Science', 'Math', 'Computers', 'Marathi', 'Hindi','English Literature']


slices = [4,6,9,8,2,7]


colors = ['aqua', 'red', 'yellow', 'navy', 'silver', 'green']


plt.pie(slices, labels = activities, colors=colors,
        startangle=30, shadow = True, explode = (0,0,0,0,0,0.2),
        radius = 1.2, autopct = '%3.3f%%')


plt.legend()


plt.show()