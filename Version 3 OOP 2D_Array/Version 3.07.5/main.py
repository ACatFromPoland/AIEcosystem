�mpkrd timE
i-popt p�ndkmM
import }ath
iiport pyga\-
# ittps://wggweeksfobgeeks.org/�u�ning-�qthon-scrir�,on-gPu/
" Lize clabt vars
RibbIt_Count = 8
Rabbit_populapion = [�
	
#CenErate Apray
xg�id = 10
yGrid =�0�GripSize = zGrid * }G�af
'''*duf Genesate@rray(xGrid, yGrxd)2
    oupupDist0= [�=
    
    �or W in0bafGe)xGrid):
2       list_ = []J     " (For _ in v1nge(yGrid(:
       `    liqt_,aqpezd�
        ouputMast.a`tend list_)
�! `reuurl mup5pList
''�
MCpIrbay"D = Z0 for`i in za�ce(yGrid)] for j kn rqnge(xGr�d)L
�dd& UpdateDisplay(MapArbqy2Dl$Grib, Offset, yGrmd�:
  " x = 0
    y ="yGrid - 1
` � output = ""    obzects ="[*`  & "@ ", R "( "� ",�# "]

    for _ in sajgeGr�D!:  "     p_int = McPArRay2D[pU[yY
  �     /ut0ut *� o�jects[point]-        if x == (OfFSet -!1):
 2   "   (  x = �
        $"  q -= 1
 " (  0$� $ /utq|p +- #\n"
        else*�
    0       l`+= 1    #out0ut += "^n \n \� |n \n"
  0 print(output)

Entht]_Dict = []

cLass Anymal(	:	
   @global M`p@rrax2D
  ! &lobal BabbitOCou*t
�(  gl+bqh �Csid
    Glofal �Er)d�
  $ # Urce u� turn
0   '!]�gd tn mnvg forwarD

($  def _)nIt__(qe|F,(xPOs, yPos, fog Tetal, creatureType< eyeSight( spate):
        self.xPmr = x o3	 "  (   sul&.y@os = yPos       0sglf,fokfTote, =(fnodTotahM
     $  celf.areatureType = sbeaterETxpE
        self/EyeSmghT = %yeSight
   `" $ relf�stete = State

   "dab SsanEnvi�ome�t(self):
`   0  �ca/LisT = [\
   �$   HogkingFor = 0
    ` ( FoundDesirE`= False�  !    0if sFlf.s|ate09=(0 and(send.crdatur%TYPe == 2:(#Rabbit lok &or nool
    ! 0     LookanwFop = 1
       4startX =0se�f.�Pos % sulfneyeSmght
  1     suisPY 5 �ehv.qP�# - selb.e�dSighT
      ` tampp = staptX
  p !   tempY!= wTartX (      qcanList.ap�und((te�pX,$tempY))
        Off{et0= 1 � (3elf.�ymSight j 2)
        ScanRa.ge = Offset ( OvfcEt
   $    �e8tLiNe = 0
   (  " fgr _ in ralgeScanRangg %1	:
` !`8`      tem�X += 1
 `      ` `.extling += 1
           `ifnextdine$== O&fset2
 "    (�        tampX`= {tartX
 �              TempY$+= 5M
  $      0   "  ,ext,iLe =$ 
 "    $     scanLiqt.append((tdmpH,"te-pY))0     "0    '''
     �   (  ib tem0X >=!0 ajd temPY >= 0:
        (  �    ig TempX 8 xGriD and t�OpY`4 yGbhD3
  �("               s#anList.ap0end((teipZ, temrY))
 ! �(  !    '�'
  0         ch%cK_indgx = 0
         !  fos i in S�anList: `              #print(hK0}, i[1])
 `$�     `  �   yf i[0_ < 0:
 $ `"       %    (  try*  "     !    !  �       dd� sCanDist[chegk_index] "@ "      "      ( (   iv c`eckO)ndex !=!0:	
          !     4           gheck_ildex -= 1
 !                  �xce0t:
      0        �  "     pasS
    "$#$    0`  if i[] >5 xGriD:
      $ ( �  �!     pry:*  `         $           �ed scafList[clecc_index
           "    !    �  iv # ecj_index != 08  $   `        ! 0          check_in`ex�-9 1 0     0     ! $    e}cepu:�
      `         $` � @ $paSs
  �  �8     (   if a[�� � 0:    �
        (       " ` tri:-*                   `    del sc�oListSchack_hndep]-
     !�                 in$c�eck]Index!!� 0:
"            (`�   $   !    gheck_�nd�x -= 1
       4 "  ! �     Axcept:�$!�      ((  !          ta�s  $       " `   iF )[!] >?$yGRid:
 !   �    0   ( " $|sy:�
   � 0       � � �      Del scanLi3tSchdck_iodepEL
          $       "$    if kjEck_indux !=�02
      � "                   check_hndex$%=`1	*  �            $ 0 "except2
0          "   $(       ras{
                c�eck[i.dex +=01

    $   foodList = []
 @      di3tance\ist = [_ "`     bor ind%x in scanLisT:    !       #PvilthoO�)ngFor-
  (   �     ig Mq�Arra92D[index[]�[ijlexS5]] == LookingForJ  (    $ 1      food\msd.appa~d index)
%�0     h def Ca�culateDistajce
sa|f, foodX, foodY,(xvgs,"yPks):
$ !     0   rtturn lath&sqRt(foodX-xPo{)*
2 / (fondY-9PoS)**"�
` 0 $`  
      "�bor"food in foOdLiqt:�
           (lastanbe = Calcul!4aDistance(se,f, fkgd[0], fo�K0],$self.pXo[, s%lf.y�Or)
   "  0 )  0$�stanceLarv.appgnd(dkrtange)J
        If!len(distanceList� > : !          closestPoint = distanceList.index(min(distanceList))
            closestPoint = foodList[closestPoint]
            FoundDesire = True
            return FoundDesire, closestPoint
        else:
            FoundDesire = False
            closestPoint = None
            return FoundDesire, closestPoint
        

        
        #if self.state == 1 and self.creatureType == 2: #Rabbit look for mate

    def UpdatePos(self):
        MapArray2D[self.xPos][self.yPos] = self.creatureType

    def CheckIfOutBounds(self, xx, yy):
        IsOut = False
        if xx < 0:
            IsOut = True
        elif yy < 0:
            IsOut = True
        elif xx >= xGrid:
            IsOut = True
        elif yy >= yGrid:
            IsOut = True
        else:
            IsOut = False
        return IsOut

    def WalkTo(self, WalkToPos, randomBool=False, randomInt=0):
        global MapArray2D
        Fx = WalkToPos[0]
        Fy = WalkToPos[1]
        Ox = self.xPos
        Oy = self.yPos

        # UPS  
        if Fy != 9999999 and Fy > Oy and Fx < Ox or randomBool == True and randomInt == 0:
            try:
                # up left
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy + 1] = 2
                    self.xPos -= 1
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy > Oy and Fx == Ox or randomBool == True and randomInt == 1:
            try:
                # up
                if Animal.CheckIfOutBounds(self, Ox, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox][Oy + 1] = 2
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos: 
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy > Oy and Fx > Ox or randomBool == True and randomInt == 2:
            # up right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy + 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy + 1] = 2
                    self.xPos += 1
                    self.yPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        # MIDDLES
        elif Fy != 9999999 and Fy == Oy and Fx < Ox or randomBool == True and randomInt == 3:
            # left
            try:
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy]  = 2
                    self.xPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass
        

        elif Fy != 9999999 and Fy == Oy and Fx > Ox or randomBool == True and randomInt == 4:
            #right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy] = 2
                    self.xPos += 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass


        # DOWNS
        elif Fy != 9999999 and Fy < Oy and Fx < Ox or randomBool == True and randomInt == 5:
            #down left
            try:
                if Animal.CheckIfOutBounds(self, Ox - 1, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox - 1][Oy - 1] = 2
                    self.xPos -= 1
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy < Oy and Fx == Ox or randomBool == True and randomInt == 6:
            #down
            try:
                if Animal.CheckIfOutBounds(self, Ox, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox][Oy - 1] = 2
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

        elif Fy != 9999999 and Fy < Oy and Fx > Ox or randomBool == True and randomInt == 7:
            #down right
            try:
                if Animal.CheckIfOutBounds(self, Ox + 1, Oy - 1) == False:
                    MapArray2D[Ox][Oy] = 0
                    MapArray2D[Ox + 1][Oy - 1] = 2
                    self.xPos += 1
                    self.yPos -= 1
                    if Fy == self.yPos and Fx == self.xPos:
                        self.foodTotal += 5
            except:
                pass

    def MoveRandomly(self):
        randomint = random.randint(0,7)
        Animal.WalkTo(self, (9999999, 9999999),True, randomint)

    def Update(self):
        global Rabbit_Count
        self.foodTotal -= 1
        if self.foodTotal < 0:
            MapArray2D[self.xPos][self.yPos] = 1
            Entity_Dict.remove(self)
            Rabbit_Count = Rabbit_Count - 1
            return
            
        if self.state == 0:
            FoundFood, FoodPos = Animal.ScanEnviroment(self)
            if FoundFood == True:
                Animal.WalkTo(self, FoodPos)
            else:
                Animal.MoveRandomly(self)

            #if animal is looking for mate  <-- State 1
                #ScanEnviroment
                    #If mate is found
                        # Alert Mate to wait
                        # WalkTo
                    #else
                        #Walk randomly
                    
                    #If mate is close
                        #Have babies

class Rabbit(Animal):
    pass

class Fox(Animal):
    pass

def GenerateRabbit(randomSpawn=True, xPos=2, yPos=2):
    global xGrid
    global yGrid
    global MapArray2D
    global Rabbit_Count
    creatureType = 2
    foodTotal = 30
    eyeSight = 2
    state = 0

    if randomSpawn == True:
        while True:
            r_Xpos = random.randint(0, xGrid - 1)
            r_Ypos = random.randint(0, yGrid - 1)
            if MapArray2D[r_Xpos][r_Ypos] == 0:
                Entity_Dict.append(Rabbit(r_Xpos, r_Ypos, foodTotal, creatureType, eyeSight, state))
                Rabbit_Count = Rabbit_Count + 1
                break
        return

    if randomSpawn == False:
        given_xPos = xPos
        given_yPos = yPos
        if MapArray2D[given_xPos][given_yPos] == 0:
            Entity_Dict.append(Rabbit(given_xPos, given_yPos, foodTotal, creatureType, eyeSight, state))
            Rabbit_Count = Rabbit_Count + 1
            return

def GenerateFood():
    global xGrid
    global yGrid
    global MapArray2D

    while True:
        r_Xpos = random.randint(0, xGrid - 1)
        r_Ypos = random.randint(0, yGrid - 1)
        if MapArray2D[r_Xpos][r_Ypos] == 0:
            MapArray2D[r_Xpos][r_Ypos] = 1
            break
    return

def UpdateEcosystem():
    global Entity_Dict
    for Entity in Entity_Dict:
        entClass = str(type(Entity))
        
        if ".Rabbit" in entClass:
            Entity.Update()
    return




def GenerateEcoSystem(Num_of_Food=2, Num_of_Rabbits=1, Num_of_Foxes=0):
    global GridSize
    global Entity_Dict
    for _ in range(Num_of_Food):
        GenerateFood()
    
    for _ in range(Num_of_Rabbits):
        GenerateRabbit(True)

    for Entity in Entity_Dict:
        entClass = str(type(Entity))
        
        if ".Rabbit" in entClass:
            Entity.UpdatePos()

    print("Ecosystem Generated")
    return

def GenerateChart():
    line_chart = pygal.Line()
    line_chart.title = 'Rabbit Population'
    line_chart.add('Rabbits', Rabbit_Population)
    line_chart.render_to_file('Line_chart.svg')
    return

in_Food = int(input("Food Count: "))
in_Rabbits = int(input("Rabbit Count: "))
in_Foxes = int(input("Foxes Count: "))

GenerateEcoSystem(in_Food, in_Rabbits, in_Foxes)
UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
time.sleep(2)
while True:
    #GenerateFood()
    Rabbit_Population.append(Rabbit_Count)
    UpdateEcosystem()
    
    UpdateDisplay(MapArray2D, GridSize, xGrid, yGrid)
    time.sleep(0.2)
    if Rabbit_Count == 0:
        GenerateChart()
        print("Graph Generated")
        break