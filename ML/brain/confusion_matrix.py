from sklearn.metrics import confusion_matrix

cm = confusion_matrix(true, pred)

sen = cm[0][0] / (cm[0][1] + cm[1][1])
spe = cm[1][1] / (cm[0][1] + cm[1][1])
acc = (cm[0][0] + cm[1][1]) / np.sum(cm)

