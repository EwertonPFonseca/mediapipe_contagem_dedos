import cv2
import mediapipe as mp

webcam = cv2.VideoCapture(0)
hand = mp.solutions.hands #config do mp
mao = hand.Hands(max_num_hands= 1) # determinar o número de mãos que o programa reconhecerá

mpDraw = mp.solutions.drawing_utils # desenhar as ligações da mão

while True:
    check, img = webcam.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) #CONVERSAO DO PADRAO BGR PARA RGB
    results = mao.process(imgRGB) # processar a imagem
    handsPoints = results.multi_hand_landmarks # extraindo as coordenadas
    h,w,_ = img.shape #extrai as dimensoes da imagem
    pontos=[]

    if handsPoints: # verifica há uma mão na imagem
        for points in handsPoints: # extrai as coordenadas
            #print(points)
            mpDraw.draw_landmarks(img,points,hand.HAND_CONNECTIONS)

            for id, cord in enumerate(points.landmark):
                cx,cy = int(cord.x*w),int(cord.y*h)
                #cv2.putText(img,str(id),(cx,cy),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
                pontos.append((cx,cy))
                #print(pontos)

        dedos=[8,12,16,20]
        contador =0
        if points:
            if pontos[4][0]<pontos[2][0]: #contador para o polegar
                contador+=1


            for x in dedos:
                if pontos[x][1] <pontos[x-2][1]: #contador para todos os outros dedos
                    contador +=1

        cv2.rectangle(img,(80,10),(200,100),(255,0,0),-1)
        cv2.putText(img,str(contador),(100,100),cv2.FONT_HERSHEY_SIMPLEX,4,(255,255,255),5)

    # mostrar o frame capturado
    cv2.imshow("Video da webcam", img)

     # cadenciar a leitura dos frames- Milissegundos

    tecla = cv2.waitKey(2)

    # comando para parar o código e sair do loop
    if tecla == 27:  # 27 tecla esc - consultar tabela ASCII
        break



# desliga a webcam
webcam.release()

# fecha a janela
cv2.destroyAllWindows()



