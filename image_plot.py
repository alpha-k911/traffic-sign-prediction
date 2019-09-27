plt.figure(figsize=(10,10))
for i in range(25):
    plt.subplot(5,5,i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(x[(i+1)*5], cmap=plt.cm.binary)
#     plt.xlabel(class_names[x[i]])
plt.show()
