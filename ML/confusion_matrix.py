from sklearn.metrics import confusion_matrix

cm = confusion_matrix(true, pred)

tn, tp = cm[0][0], cm[1][1]
fn, fp = cm[1][0], cm[0][1]

sen = tp / (tp+fn)
spe =  tn / (fp+tn)
acc = (tp + tn) / np.sum(cm)

ppv = tp / (tp+fp)
npv = tn / (fn+tn)

