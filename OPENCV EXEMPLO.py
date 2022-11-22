import cv2
#conecta a webcam
webcam = cv2.VideoCapture(0)
#validar se ele leu a informação da webcam e printar o frame
if webcam.isOpened():
    validacao, frame= webcam.read()
    #se a camera funcionar ele vai executar o codigo,caso validacao seja true
    while validacao:
        validacao, frame= webcam.read() #lê
        cv2.imshow("VIDEO DA WEBCAM",frame) #mostra
        key = cv2.waitKey(2) #define quanto tempo ele demora pra mostrar o print(milisegundos)
        if key == 27:  #esc #delimitar um tecla para encerrar
            break
    cv2.imwrite("FotoCam.png",frame) #salva a ultima imagem e coloca em uma aba

webcam.release() #fecha a conexão co a webcam
cv2.destroyAllWindows() #fecha todas as janelas abertas pelo codigo

        
