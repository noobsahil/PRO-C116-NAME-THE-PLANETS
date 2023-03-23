import cv2

img = cv2.imread("solar-system.jpg")


cv2.putText(img, "Sun", (110, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
cv2.putText(img, "Mercury", (100, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, "Venus", (190, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, "Earth", (300, 270), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, "Mars", (400, 280), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, "Jupiter", (580, 400), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, "Saturn", (810, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, "Uranus", (960, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img, "Neptune", (1120, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2, cv2.LINE_AA)

cv2.imshow("output", img)

cv2.waitKey(0)

cv2.imwrite("Solar_systemwithname.jpg", img)
